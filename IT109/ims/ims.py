from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
data_file = "inventory.json"

# Initialize inventory file
if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        json.dump([], f)

def load_inventory():
    with open(data_file, "r") as f:
        return json.load(f)

def save_inventory(inventory):
    with open(data_file, "w") as f:
        json.dump(inventory, f, indent=4)

@app.route("/")
def index():
    inventory = load_inventory()
    return render_template("index.html", inventory=inventory)

@app.route("/add_item", methods=["POST"])
def add_item():
    inventory = load_inventory()
    item = {
        "id": len(inventory) + 1,
        "name": request.form["name"],
        "price": float(request.form["price"]),
        "quantity": int(request.form["quantity"])
    }
    inventory.append(item)
    save_inventory(inventory)
    return redirect(url_for("index"))

@app.route("/update_item/<int:item_id>", methods=["POST"])
def update_item(item_id):
    inventory = load_inventory()
    for item in inventory:
        if item["id"] == item_id:
            item["name"] = request.form["name"]
            item["price"] = float(request.form["price"])
            item["quantity"] = int(request.form["quantity"])
            break
    save_inventory(inventory)
    return redirect(url_for("index"))

@app.route("/delete_item/<int:item_id>")
def delete_item(item_id):
    inventory = load_inventory()
    inventory = [item for item in inventory if item["id"] != item_id]
    save_inventory(inventory)
    return redirect(url_for("index"))

@app.route("/api/inventory", methods=["GET"])
def api_inventory():
    return jsonify(load_inventory())

if __name__ == "__main__":
    app.run(debug=True, port=5000)
