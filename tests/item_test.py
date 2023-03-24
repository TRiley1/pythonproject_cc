import unittest
from models.item import Item

class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item("Sword", "The Sword of Gods", "Super Rare", 100000)

    def test_item_has_name(self):
        self.assertEqual("The Sword of Gods", self.item.name)

    def test_item_has_value(self):
        self.assertEqual(100000, self.item.value)