from flask import Blueprint, Flask, redirect, render_template, request
from models.item import Item
from models.adventurer import Adventurer
from models.inventory import Inventory
import pdb
import repositories.item_repo as item_repo
import repositories.inventory_repo as invo_repo
import repositories.adventurer_repo as adventurer_repo

inventory_blueprint = Blueprint("inventory", __name__)

@inventory_blueprint.route('/inventory')
def stock_record():
    results = invo_repo.select_all()
    return render_template("/inventory/store.html", inventory_list = results)

@inventory_blueprint.route('/inventory/<user_id>')
def inventory(user_id):
    results=invo_repo.select_adventurer_inventory(user_id)
    return render_template("/inventory/index.html", inventory = results)
