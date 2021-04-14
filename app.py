import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, templating, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import gridfs
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/recipes")
def get_recipe():
    recipies = list(mongo.db.recipies.find())
    return render_template("recipes.html", recipies=recipies)

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
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "myProfile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/myProfile/<username>", methods=["GET", "POST"])
def myProfile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("myProfile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/new_recipes", methods=["GET", "POST"])
def new_recipes():
    if request.method == "POST":
        vegan = "on" if request.form.get("vegan") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "short_describe": request.form.get("short_describe"),
            "ingredients": request.form.get("ingredients"),
            "step_1_of_preparation": request.form.get("step_1_of_preparation"),
            "step_2": request.form.get("step_2"),
            "step_3": request.form.get("step_3"),
            "vegan": vegan,
            "created_by": session["user"],
            "recipe_url": request.form.get("recipe_name")
        }
        mongo.db.recipies.insert_one(recipe)
        flash("Recipe Added")
        return redirect(url_for("new_recipes"))
    return render_template("new_recipes.html", page_title="Add a Recipe")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        vegan = "on" if request.form.get("vegan") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "short_describe": request.form.get("short_describe"),
            "ingredients": request.form.get("ingredients"),
            "step_1_of_preparation": request.form.get("step_1_of_preparation"),
            "step_2": request.form.get("step_2"),
            "step_3": request.form.get("step_3"),
            "vegan": vegan,
            "created_by": session["user"],
            "recipe_url": request.form.get("recipe_name")
        }
        mongo.db.recipies.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Updated")

    recipe = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipies.remove({"_id": ObjectId(recipe_id)})
    flash("Successfully Deleted")
    return redirect(url_for("get_recipe"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


