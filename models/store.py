class Store: 
    def __init__(self, name, money id = None):
        self.name = name 
        self.money = money 
        self.stock = {} 
        self.appraisel = {}

    # takes in an item and adds a random new item.name, item.rarity and item.value
    # appraisel is a dict of three keys: name, rarity and item te values are a list of names, rarities and values 
    # {name: [list of names],
    #  rarities: [list of rarities],
    # values: [list of values]}

    def appraisel(item, appraisel,randomNum):
        item.name = appraisel['name'][randomNum]
        item.rarity = appraisel['rarity'][randomNum]
        item.value = appraisel['value'][randomNum]

    # I think this could also be done with an extra table in the database filled with name, rarity and value and assiging.
    # doing an SQL random query to return a random object. 