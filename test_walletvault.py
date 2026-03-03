# test_walletvault.py
"""
Tests for WalletVault module.
"""

import unittest
from walletvault import WalletVault

class TestWalletVault(unittest.TestCase):
    """Test cases for WalletVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletVault()
        self.assertIsInstance(instance, WalletVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
