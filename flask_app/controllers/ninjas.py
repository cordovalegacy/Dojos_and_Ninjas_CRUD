from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/show_ninja_list')
def show_ninja_list():
    ninjas = Ninja.display_ninjas()
    print(ninjas)
    return render_template('show_ninja.html', ninja_list = ninjas, all_dojos = Dojo.display_dojos())

@app.route('/add_ninjas_page')
def add_ninjas_page():
    return render_template('ninja.html', all_dojos = Dojo.display_dojos())

@app.route('/add_ninja', methods = ['POST'])
def add_ninja():
    data = {
        'fname': request.form['fname'],
        'lname' : request.form['lname'],
        'age': request.form['age'],
        'doj': request.form['dojo_id']
    }
    Ninja.add_ninja(data)
    return redirect('/show_ninja_list')

@app.route('/edit_ninja/<int:id>')
def edit_ninja(id):
    data={
        'id':id
    }
    return render_template('edit_ninja.html', one_ninja = Ninja.display_one_ninja(data))

@app.route('/update_ninja', methods = ['POST'])
def update_ninja():
    Ninja.update_ninja(request.form)
    return redirect('/show_ninja_list')

@app.route('/delete_ninja/<int:id>')
def delete_ninja(id):
    data={
        'id':id
    }
    Ninja.delete_ninja(data)
    return redirect('/show_ninja_list')