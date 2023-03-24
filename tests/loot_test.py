import unittest
from models.loot import Loot

class TestItem(unittest.TestCase):

    def setUp(self):
        self.loot = Loot('sword', 'a dirty sword')