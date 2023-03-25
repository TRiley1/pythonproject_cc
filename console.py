from models.item import Item
import repositories.item_repo as item_repo

# try and add an item to the database

item = Item("Misc", "Rusty Spoon")
item_repo.save(item)

results = item_repo.select_all()

for item in results:
    print(f"I have this {item.name} and it looks like a {item.type}")


id3 =item_repo.select(2)
print(f"This is id3 : {id3}")

item_repo.delete(2)