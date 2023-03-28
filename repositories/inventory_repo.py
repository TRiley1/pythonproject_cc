from db.run_sql import run_sql
from models.inventory import Inventory
from models.item import Item
import pdb
import repositories.item_repo as item_repo
from models.adventurer import Adventurer
import repositories.adventurer_repo as adventurer_repo

def save(inventory):
    sql = "INSERT INTO inventory (adventurer_id, item_id) VALUES (%s, %s) RETURNING *"
    values = [inventory.adventurer.id, inventory.item.id]
    results = run_sql(sql, values)
    
    id = results[0]['id']
    inventory.id = id

def update(inventory):
    sql = "UPDATE inventory SET (adventurer_id, item_id) = (%s, %s) WHERE id = %s"
    values = [inventory.adventurer.id, inventory.item.id, inventory.id]
    run_sql(sql, values)


def delete(inventory):
    sql = "DELETE FROM inventory WHERE id = %s"
    values = [inventory.id]
    run_sql(sql, values)

def select_all():
    inventories = []
    sql = "SELECT * FROM inventory"
    results = run_sql(sql)

    for inventory in results:
        adventurer = adventurer_repo.select(inventory["adventurer_id"])
        item = item_repo.select(inventory["item_id"])
        inventory = Inventory(adventurer, item, inventory['id'])
        inventories.append(inventory)


    return inventories

def select_adventurer_inventory(user_id):
    items = []
    sql = 'SELECT items.* FROM items INNER JOIN inventory ON inventory.item_id = items.id WHERE inventory.adventurer_id = %s'
    values = [user_id]
    results = run_sql(sql,values)

    for row in results:
        new_item = Item(row['type'], row['name'], row['rarity'], row['value'], row['image'],row['id'])
        items.append(new_item)
    return items