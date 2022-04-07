# controller.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.cars import Car
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
bcrypt = Bcrypt(app)






@app.route('/new')
def add():
    return render_template('new.html')

@app.route('/add_car',methods=['post'])
def add_car():
    data = {
        'price': request.form['price'],
        'model': request.form['model'],
        'make': request.form['make'],
        'year': request.form['year'],
        'description': request.form['description'],
        'users_id': session['id']

    }
    is_valid = True
    if len(request.form['price']) < 1:
        flash("thats a bit low don't you think?", "car")
        is_valid = False

    if len(request.form['model']) < 1:
        flash("Heavy on Performance but too light on the name", "car")
        is_valid = False

    if len(request.form['make']) < 1:
        flash("every car is made by someone, so who made this?", "car")
        is_valid = False

    if request.form['year'] < str(1850):
        flash("Dont think they had cars in that year", "car")
        is_valid = False

    if request.form['year'] > str(2023):
        flash("Wow we're not at that model year yet", "car")
        is_valid = False

    if len(request.form['description']) < 1:
        flash("C'mon now a good description will sell itself", "car")
        is_valid = False

    if not is_valid:
        return redirect('/new')

    Car.add_car(data)

    return redirect('/dashboard')



@app.route('/edit/<int:id>')
def edit(id):
    carId = {
        'id': id
    }

    car = Car.get_one(carId)

    return render_template('update.html', car = car)


@app.route('/update_car',methods=['post'])
def update_car():
    data = {
        'id': request.form['id'],
        'price': request.form['price'],
        'model': request.form['model'],
        'make': request.form['make'],
        'year': request.form['year'],
        'description': request.form['description']
    }

    is_valid = True
    if len(request.form['price']) < 1:
        flash("thats a bit low don't you think?", "car")
        is_valid = False

    if len(request.form['model']) < 1:
        flash("Heavy on Performance but too light on the name", "car")
        is_valid = False

    if len(request.form['make']) < 1:
        flash("every car is made by someone, so who made this?", "car")
        is_valid = False

    if request.form['year'] < str(1850):
        flash("Dont think they had cars in that year", "car")
        is_valid = False

    if request.form['year'] > str(2023):
        flash("Wow we're not at that model year yet", "car")
        is_valid = False

    if len(request.form['description']) < 1:
        flash("C'mon now a good description will sell itself", "car")
        is_valid = False

    if not is_valid:
        carid = data['id']
        return redirect(f'/edit/{carid}')



    
    Car.update_car(data)

    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete_car(id):
    carId = {
        'id': id
    }

    Car.delete_car(carId)

    return redirect('/dashboard')


# @app.route('/show/<int:id>/<int:userid>')
# def show_car(id, userid):
#     carId = {
#         'id': id
#     }
#     Userid = {
#         'id': userid
#     }

#     user = User.get_one(Userid)
#     car = Car.get_one(carId)
#     return render_template('show.html', car = car, user=user)


@app.route('/show/<int:id>')
def show_car(id):
    carId = {
        'id': id
    }
    car = Car.get_one_cars(carId)

    # car = Car.get_one(carId)
    return render_template('show.html', car = car[0])