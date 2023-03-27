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
