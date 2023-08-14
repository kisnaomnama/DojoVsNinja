from flask import app, render_template, session, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja


@app.route('/')
def root_route():
    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    all_dojo_objects = dojo.Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos = all_dojo_objects)

@app.route("/dojos/create", methods = ["POST"])
def add_dojo():
    form_result ={
        "name": request.form["name"]
    }
    print(form_result)
    dojo.Dojo.create_dojo(form_result) 
    return redirect("/dojos")

@app.route('/dojos/<int:id>')
def ninjas_of_dojo(id):
    data = {
        "id":id
    }
    dojo_object = dojo.Dojo.get_one_dojo_with_ninjas(data)
    return render_template("view_ninjas_of_dojo.html", dojo_object= dojo_object)

@app.route("/dojos/<int:dojo_id>/delete/<int:ninja_id>")
def delete_ninja(dojo_id, ninja_id):
    data = {
        "id":ninja_id
    }
    dojo_id = dojo_id
    print("The Dojo id: ", dojo_id)
    print("The Ninja id: ", ninja_id)
    dojo.Dojo.delete_one_ninja(data)
    return redirect(f"/dojos/{dojo_id}")


@app.route("/dojos/enterdate", methods = ["POST"])
def add_date():
    print(request.form)
    form_result ={
        "rdate": request.form["rdate"]
    }
    print(form_result)
    dojo.Dojo.create_date(form_result) 
    return redirect("/dojos")
    