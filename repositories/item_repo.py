from db.run_sql import run_sql
from models.item import Item

def save(item): 
    sql = 'INSERT INTO items (type, name, rarity, value) VALUES (%s,%s,%s,%s) RETURNING *'
    values = [item.type, item.name, item.rarity, item.value]
    results = run_sql(sql, values)

    id = results[0]['id']
    item.id = id
