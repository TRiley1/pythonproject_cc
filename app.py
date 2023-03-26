from flask import Flask, render_template

from controllers.item_controller import item_blueprint
# from controllers.inventory_controller import inventory_blueprint
# from controllers.adventurer_controller import adventurer_blueprint

app = Flask(__name__)

app.register_blueprint(item_blueprint)
# app.register_blueprint(inventory_blueprint)
# app.register_blueprint(adventurer_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()