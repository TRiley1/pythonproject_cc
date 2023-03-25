from db.run_sql import run_sql
from models.item import Item

def save(item): 
    sql = 'INSERT INTO items (type, name, rarity, value) VALUES (%s,%s,%s,%s) RETURNING *'
    values = [item.type, item.name, item.rarity, item.value]
    results = run_sql(sql, values)

    id = results[0]['id']
    item.id = id

def select_all():
    items = []
    sql = 'SELECT * FROM items'
    results = run_sql(sql)

    for row in results:
        new_item = Item(row['type'], row['name'], row['rarity'], row['value'])
        items.append(new_item)

    return items