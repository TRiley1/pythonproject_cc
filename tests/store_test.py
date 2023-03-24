import unittest
from models.store import Store
from models.item import Item
from models.adventurer import Adventurer
from models.loot import Loot 

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = 