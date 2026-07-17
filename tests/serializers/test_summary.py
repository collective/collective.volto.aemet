"""Test JSONSummarySerializerMetadata."""

from collective.volto.aemet.serializers.summary import JSONSummarySerializerMetadata
from plone.restapi.interfaces import IJSONSummarySerializerMetadata
from zope.interface.verify import verifyClass
from zope.interface.verify import verifyObject

import unittest


class TestJSONSummarySerializerMetadata(unittest.TestCase):
    """Test cases for JSONSummarySerializerMetadata."""

    def setUp(self):
        """Set up test fixtures."""
        self.serializer = JSONSummarySerializerMetadata()

    def test_interface_compliance(self):
        """Test that the class implements IJSONSummarySerializerMetadata."""
        # Verify class implementation
        verifyClass(IJSONSummarySerializerMetadata, JSONSummarySerializerMetadata)
        # Verify object implementation
        verifyObject(IJSONSummarySerializerMetadata, self.serializer)

    def test_default_metadata_returns_expected_fields(self):
        """Test that default_metadata returns the correct set of fields."""
        expected_fields = {"image_field", "image_scales", "effective", "Subject"}
        result = self.serializer.default_metadata()

        self.assertIsInstance(result, set)
        self.assertEqual(result, expected_fields)

    def test_default_metadata_contains_image_field(self):
        """Test that 'image_field' is in default metadata fields."""
        result = self.serializer.default_metadata()
        self.assertIn("image_field", result)

    def test_default_metadata_contains_image_scales(self):
        """Test that 'image_scales' is in default metadata fields."""
        result = self.serializer.default_metadata()
        self.assertIn("image_scales", result)

    def test_default_metadata_contains_effective(self):
        """Test that 'effective' is in default metadata fields."""
        result = self.serializer.default_metadata()
        self.assertIn("effective", result)

    def test_default_metadata_contains_subject(self):
        """Test that 'Subject' is in default metadata fields."""
        result = self.serializer.default_metadata()
        self.assertIn("Subject", result)

    def test_default_metadata_has_correct_count(self):
        """Test that default_metadata returns exactly 4 fields."""
        result = self.serializer.default_metadata()
        self.assertEqual(len(result), 4)

    def test_field_accessors_returns_dict(self):
        """Test that field_accessors returns a dictionary."""
        result = self.serializer.field_accessors()
        self.assertIsInstance(result, dict)

    def test_field_accessors_returns_empty_dict(self):
        """Test that field_accessors returns an empty dictionary."""
        result = self.serializer.field_accessors()
        self.assertEqual(result, {})

    def test_non_metadata_attributes_returns_set(self):
        """Test that non_metadata_attributes returns a set."""
        result = self.serializer.non_metadata_attributes()
        self.assertIsInstance(result, set)

    def test_non_metadata_attributes_returns_empty_set(self):
        """Test that non_metadata_attributes returns an empty set."""
        result = self.serializer.non_metadata_attributes()
        self.assertEqual(result, set())

    def test_blocklisted_attributes_returns_set(self):
        """Test that blocklisted_attributes returns a set."""
        result = self.serializer.blocklisted_attributes()
        self.assertIsInstance(result, set)

    def test_blocklisted_attributes_returns_empty_set(self):
        """Test that blocklisted_attributes returns an empty set."""
        result = self.serializer.blocklisted_attributes()
        self.assertEqual(result, set())
