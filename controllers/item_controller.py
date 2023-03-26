from flask import Blueprint, Flask, redirect, render_template, request

from models.item import Item
import repositories.item_repo as item_repo

item_blueprint = Blueprint("item", __name__)

@item_blueprint.route("/items")
def items():
    items = item_repo.select_all()
    return render_template("index.html", items = items)