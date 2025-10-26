# test_solidstart.py
"""
Tests for SolidStart module.
"""

import unittest
from solidstart import SolidStart

class TestSolidStart(unittest.TestCase):
    """Test cases for SolidStart class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidStart()
        self.assertIsInstance(instance, SolidStart)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidStart()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
