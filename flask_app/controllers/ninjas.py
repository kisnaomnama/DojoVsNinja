from flask import app, render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models import dojo, ninja


@app.route('/ninjas')
def ninjas():
    all_dojos = dojo.Dojo.get_all_dojos()
    return render_template("ninjas.html", all_dojos=all_dojos)


@app.route("/ninjas/create", methods=["POST"])
def add_ninja():
    form_result = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    ninja.Ninja.create_ninja(form_result)
    # print(new_id)
    return redirect("/ninjas")


@app.route('/ninjas/<int:id>')
def view_ninja(id):
    data = {
        "id": id
    }
    dojo_object = dojo.Dojo.get_one_dojo_with_ninjas(data)
    return render_template("view_ninjas_of_dojo.html", dojo_object=dojo_object)


@app.route("/ninjas/<int:ninja_id>/edit")
def edit_ninja(ninja_id):
    data = {
        "id": ninja_id
    }
    this_ninja = ninja.Ninja.get_one_ninja(data)
    return render_template("ninja_edit.html", this_ninja=this_ninja)


@app.route("/ninjas/<int:id>/update", methods=["POST"])
def update_ninja(id):
    print(request.form)
    form_result = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"],
        "id":id
    }
    dojo_id = request.form["dojo_id"]
    ninja.Ninja.update_ninja(form_result)
    return redirect(f"/dojos/{dojo_id}")


