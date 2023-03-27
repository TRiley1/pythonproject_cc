from models.item import Item
from models.adventurer import Adventurer
from models.inventory import Inventory
import repositories.item_repo as item_repo
import repositories.adventurer_repo as adventurer_repo
import repositories.inventory_repo as inv_repo

adventurers = adventurer_repo.select_all()

for adventurer in adventurers:
    print(adventurer.name)

run = adventurer_repo.select(2)
print(run)