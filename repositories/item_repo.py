from db.run_sql import run_sql
from models.item import Item

def save(item): 
    sql = 'INSERT INTO items (type, name, rarity, value) VALUES (%s,%s,%s,%s,%s) RETURNING *'
    values = [item.type, item.name, item.rarity, item.value, item.image]
    results = run_sql(sql, values)

    id = results[0]['id']
    item.id = id

def select_all():
    items = []
    sql = 'SELECT * FROM items'
    results = run_sql(sql)

    for row in results:
        new_item = Item(row['type'], row['name'], row['rarity'], row['value'], row['image'])
        items.append(new_item)

    return items

def select(id):
    sql = 'SELECT * FROM items WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        item = Item(result['type'], result['name'], result['rarity'], result['value'], result['image'])

    return item

def delete_all():
    sql = "DELETE * FROM items"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def item_update(item):
    sql = "UPDATE items \
        SET (type, name, rarity, value) = (%s,%s,%s,%s,%s) \
        WHERE id = %s"
    values = [item.type, item.name, item.rarity, item.value, item.image, item.id]
    run_sql(sql,values)

# gives a random number of loot objects

def find_loot(num):
    backpack = []
    sql = "SELECT * FROM items \
        WHERE value IS NULL \
        ORDER BY RANDOM() LIMIT(%s)"
    values = [num]
    results = run_sql(sql, values)

    for loot in results:
        new_loot = Item(loot['type'], loot['name'], loot['rarity'], loot['image'])
        backpack.append(new_loot)

    return backpack


    

