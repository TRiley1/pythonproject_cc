import unittest
from models.adventurer import Adventurer
from models.loot import Loot
from models.item import Item

class TestAdventurer(unittest.TestCase):

    def setUp(self):
        self.loot = Loot("Helmet", "Rusty Helmet")
        self.loot1 = Loot("boots", "Worn boots")
        self.item = Item("Sword", "The Sword of Gods", "Super Rare", 100000)
        self.item = Item("Sword", "The Sword of Gods", "Super Rare", 100000)
        self.adventurer = Adventurer("Steve the Great", [self.loot, self.loot1],[self.item, self.item])