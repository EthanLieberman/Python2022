# controller.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    dojos = Dojo.get_all()                                      #<-- assigns the function of the class to the variable
    return render_template('index.html', my_dojos=dojos)        #<-- assigns the variable to a variable we can use on the rendered page


@app.route('/create_ninja')
def create_ninja_page():
    dojos = Dojo.get_all()
    return render_template('add_new_ninja.html', my_dojos=dojos)


@app.route('/create_ninja_submit', methods=['post'])
def submit_ninja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.save(data)
    return redirect('/')


@app.route('/dojos_list/<int:id>')
def dojos_members(id):
    data = {
        'id': id
    }

    dojo = Dojo.get_dojos_with_ninjas(data)
    return render_template('members.html', dojo=dojo)



@app.route('/show_ninjas/<int:id>')
def show_ninjas(id):
    data = {
        "id" :id
    }
    return render_template('ninjas.html', dojo_name=Dojo.get_one(data))


@app.route('/new_dojo',methods=['post'])
def create_dojo():
    data = {
        'name': request.form['new_dojo_name']
    }
    Dojo.create(data)
    return redirect('/')


@app.route('/delete_dojo/<int:id>')
def delete_dojo(id):
    data = {
        'id': id
    }
    Dojo.deleteDojo(data)
    return redirect('/')

# @app.route('/create', methods=['post'])
# def save():
#     data = {                                            #<-- assigns the data collected in the form on the page to a dictionary object 
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email']
#     }

#     Dojo.save(data)                                     #<-- runs the function on the class, passing in the data we just got from the form

#     return redirect('/')


# @app.route('/add')
# def add_new_user():
#     return render_template('add_new_user.html')


# @app.route('/delete/<int:id>')          #<-- takes the int value from the url
# def delete_user(id):                    #<-- passes the int value we captured from the url route
#     data = {"id": id}                   #<-- makes a dictionary of the key we want with the value of what we passed in
#     Dojo.delete_user(data)              #<-- runs the .classmethod passing in the data dictionary we just made
#     return redirect('/')


# @app.route('/edit_user/<int:id>', methods=['post'])     #<-- post from the html to the server
# def edit_existing_user(id):
#     data = {                                            #<-- passing in data from forms and url capture
#         "id" : id,
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email']
#     }

#     Dojo.edit(data)
#     return redirect('/')

# @app.route('/edit/<int:id>')
# def edit_user(id):
#     print('editing')
#     data = {'id':id}
#     return render_template('edit_user.html', dojo=Dojo.get_one(data))


# # @app.route('/show/<int:id>')
# # def show_user(id):
# #     data = {
# #         "id" :id
# #     }
# #     return render_template('show_user.html', single_user=User.get_one(data))