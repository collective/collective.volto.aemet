from collective.volto.aemet import _
from collective.volto.aemet.interfaces import IAemetSettings
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm


class AemetEditForm(RegistryEditForm):
    schema = IAemetSettings
    schema_prefix = "aemet"
    label = _("AEMET Settings")
    description = _("Define the parameters for get data from AEMET service.")

    def updateFields(self):
        super().updateFields()

    def updateWidgets(self):
        super().updateWidgets()


class AemetControlPanel(ControlPanelFormWrapper):
    form = AemetEditForm
