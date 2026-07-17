from plone.restapi.interfaces import IJSONSummarySerializerMetadata
from zope.interface import implementer


@implementer(IJSONSummarySerializerMetadata)
class JSONSummarySerializerMetadata:
    """Additional metadata to be exposed on listings."""

    def default_metadata(self):
        """Returns a set with default metadata to be serialized."""
        return {"image_field", "image_scales", "effective", "Subject"}

    def field_accessors(self):
        """Return field accessors mapping."""
        return {}

    def non_metadata_attributes(self):
        """Return non-metadata attributes."""
        return set()

    def blocklisted_attributes(self):
        """Return blocklisted attributes."""
        return set()
