class Adventurer:
    def __init__(self, name, wallet,id = None):
        self.name = name 
        self.id = id
        self.wallet = wallet 
        # self.inventory = []
        
    # item being an object
    def find_loot(self,item):
        self.inventory.extend(item)

    def spend_money(self,value):
       self.wallet -= value