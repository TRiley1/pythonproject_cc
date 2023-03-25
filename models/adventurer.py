class Adventurer:
    def __init__(self, name, id = None):
        self.name = name 
        self.id = id
        self.inventory = []

    def find_loot(self,item):
        self.inventory.append(item)