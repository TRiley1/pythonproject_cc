class Adventurer:
    def __init__(self, name,loot, id = None):
        self.name = name 
        self.loot = loot 
        self.id = id
        self.inventory = []

    def find_loot(self,item):
        self.inventory.append(item)