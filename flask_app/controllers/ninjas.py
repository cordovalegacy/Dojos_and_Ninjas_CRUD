from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja

@app.route('/show_ninja_list')
def show_ninja_list():
    ninjas = Ninja.display_ninjas()
    print(ninjas)
    return render_template('show_ninja.html', ninja_list = ninjas)