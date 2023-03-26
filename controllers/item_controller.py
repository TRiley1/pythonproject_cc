from flask import Blueprint, Flask, redirect, render_template, request
from models.item import Item
from models.adventurer import Adventurer
from models.inventory import Inventory
import repositories.item_repo as item_repo
import repositories.inventory_repo as invo_repo
import repositories.adventurer_repo as adventurer_repo

item_blueprint = Blueprint("item", __name__)

@item_blueprint.route("/items")
def items():
    items = item_repo.select_all_stock()
    return render_template("store/index.html", items = items)

@item_blueprint.route("/items/<id>/delete", methods = ['POST'])
def sell(id):
    adventurer1 = Adventurer("The Green Giant")
    adventurer_repo.save(adventurer1)
    selling_item = item_repo.select(id)
    item_repo.save(selling_item)
    inventory = Inventory(adventurer1, selling_item)
    invo_repo.save(inventory)
    item_repo.delete(id)
    
    return redirect("/items")