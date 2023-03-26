from models.item import Item
from models.adventurer import Adventurer
from models.inventory import Inventory
import repositories.item_repo as item_repo
import repositories.adventurer_repo as adventurer_repo
import repositories.inventory_repo as inv_repo

# try and add an item to the database

# item1 = Item("Misc", "Rusty Spoon")
 
# # item1 = Item('boo', 'The Ladel of Gods', 'Ultra Rare', 1000)
# # item_repo.item_update(item1)

# item_repo.save(item1)


# item1.name = 'The Ladel of the Gods'
# item1.rarity = 'Ultra Rare'
# item1.value = 1000

# adventurer1 = Adventurer("Indiana") 
# adventurer_repo.save(adventurer1)
# adventurer1.name = 'Dora the Explorer'
# adventurer_repo.adventurer_update(adventurer1)

# item_repo.item_update(item1)

# results = item_repo.select_all()

# for item in results:
#     print(f"I have this {item.name} and it looks like a {item.type}")


# # id3 =item_repo.select(2)
# # print(f"This is id3 : {id3}")

# # item_repo.delete(2)

# backpack1  = item_repo.find_loot(3)

# for item in backpack1:
#     print (f"{item.name}, {item.type}")


# inventory1 = Inventory(adventurer1, item1)
# inv_repo.save(inventory1)

# adventurer2 = Adventurer("Wasll-E")
# adventurer_repo.save(adventurer2)

# inventory2 = Inventory(adventurer2, item1)
# inv_repo.save(inventory2)
# inventory2.adventurer.id = 2
# inv_repo.update(inventory2)

item1 = Item("misc", "Rusty Spoon")
item_repo.save(item1)

adventurer1 = Adventurer("The Great Khali")
adventurer_repo.save(adventurer1)

inventory1 = Inventory(adventurer1, item1)
inv_repo.save(inventory1)

# now because many adventurers can hold item1 I can't just edit item1 it'll change for everyone that holds it. 
# 1. create a new item. 
# 2. delete adventurer holding rusty spoon. 
# 3 assign adventurer new item. 

item2 = item_repo.select(2)
item_repo.save(item2)

inventory2 = Inventory(adventurer1, item2)
inv_repo.save(inventory2)



