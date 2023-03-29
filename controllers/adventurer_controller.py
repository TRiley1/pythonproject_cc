from flask import Blueprint, Flask, redirect, render_template, request
from models.adventurer import Adventurer
import pdb
import repositories.adventurer_repo as adventurer_repo

adventurer_blueprint = Blueprint("adventurer", __name__)

@adventurer_blueprint.route('/adventurer/new')
def adventurer():
    return render_template('/adventurers/new.html')

@adventurer_blueprint.route('/adventurer/new', methods = ['POST'])
def new_adventurer():
    name = request.form['name']
    wallet = request.form['wallet']
    adventurer = Adventurer(name,wallet)
    adventurer_repo.save(adventurer)
    return redirect('/')

@adventurer_blueprint.route('/adventurer/<user_id>/edit')
def edit_adventurer(user_id):
    adventurer = adventurer_repo.select(user_id)
    return render_template('adventurers/edit.html', user_id = user_id, adventurer= adventurer)


@adventurer_blueprint.route('/adventurer/<user_id>/delete', methods = ['POST'])
def delete_adventurer(user_id):
    adventurer_repo.delete(user_id)
    return redirect('/')

@adventurer_blueprint.route('/adventurer/<user_id>/edit', methods = ['POST'])
def update_adventurer(user_id):
    name = request.form['name']
    wallet = request.form['wallet']
    adventurer = Adventurer(name,wallet,user_id)
    adventurer_repo.adventurer_update(adventurer)
    return redirect('/')

@adventurer_blueprint.route('/adventurer/<user_id>/deposit')
def deposit_adventurer(user_id):
    return render_template('adventurers/deposit.html')