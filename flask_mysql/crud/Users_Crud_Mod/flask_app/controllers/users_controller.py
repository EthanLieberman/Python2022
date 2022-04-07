# controller.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users import User


@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', my_users=users)


@app.route('/create', methods=['post'])
def save():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.save(data)

    return redirect('/')


@app.route('/add')
def add_new_user():
    return render_template('add_new_user.html')


@app.route('/delete/<int:id>')
def delete_user(id):
    data = {"id": id}
    User.delete_user(data)
    return redirect('/')


@app.route('/edit_user/<int:id>', methods=['post'])
def edit_existing_user(id):
    data = {
        "id" : id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.edit(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit_user(id):
    print('editing')
    data = {'id':id}
    return render_template('edit_user.html', user=User.get_one(data))


@app.route('/show/<int:id>')
def show_user(id):
    data = {
        "id" :id
    }
    return render_template('show_user.html', single_user=User.get_one(data))