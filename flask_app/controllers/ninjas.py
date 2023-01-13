from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja

@app.route('/show_ninja_list')
def show_ninja_list():
    ninjas = Ninja.display_ninjas()
    print(ninjas)
    return render_template('show_ninja.html', ninja_list = ninjas)

@app.route('/add_ninjas_page')
def add_ninjas_page():
    return render_template('ninja.html')

@app.route('/add_ninja', methods = ['POST'])
def add_ninja():
    data = {
        'first_name': request.form['fname'],
        'last_name' : request.form['lname'],
        'age': request.form['age']
    }
    Ninja.add_ninja(data)
    return redirect('/show_ninja_list')

@app.route('/edit_ninja/<int:id>')
def edit_ninja(id):
    return redirect('/show_ninja_list')

@app.route('/delete_ninja/<int:id>')
def delete_ninja(id):
    return redirect('/show_ninja_list')