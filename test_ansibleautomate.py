# test_ansibleautomate.py
"""
Tests for AnsibleAutomate module.
"""

import unittest
from ansibleautomate import AnsibleAutomate

class TestAnsibleAutomate(unittest.TestCase):
    """Test cases for AnsibleAutomate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnsibleAutomate()
        self.assertIsInstance(instance, AnsibleAutomate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnsibleAutomate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
