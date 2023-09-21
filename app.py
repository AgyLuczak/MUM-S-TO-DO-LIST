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
@app.route("/get_to_do_items")
def get_to_do_items():
    to_do_items = list(mongo.db.to_do_items.find())
    return render_template("to_do_items.html", to_do_items=to_do_items)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
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

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Complete!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hi, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            elif len(request.form.get("username")) < 3:
                flash("must be at least 3 characters")
                return redirect(url_for("signin"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signin"))

 
@app.route("/add_to_do_item", methods=["GET", "POST"])
def add_to_do_item():
    if request.method == "POST":
        is_important = "on" if request.form.get("is_important") else "off"
        new_item = {
            "category_name": request.form.get("category_name"),
            "to_do_item": request.form.get("to_do_item"),
            "item_details": request.form.get("item_details"),
            "is_important": is_important,
            "due_date": request.form.get("due_date"),
        
        }
        mongo.db.to_do_items.insert_one(new_item)
        flash("Added to the list!")
        return redirect(url_for("get_to_do_items"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_to_do_item.html", categories=categories)


@app.route("/edit_to_do_item/<to_do_item_id>", methods=["GET", "POST"])
def edit_to_do_item(to_do_item_id):
    if request.method == "POST":
        is_important = "on" if request.form.get("is_important") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "to_do_item": request.form.get("to_do_item"),
            "item_details": request.form.get("item_details"),
            "is_important": is_important,
            "due_date": request.form.get("due_date"),
        
        }
        mongo.db.to_do_items.update({"_id": ObjectId(to_do_item_id)}, submit)
        flash("Updated!")
       
    to_do_item = mongo.db.to_do_items.find_one({"_id": ObjectId(to_do_item_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_to_do_item.html", to_do_item=to_do_item, categories=categories)


@app.route("/delete_to_do_item/<to_do_item_id>")
def delete_to_do_item(to_do_item_id):
    mongo.db.to_do_items.remove({"_id": ObjectId(to_do_item_id)})
    flash("Deleted!")
    return redirect(url_for("get_to_do_items"))

@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)