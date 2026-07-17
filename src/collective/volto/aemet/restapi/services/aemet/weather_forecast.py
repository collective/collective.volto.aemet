"""Weather forecast service for AEMET data."""

from collective.volto.aemet import _
from datetime import date
from datetime import datetime
from plone import api as ploneapi
from plone.restapi.services import Service
from xml.etree import ElementTree

import requests


class WeatherForecastGet(Service):
    """Weather forecast data service."""

    def _get_current_time_period(self, current_hour):
        """Determine the appropriate time period based on current hour.

        Args:
            current_hour: Current hour (0-23)

        Returns:
            String representing the time period (e.g., "00-06", "06-12", etc.)
        """
        if 0 <= current_hour < 6:
            return "00-06"
        elif 6 <= current_hour < 12:
            return "06-12"
        elif 12 <= current_hour < 18:
            return "12-18"
        else:  # 18-24
            return "18-24"

    def _get_sky_state_for_period(self, day_element, target_period):
        """Get the sky state for a specific time period.

        Args:
            day_element: XML element for the day
            target_period: Target time period (e.g., "12-18")

        Returns:
            Tuple of (description, value) or (None, None) if not found
        """
        # Find all estado_cielo elements
        sky_states = day_element.findall("estado_cielo")

        for sky_state in sky_states:
            period = sky_state.get("periodo")
            if period == target_period:
                description = sky_state.get("descripcion", "")
                value = sky_state.text if sky_state.text else None
                # Only return if both description and value are present
                if description and value:
                    return (description, value)

        return (None, None)

    def _get_location_id(self):
        """Get the location_id from the aemet-settings controlpanel."""
        return ploneapi.portal.get_registry_record("aemet.location_id")

    def reply(self):
        """Return weather data from AEMET."""
        try:
            # Default to Sevilla if not set
            location_id = self._get_location_id() or "41091"
            url = f"https://www.aemet.es/xml/municipios/localidad_{location_id}.xml"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # Parse XML and convert to JSON structure
                root = ElementTree.fromstring(response.content)  # noqa: S314

                # Get current hour to determine the appropriate time period
                current_hour = datetime.now().hour

                forecast = []
                province = root.findall(".//provincia")
                name = root.findall(".//nombre")
                for day in root.findall(".//dia"):
                    day_date = day.get("fecha")
                    # Only include today's forecast
                    if datetime.strptime(day_date, "%Y-%m-%d").date() == date.today():
                        temp = day.find("temperatura")

                        # Determine the appropriate time period
                        time_period = self._get_current_time_period(current_hour)

                        # Get sky state for the current time period
                        sky_description, sky_value = self._get_sky_state_for_period(
                            day, time_period
                        )

                        # Fallback to broader periods if specific period not found
                        if not sky_description or not sky_value:
                            # Try 12-hour periods
                            fallback_period = "00-12" if current_hour < 12 else "12-24"
                            sky_description, sky_value = self._get_sky_state_for_period(
                                day, fallback_period
                            )

                        # Final fallback to 00-24
                        if not sky_description or not sky_value:
                            sky_description, sky_value = self._get_sky_state_for_period(
                                day, "00-24"
                            )

                        forecast.append({
                            "date": day_date,
                            "province": province[0].text if province else None,
                            "name": name[0].text if name else None,
                            "tempMin": (
                                temp.find("minima").text
                                if temp is not None and temp.find("minima") is not None
                                else None
                            ),
                            "tempMax": (
                                temp.find("maxima").text
                                if temp is not None and temp.find("maxima") is not None
                                else None
                            ),
                            "skyState": sky_description or _("Not available"),
                            "skyStateValue": sky_value or "11",
                            "timePeriod": time_period,
                            "currentHour": current_hour,
                        })

                response_json = {"forecast": forecast}
                return response_json
            else:
                self.request.response.setStatus(response.status_code)
                return {"error": "Failed to fetch weather forecast data"}
        except Exception as e:
            self.request.response.setStatus(500)
            return {"error": str(e)}
