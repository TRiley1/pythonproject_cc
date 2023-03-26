from db.run_sql import run_sql
from models.inventory import Inventory
from models.item import Item
import repositories.item_repo as item_repo
from models.adventurer import Adventurer
import repositories.adventurer_repo as adventurer_repo

def save(inventory):
    sql = "INSERT INTO item_adv (adventurer_id, loot_id) VALUES (%s, %s) RETURNING id"
    values = [inventory.adventurer.id, inventory.item.id]
    results = run_sql(sql, values)

    id = results[0]['id']
    inventory.id = id

def update(inventory):
    sql = "UPDATE item_adv SET (adventurer_id, loot_id) = (%s, %s) WHERE id = %s"
    values = [inventory.adventurer.id, inventory.item.id, inventory.id]
    run_sql(sql, values)

def delete(inventory):
    sql = "DELETE FROM item_adv WHERE id = %s"
    values = [inventory.id]
    run_sql(sql, values)
