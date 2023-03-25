from models.item import Item
import repositories.item_repo as item_repo

# try and add an item to the database

item = Item("Misc", "Rusty Spoon")
item_repo.save(item)