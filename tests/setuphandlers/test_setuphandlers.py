"""Test setuphandlers."""

from collective.volto.aemet.setuphandlers import HiddenProfiles
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface.verify import verifyClass
from zope.interface.verify import verifyObject

import unittest


class TestHiddenProfiles(unittest.TestCase):
    """Test cases for HiddenProfiles."""

    def setUp(self):
        """Set up test fixtures."""
        self.hidden_profiles = HiddenProfiles()

    def test_interface_compliance(self):
        """Test that HiddenProfiles implements INonInstallable."""
        # Verify class implementation
        verifyClass(INonInstallable, HiddenProfiles)
        # Verify object implementation
        verifyObject(INonInstallable, self.hidden_profiles)

    def test_get_non_installable_profiles_returns_list(self):
        """Test that getNonInstallableProfiles returns a list."""
        result = self.hidden_profiles.getNonInstallableProfiles()
        self.assertIsInstance(result, list)

    def test_get_non_installable_profiles_contains_uninstall(self):
        """Test that uninstall profile is in non-installable profiles."""
        result = self.hidden_profiles.getNonInstallableProfiles()
        self.assertIn("collective.volto.aemet:uninstall", result)

    def test_get_non_installable_profiles_count(self):
        """Test that getNonInstallableProfiles returns expected number of items."""
        result = self.hidden_profiles.getNonInstallableProfiles()
        self.assertEqual(len(result), 1)

    def test_get_non_installable_products_returns_list(self):
        """Test that getNonInstallableProducts returns a list."""
        result = self.hidden_profiles.getNonInstallableProducts()
        self.assertIsInstance(result, list)

    def test_get_non_installable_products_contains_upgrades(self):
        """Test that upgrades package is in non-installable products."""
        result = self.hidden_profiles.getNonInstallableProducts()
        self.assertIn("collective.volto.aemet.upgrades", result)

    def test_get_non_installable_products_count(self):
        """Test that getNonInstallableProducts returns expected number of items."""
        result = self.hidden_profiles.getNonInstallableProducts()
        self.assertEqual(len(result), 1)
