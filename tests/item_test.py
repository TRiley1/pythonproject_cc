import unittest
from models.item import Item

class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item("Sword", "The Sword of Gods", "Super Rare", 100000)