"""Tests for the WeatherForecastGet REST API service."""

from collective.volto.aemet.restapi.services.aemet.weather_forecast import (
    WeatherForecastGet,
)
from unittest.mock import MagicMock
from unittest.mock import patch
from xml.etree import ElementTree

import datetime as _dt_module
import pytest


def _make_service(request=None):
    svc = WeatherForecastGet()
    svc.context = MagicMock()
    svc.request = request or MagicMock()
    return svc


def _build_xml(day_date_str, periods=None, temp_block=None):
    """Build a minimal AEMET-style XML response.

    Args:
        day_date_str: Date string for the <dia> element (e.g. "2026-04-12").
        periods: List of (periodo, descripcion, text) tuples for estado_cielo
                 elements.  Pass ``[]`` for no sky states.  Pass ``None`` for
                 a sane default that includes a matching period.
        temp_block: Raw XML string for a <temperatura> block, or ``False`` to
                    omit the element entirely.  ``None`` means the default
                    ``<temperatura><minima>12</minima><maxima>22</maxima></temperatura>``.
    """
    if temp_block is None:
        temp_xml = "<temperatura><minima>12</minima><maxima>22</maxima></temperatura>"
    elif temp_block is False:
        temp_xml = ""
    else:
        temp_xml = temp_block

    sky_xml = ""
    if periods is not None:
        for periodo, descripcion, text in periods:
            sky_xml += (
                f'<estado_cielo periodo="{periodo}" '
                f'descripcion="{descripcion}">{text}</estado_cielo>\n'
            )

    return (
        f"<root><dia fecha='{day_date_str}'>{temp_xml}{sky_xml}</dia></root>"
    ).encode()


class TestGetCurrentTimePeriod:
    """Unit tests for WeatherForecastGet._get_current_time_period."""

    def setup_method(self):
        self.svc = _make_service()

    @pytest.mark.parametrize(
        "hour,expected",
        [
            (0, "00-06"),
            (5, "00-06"),
            (6, "06-12"),
            (11, "06-12"),
            (12, "12-18"),
            (17, "12-18"),
            (18, "18-24"),
            (23, "18-24"),
        ],
    )
    def test_time_period_mapping(self, hour, expected):
        assert self.svc._get_current_time_period(hour) == expected


class TestGetSkyStateForPeriod:
    """Unit tests for WeatherForecastGet._get_sky_state_for_period."""

    def setup_method(self):
        self.svc = _make_service()

    @staticmethod
    def _day(sky_states):
        parts = "".join(
            f'<estado_cielo periodo="{p}" descripcion="{d}">{t}</estado_cielo>'
            for p, d, t in sky_states
        )
        return ElementTree.fromstring(f"<dia>{parts}</dia>")  # noqa: S314

    def test_returns_description_and_value(self):
        day = self._day([("12-18", "Soleado", "11")])
        assert self.svc._get_sky_state_for_period(day, "12-18") == ("Soleado", "11")

    def test_period_not_present_returns_none_tuple(self):
        day = self._day([("06-12", "Nublado", "15")])
        assert self.svc._get_sky_state_for_period(day, "12-18") == (None, None)

    def test_empty_day_element_returns_none_tuple(self):
        day = ElementTree.fromstring("<dia></dia>")  # noqa: S314
        assert self.svc._get_sky_state_for_period(day, "12-18") == (None, None)

    def test_skips_entry_with_empty_description(self):
        day = self._day([("12-18", "", "11")])
        assert self.svc._get_sky_state_for_period(day, "12-18") == (None, None)

    def test_skips_entry_with_no_text(self):
        xml = '<dia><estado_cielo periodo="12-18" descripcion="Soleado"></estado_cielo></dia>'
        day = ElementTree.fromstring(xml)  # noqa: S314
        assert self.svc._get_sky_state_for_period(day, "12-18") == (None, None)


class TestGetLocationId:
    """Unit tests for WeatherForecastGet._get_location_id."""

    def setup_method(self):
        self.svc = _make_service()

    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.ploneapi")
    def test_returns_registry_value(self, mock_ploneapi):
        """Returns the value stored in the Plone registry."""
        mock_ploneapi.portal.get_registry_record.return_value = "28058"
        assert self.svc._get_location_id() == "28058"
        mock_ploneapi.portal.get_registry_record.assert_called_once_with(
            "aemet.location_id"
        )

    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.ploneapi")
    def test_returns_none_when_not_configured(self, mock_ploneapi):
        """Returns None when the registry record has no value set."""
        mock_ploneapi.portal.get_registry_record.return_value = None
        assert self.svc._get_location_id() is None


