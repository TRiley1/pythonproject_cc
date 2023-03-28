from flask import Blueprint, Flask, redirect, render_template, request
from models.adventurer import Adventurer
import repositories.adventurer_repo as adventurer_repo

adventurer_blueprint = Blueprint("adventurer", __name__)

@adventurer_blueprint.route('/adventurer/<user_id>/delete', methods = ['POST'])
def delete_adventurer(user_id):
    adventurer_repo.delete(user_id)
    return redirect('/')

@adventurer_blueprint.route('/adventurer/<user_id>/update', methods = ['POST'])
def update_adventurer(user_id):
    name = request.form['name']
    adventurer = Adventurer(name,user_id)
    adventurer_repo.adventurer_update(adventurer)
    return redirect('/')