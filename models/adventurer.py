class Adventurer:
    def __init__(self, name, id = None):
        self.name = name 
        self.id = id
        self.inventory = []
        
    # item being an object
    def find_loot(self,item):
        self.inventory.extend(item)