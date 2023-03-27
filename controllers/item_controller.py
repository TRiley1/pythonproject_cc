from flask import Blueprint, Flask, redirect, render_template, request
from models.item import Item
from models.adventurer import Adventurer
from models.inventory import Inventory
import repositories.item_repo as item_repo
import repositories.inventory_repo as invo_repo
import repositories.adventurer_repo as adventurer_repo

item_blueprint = Blueprint("item", __name__)

@item_blueprint.route("/store/<id>")
def items(id):
    items = item_repo.select_store_stock(1)
    advs = adventurer_repo.select(id)
    return render_template("/store/index.html", items = items, adventurers = advs, id = id)

@item_blueprint.route("/store/<id>/update", methods = ['POST'])
def sell(id):
    adventurer = adventurer_repo.select(request.form['adventurer_id'] )
    selling_item = item_repo.select(id)
    inventory = Inventory(adventurer, selling_item)
    invo_repo.save(inventory)
    
    return redirect("/store/" + adventurer.id)