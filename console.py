from models.item import Item
from models.adventurer import Adventurer
from models.inventory import Inventory
import repositories.item_repo as item_repo
import repositories.adventurer_repo as adventurer_repo
import repositories.inventory_repo as inv_repo

adventurers = adventurer_repo.select_all()

for adventurer in adventurers:
    print(adventurer.name)


adventurer1 = Adventurer("blah")
adventurer_repo.save(adventurer1)
item1 = Item("Sword", "Blah Blah")
item_repo.save(item1)



inventory1 = Inventory(adventurer1,item1)
inv_repo.save(inventory1)

run = adventurer_repo.select(2)
print(run)