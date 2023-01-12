from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    dojos = Dojo.display_dojos()
    print(dojos)
    return render_template('dojo.html', all_dojos = dojos)

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data = {
        'name': request.form['dojo_name']
    }
    Dojo.save(data)
    return redirect('/')