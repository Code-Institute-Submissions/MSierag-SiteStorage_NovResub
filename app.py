import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/get_items")
def get_items():
    items = list(mongo.db.items.find())
    return render_template("items.html", items=items)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    items = list(mongo.db.items.find({"$text": {"$search": query}}))
    return render_template("items.html", items=items)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            }
        mongo.db.users.insert_one(register)

        # Put the new user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("You are now registered")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Make sure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user's session cookie
    flash("You've successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        item = {
            "location_name": request.form.get("location_name"),
            "item_name": request.form.get("item_name"),
            "item_description": request.form.get("item_description"),
            "date_received": request.form.get("date_received"),
            "created_by": session["user"]
        }
        mongo.db.items.insert_one(item)
        flash("Item added successfully")
        return redirect(url_for("get_items"))

    locations = mongo.db.locations.find().sort("location_name", 1)
    return render_template("add_item.html", locations=locations)


@app.route("/edit_item/<item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    if request.method == "POST":
        submit = {
            "location_name": request.form.get("location_name"),
            "item_name": request.form.get("item_name"),
            "item_description": request.form.get("item_description"),
            "date_received": request.form.get("date_received"),
            "created_by": session["user"]
        }
        mongo.db.items.update({"_id": ObjectId(item_id)}, submit)
        flash("Item updated successfully")
        return redirect(url_for("get_items"))

    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    locations = mongo.db.locations.find().sort("location_name", 1)
    return render_template("edit_item.html", item=item, locations=locations)


@app.route("/delete_item/<item_id>")
def delete_item(item_id):
    mongo.db.item.remove({"_id": ObjectId(item_id)})
    flash("Item deleted")
    return redirect(url_for("get_items"))


@app.route("/get_locations")
def get_locations():
    locations = list(mongo.db.locations.find().sort("location_name", 1))
    return render_template("locations.html", locations=locations)


@app.route("/add_locaton", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        location = {
            "location_name": request.form.get("location_name")
        }
        mongo.db.locations.insert_one(location)
        flash("New storage location added")
        return redirect(url_for("get_locations"))

    return render_template("add_location.html")


@app.route("/edit_location/<location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    if request.method == "POST":
        submit = {
            "location_name": request.form.get("location_name")
        }
        mongo.db.locations.update({"_id": ObjectId(location_id)}, submit)
        flash("Location updated successfully")
        return redirect(url_for("get_locations"))

    location = mongo.db.locations.find_one({"_id": ObjectId(location_id)})
    return render_template("edit_location.html", location=location)


@app.route("/delete_location/<location_id>")
def delete_location(location_id):
    mongo.db.locations.remove({"_id": ObjectId(location_id)})
    flash("Location deleted successfully")
    return redirect(url_for("get_locations"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
