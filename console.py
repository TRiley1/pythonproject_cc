from models.item import Item
import repositories.item_repo as item_repo

# try and add an item to the database

item1 = Item("Misc", "Rusty Spoon")  
# item1 = Item('boo', 'The Ladel of Gods', 'Ultra Rare', 1000)
# item_repo.item_update(item1)
item_repo.save(item1)

item1.name = 'The Ladel of the Gods'
item1.rarity = 'Ultra Rare'
item1.value = 1000

item_repo.item_update(item1)

results = item_repo.select_all()

for item in results:
    print(f"I have this {item.name} and it looks like a {item.type}")


# id3 =item_repo.select(2)
# print(f"This is id3 : {id3}")

# item_repo.delete(2)

backpack1  = item_repo.find_loot(3)

for item in backpack1:
    print (f"{item.name}, {item.type}")

