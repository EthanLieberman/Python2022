# controller.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.cars import Car
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)



# for the index route and anything else typed that doesnt already exist
@app.route('/')
@app.route('/<none>')
def index(none=None):
    if 'id' in session:
        return redirect('/dashboard')

    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # validates true or false based on data in the request form
    if not User.validate_register(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things

    # packages all data from the request form and the password after it is hashed
    hashword = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": hashword
    }

    #saves the packaged data
    User.save(data)
    #sets session user name from data gathered when registering and redirects the logged in user to the dashboard
    user_in_db = User.get_by_email(data)
    
    session['name'] = user_in_db.first_name
    session['id'] = user_in_db.id
    # session['name'] = request.form['first_name']
    return redirect('/dashboard')



@app.route('/login',methods=['post'])
def login():

    data = {
        'email': request.form['email']
    }

    # gets the dictionary of the user from the login form by their email
    user_in_db = User.get_by_email(data)

    # if there is nothing in the dictionary, that email was not found
    if not user_in_db:
        flash("Invalid email/password",'login')
        return redirect('/')

    # if the password in the database at the users email doesnt match the entered password on the form, validation is false
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid email/password", 'login')
        return redirect('/')

    
    # stores the logged in users name in session
    session['name'] = user_in_db.first_name
    # stores the logged in users id in session
    session['id'] = user_in_db.id

    return redirect('/dashboard')



@app.route('/dashboard')
def dashboard():
    # if nothing is in session go back to login page
    if not session:
        return redirect('/')


    cars = Car.get_all_cars()

    currentuser = {
        'id': session['id']
    }
    user = User.get_one(currentuser)
    # if there is data in session, continue and pass it to dashboard to use
    return render_template('dashboard.html', user = user, cars=cars)


@app.route('/logout')
def logout():
    #clears the user from session and returns to the login page
    session.clear()
    return render_template('index.html')