"""
Basic unit test for lambda package
"""

import unittest
from random import randint

from example_module import COLORS, increment
from oop_example import SocialMediaUser


class SocialMediaUserTests(unittest.TestCase):
    """Tests for the usage of Social Media Users in our Social Media Class"""

    def setUp(self):
        self.user1 = SocialMediaUser(name='Jimmy', location='France')
        self.user2 = SocialMediaUser(name='Craig', location='Kenya')
        self.user3 = SocialMediaUser(name='Nick', location='Nova Scotia')

    def test_name(self):
        """Testing the name attribute"""
        self.assertEqual(self.user1.name, 'Jimmy')
        self.assertEqual(self.user2.name, 'Craig')

    def test_location(self):
        """Testing the location attribute"""
        self.assertEqual(self.user1.location, 'France')
        self.assertEqual(self.user2.location, 'Kenya')

    def test_default_upvotes(self):
        """Testing default upvotes"""
        self.assertEqual(self.user3.upvotes, 0)

    def test_unpopular(self):
        """Testing is popular method"""
        self.assertFalse(self.user3.is_popular())
        self.user3.receive_upvotes(randint(101, 10000))
        self.assertTrue(self.user3.is_popular())


class ExampleTests(unittest.TestCase):
    """Making sure examples work as expected"""

    def test_increment(self):
        """Testing that increment adds one to a number"""
        x0 = 0
        y0 = increment(x0)  # y0 should be 1
        self.assertEqual(y0, 1)

        x1 = 100
        y1 = increment(x1)  # y1 should be 101
        self.assertTrue(y1, 101)

        x2 = -1
        y2 = increment(x2)  # y2 should be 0
        self.assertEqual(y2, 0)

        x3 = -1.5
        y3 = increment(x3)  # y3 should be -0.5
        self.assertEqual(y3, -0.5)

    def test_colors(self):
        "Testing the presence/absence of members in the colors list COLORS = ['cyan', 'teal', 'mauve', 'blue']"
        self.assertIn('blue', COLORS)
        self.assertNotIn('brown', COLORS)

    def test_colors_number(self):
        """Testing that we have expected numbers of colors"""
        self.assertEqual(len(COLORS), 4)


if __name__ == '__main__':
    unittest.main()
