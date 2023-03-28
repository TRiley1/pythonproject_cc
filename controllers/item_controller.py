from flask import Blueprint, Flask, redirect, render_template, request
from models.item import Item
from models.adventurer import *
from models.inventory import Inventory
import pdb
import repositories.item_repo as item_repo
import repositories.inventory_repo as invo_repo
import repositories.adventurer_repo as adventurer_repo

item_blueprint = Blueprint("item", __name__)

@item_blueprint.route("/items/<user_id>")
def items(user_id):
    items = item_repo.select_all()
    advs = adventurer_repo.select(user_id)
    return render_template("/items/index.html", items = items, adventurer = advs, id = user_id)

@item_blueprint.route("/items/<weapon_id>/update", methods = ['POST'])
def sell(weapon_id):
    # pdb.set_trace()
    adventurer = adventurer_repo.select(request.form['adventurer_id'] )
    selling_item = item_repo.select(weapon_id)
    
    if adventurer.wallet >= selling_item.value:
        inventory = Inventory(adventurer, selling_item)
        adventurer.spend_money(selling_item.value)
        invo_repo.save(inventory)
        adventurer_repo.adventurer_update(adventurer)
        return redirect("/items/" + str(adventurer.id))

    else: return redirect('/items/no')

@item_blueprint.route('/items/no')
def not_enough():
    return render_template('items/nah.html')
    
    