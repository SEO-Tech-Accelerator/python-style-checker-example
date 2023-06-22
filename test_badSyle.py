import unittest
from badStyle import add

class TestBadStyle(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(add(1,1), 2)
