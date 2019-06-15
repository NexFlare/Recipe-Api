from django.test import TestCase

from app.calc import add, subtract


class ClacTest(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 4), 7)
    
    def test_subtract_numbers(self):
        """Test that two numbers are subtracted"""
        self.assertEqual(subtract(3, 2), 1)