class TestWeatherForecastGetReply:
    """Integration-style unit tests for WeatherForecastGet.reply()."""

    def setup_method(self):
        self.request_mock = MagicMock()
        self.svc = _make_service(request=self.request_mock)
        self.today_str = _dt_module.date.today().strftime("%Y-%m-%d")
        # Avoid requiring an active Plone site in unit tests
        self.svc._get_location_id = MagicMock(return_value="28058")

    def _mock_get(self, status_code=200, xml_content=b""):
        r = MagicMock()
        r.status_code = status_code
        r.content = xml_content
        return r

    # ------------------------------------------------------------------
    # Successful (200) paths
    # ------------------------------------------------------------------

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_primary_period_found(self, mock_dt, mock_get):
        """Sky state is found at the exact current time period."""
        mock_dt.now.return_value.hour = 14  # → "12-18"
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml(self.today_str, periods=[("12-18", "Despejado", "11")])
        mock_get.return_value = self._mock_get(200, xml)

        result = self.svc.reply()

        assert "forecast" in result
        item = result["forecast"][0]
        assert item["skyState"] == "Despejado"
        assert item["skyStateValue"] == "11"
        assert item["timePeriod"] == "12-18"
        assert item["tempMin"] == "12"
        assert item["tempMax"] == "22"
        assert item["currentHour"] == 14

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_fallback_to_00_12_when_hour_lt_12(self, mock_dt, mock_get):
        """Falls back to '00-12' period when primary '00-06' period is absent."""
        mock_dt.now.return_value.hour = 3  # → "00-06"
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml(self.today_str, periods=[("00-12", "Nublado", "15")])
        mock_get.return_value = self._mock_get(200, xml)

        item = self.svc.reply()["forecast"][0]
        assert item["skyState"] == "Nublado"
        assert item["skyStateValue"] == "15"

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_fallback_to_12_24_when_hour_gte_12(self, mock_dt, mock_get):
        """Falls back to '12-24' period when primary '18-24' period is absent."""
        mock_dt.now.return_value.hour = 20  # → "18-24"
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml(self.today_str, periods=[("12-24", "Tormenta", "54")])
        mock_get.return_value = self._mock_get(200, xml)

        item = self.svc.reply()["forecast"][0]
        assert item["skyState"] == "Tormenta"
        assert item["skyStateValue"] == "54"

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_final_fallback_to_00_24(self, mock_dt, mock_get):
        """Falls back to '00-24' when both primary and 12-hour periods are absent."""
        mock_dt.now.return_value.hour = 14  # → "12-18", first fallback "12-24"
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml(self.today_str, periods=[("00-24", "Cubierto", "8")])
        mock_get.return_value = self._mock_get(200, xml)

        item = self.svc.reply()["forecast"][0]
        assert item["skyState"] == "Cubierto"
        assert item["skyStateValue"] == "8"

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_no_sky_state_uses_default_values(self, mock_dt, mock_get):
        """When no sky state can be found, defaults are used."""
        mock_dt.now.return_value.hour = 14
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml(self.today_str, periods=[])  # no sky states
        mock_get.return_value = self._mock_get(200, xml)

        item = self.svc.reply()["forecast"][0]
        assert item["skyStateValue"] == "11"
        assert "Not available" in str(item["skyState"])

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_no_temperatura_element_gives_none_temps(self, mock_dt, mock_get):
        """When the <temperatura> element is absent, min/max are None."""
        mock_dt.now.return_value.hour = 9  # → "06-12"
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml(
            self.today_str,
            periods=[("06-12", "Soleado", "11")],
            temp_block=False,
        )
        mock_get.return_value = self._mock_get(200, xml)

        item = self.svc.reply()["forecast"][0]
        assert item["tempMin"] is None
        assert item["tempMax"] is None

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_temperatura_without_children_gives_none_temps(self, mock_dt, mock_get):
        """When <temperatura> has no minima/maxima children, min/max are None."""
        mock_dt.now.return_value.hour = 9
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml(
            self.today_str,
            periods=[("06-12", "Soleado", "11")],
            temp_block="<temperatura></temperatura>",
        )
        mock_get.return_value = self._mock_get(200, xml)

        item = self.svc.reply()["forecast"][0]
        assert item["tempMin"] is None
        assert item["tempMax"] is None

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    @patch("collective.volto.aemet.restapi.services.aemet.weather_forecast.datetime")
    def test_non_today_days_are_excluded(self, mock_dt, mock_get):
        """Days whose date does not match today must not appear in the forecast."""
        mock_dt.now.return_value.hour = 9
        mock_dt.strptime.side_effect = _dt_module.datetime.strptime

        xml = _build_xml("1999-01-01", periods=[("06-12", "Soleado", "11")])
        mock_get.return_value = self._mock_get(200, xml)

        assert self.svc.reply()["forecast"] == []

    # ------------------------------------------------------------------
    # Error paths
    # ------------------------------------------------------------------

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    def test_non_200_response_returns_error(self, mock_get):
        mock_get.return_value = self._mock_get(503)

        result = self.svc.reply()

        assert result == {"error": "Failed to fetch weather forecast data"}
        self.request_mock.response.setStatus.assert_called_once_with(503)

    @patch(
        "collective.volto.aemet.restapi.services.aemet.weather_forecast.requests.get"
    )
    def test_exception_returns_500_error(self, mock_get):
        mock_get.side_effect = ConnectionError("network failure")

        result = self.svc.reply()

        assert "error" in result
        assert "network failure" in result["error"]
        self.request_mock.response.setStatus.assert_called_once_with(500)
