import os
from datetime import timedelta
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
# Set the permanent session lifetime
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)


mongo = PyMongo(app)


# landing page
@app.route("/")
def landing():
    if "user" in session:
        return redirect(url_for("get_to_do_items"))
    else:
        return render_template("landing.html")


# sign in
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                session.permanent = True
                return redirect(url_for("get_to_do_items", username=session["user"]))
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


# register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Complete!")
        return redirect(url_for("get_to_do_items", username=session["user"]))

    return render_template("register.html")


# sign out
@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signin"))


# display to-do list
@app.route("/get_to_do_items")
def get_to_do_items():
    sort_order = request.args.get("sort")
    sort_category = request.args.get("category")

    if "user" not in session:
        return redirect(url_for("signin"))

    username = session["user"]
    query = {"created_by": username}

    to_do_items = list(mongo.db.to_do_items.find(query))

    if sort_category:
        to_do_items.sort(key=lambda x: x["category_name"].lower())
    elif sort_order == "important":
        to_do_items.sort(key=lambda x: x.get("is_important", False), reverse=True)
    elif sort_order == "alpha":
        # Alphabetical sorting
        to_do_items.sort(key=lambda x: x["to_do_item"].lower())
    else:
        # Default sorting
        to_do_items.sort(key=lambda x: x["category_name"].lower())
    return render_template(
        "to_do_items.html", to_do_items=to_do_items, username=username
    )


# search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    username = session["user"] if "user" in session else None
    to_do_items = list(mongo.db.to_do_items.find({"$text": {"$search": query}}))

    if not to_do_items:
        flash("Sorry, there are no such items or categories:(")
        to_do_items = list(mongo.db.to_do_items.find({"created_by": username}))

    return render_template(
        "to_do_items.html", to_do_items=to_do_items, username=username
    )


# adding to the list
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
            "created_by": session["user"].lower(),
        }
        mongo.db.to_do_items.insert_one(new_item)
        flash("Added to the list!")
        return redirect(url_for("get_to_do_items"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_to_do_item.html", categories=categories)


# editing list item
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
            "created_by": session["user"].lower(),
        }

        mongo.db.to_do_items.update_one(
            {"_id": ObjectId(to_do_item_id)}, {"$set": submit}
        )
        flash("Updated!")
        return redirect(url_for("get_to_do_items"))

    to_do_item = mongo.db.to_do_items.find_one({"_id": ObjectId(to_do_item_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_to_do_item.html", to_do_item=to_do_item, categories=categories
    )


# mark an item as completed
@app.route("/toggle_cross_out/<item_id>")
def toggle_cross_out(item_id):
    to_do_item = mongo.db.to_do_items.find_one({"_id": ObjectId(item_id)})

    if not to_do_item:
        flash("Item not found", "error")
        return redirect(url_for("get_to_do_items"))

    new_state = not to_do_item.get("is_crossed_out", False)
    mongo.db.to_do_items.update_one(
        {"_id": ObjectId(item_id)}, {"$set": {"is_crossed_out": new_state}}
    )

    if new_state:
        flash("One less thing to worry about!")
    else:
        flash("That's fine, take your time:)")

    return redirect(url_for("get_to_do_items"))


# delete a list item
@app.route("/delete_to_do_item/<to_do_item_id>")
def delete_to_do_item(to_do_item_id):
    mongo.db.to_do_items.delete_one({"_id": ObjectId(to_do_item_id)})
    flash("Item Deleted!")
    return redirect(url_for("get_to_do_items"))


# delete all checked items
@app.route("/delete_checked_items")
def delete_checked_items():
    count_checked = mongo.db.to_do_items.count_documents({"is_crossed_out": True})

    if count_checked == 0:
        flash("You haven't checked any items!")
    else:
        mongo.db.to_do_items.delete_many({"is_crossed_out": True})
        flash("Done and dusted! You're a star!")

    return redirect(url_for("get_to_do_items"))


# display categories created by admin or a logged-in user
@app.route("/get_categories")
def get_categories():
    if "user" not in session:
        return redirect(url_for("signin"))

    username = session["user"].lower()
    sort_order = request.args.get("sort")

    # Query for categories created by the user or admin
    categories_query = {"$or": [{"created_by": username}, {"created_by": "admin"}]}

    categories = list(mongo.db.categories.find(categories_query))

    if sort_order == "alpha":
        # Alphabetical sorting
        categories.sort(key=lambda x: x["category_name"].lower())
    elif sort_order == "created_by":
        #  user's categories come first
        categories.sort(
            key=lambda x: (x["created_by"] != username, x["category_name"].lower())
        )

    else:
        # Default sort
        categories.sort(key=lambda x: x["category_name"].lower())

    return render_template("categories.html", categories=categories)


# add a category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "created_by": session["user"].lower(),
        }
        mongo.db.categories.insert_one(category)
        flash("Category Added!")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# edit a category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "created_by": session["user"].lower(),
        }

        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Updated!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete a category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# error pages
@app.errorhandler(404)
def page_not_found(e):

    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    print("500 error handler triggered")
    return render_template("500.html"), 500


@app.route("/trigger-500")
def trigger_500():
    raise Exception("This is a test exception to trigger a 500 error.")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
