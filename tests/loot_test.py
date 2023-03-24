import unittest
from models.loot import Loot

class TestLoot(unittest.TestCase):

    def setUp(self):
        self.loot = Loot('sword', 'a dirty sword')