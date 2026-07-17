"""Module where all interfaces, events and exceptions live."""

from collective.volto.aemet import _
from plone.restapi.controlpanels import IControlpanel
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IAemetLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAemetSettingsControlpanel(IControlpanel):
    """Volto control panel for the AEMET."""


class IAemetSettings(Interface):
    """AEMET connector configuration"""

    location_id = schema.TextLine(
        title=_("Location ID"),
        description=_(
            "The Location ID of the AEMET service, for example '41091' "
            "to Sevilla location ID."
        ),
        required=True,
    )
