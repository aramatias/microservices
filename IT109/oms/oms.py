from flask import Flask, render_template, request, jsonify
import json
import os
from queue import Queue

app = Flask(__name__)
order_queue = Queue()
inventory_file = "../ims/inventory.json"

def load_inventory():
    with open(inventory_file, "r") as f:
        return json.load(f)

def save_inventory(inventory):
    with open(inventory_file, "w") as f:
        json.dump(inventory, f, indent=4)

@app.route("/")
def order_form():
    inventory = load_inventory()
    return render_template("order_form.html", inventory=inventory)

@app.route("/place_order", methods=["POST"])
def place_order():
    inventory = load_inventory()
    item_id = int(request.form["item_id"])
    quantity = int(request.form["quantity"])
    for item in inventory:
        if item["id"] == item_id:
            if item["quantity"] >= quantity:
                item["quantity"] -= quantity
                order_queue.put({"item": item["name"], "quantity": quantity})
                save_inventory(inventory)
                return jsonify({"message": "Order placed successfully!"})
            else:
                return jsonify({"message": "Sold out! Not enough stock."}), 400
    return jsonify({"message": "Item not found!"}), 404


@app.route("/view_orders")
def view_orders():
    orders = list(order_queue.queue)
    return render_template("inventory_view.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
