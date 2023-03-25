from db.run_sql import run_sql
from models.adventurer import Adventurer
from models.adventurer import *
from models.item import Item

import repositories.item_repo as item_repo

def save(adventurer):
    sql = "INSERT INTO adventurers (name) VALUES (%s) RETURNING *"
    values = [adventurer.name]
    results = run_sql(sql, values)

    id = results[0]['id']
    adventurer.id = id

def delete_all():
    sql = "DELETE * FROM adventurers"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM adventurers WHERE id = %s"
    values = [id]
    run_sql(sql, values) 

def select_all():
    adventurers = []
    sql = 'SELECT * FROM adventurers'
    results = run_sql(sql)

    for row in results:
        new_item = Item(row['name'])
        adventurers.append(new_item)

    return adventurers

def select(id):
    sql = 'SELECT * FROM adventurers WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        item = Item(result['name'])

    return item