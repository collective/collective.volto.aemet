"""Tests for the AemetEditForm controlpanel."""

from collective.volto.aemet.controlpanels.aemet_settings import (
    AemetControlPanel,
)
from collective.volto.aemet.controlpanels.aemet_settings import (
    AemetEditForm,
)
from unittest.mock import patch


class TestAemetEditForm:
    def test_update_fields_delegates_to_super(self):
        with patch.object(
            AemetEditForm.__bases__[0], "updateFields"
        ) as mock_uf:
            form = object.__new__(AemetEditForm)
            form.updateFields()
        mock_uf.assert_called_once()

    def test_update_widgets_delegates_to_super(self):
        with patch.object(
            AemetEditForm.__bases__[0], "updateWidgets"
        ) as mock_uw:
            form = object.__new__(AemetEditForm)
            form.updateWidgets()
        mock_uw.assert_called_once()

    def test_control_panel_uses_edit_form(self):
        assert AemetControlPanel.form is AemetEditForm
