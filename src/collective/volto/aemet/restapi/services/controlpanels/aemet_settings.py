from collective.volto.aemet.interfaces import IAemetSettings
from collective.volto.aemet.interfaces import (
    IAemetSettingsControlpanel,
)
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(Interface, Interface)
@implementer(IAemetSettingsControlpanel)
class AemetSettingsControlpanel(RegistryConfigletPanel):
    """Volto control panel for AEMET settings."""

    schema = IAemetSettings
    configlet_id = "AemetSettings"
    configlet_category_id = "Products"
    schema_prefix = "aemet"
