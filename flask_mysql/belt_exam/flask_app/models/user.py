from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB
from flask import flash
import re

# from flask_app.models.cars import Car

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')

class User:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @staticmethod
    def validate_register(data):
        is_valid = True

        # searches database for the email entered, if it finds it the email is taken
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        if len(results) >= 1:
            flash('email already in use', 'register')
            is_valid = False

        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']): 
            flash('Invalid email address!', 'register')
            is_valid = False

        # checks the length of first and last names
        if len(data['first_name']) < 3 or len(data['last_name']) < 3:
            flash('name too short', 'register')
            is_valid = False

        # checks that names only contain valid characters
        if not NAME_REGEX.match(data['first_name']) or not NAME_REGEX.match(data['last_name']):
            flash('Name must be only letters', 'register')
            is_valid = False

        # checks the length of passwords
        if len(data['password']) < 8:
            flash('password must be longer than 8 characters', 'register')
            is_valid = False

        # checks that the password was entered correctly both times
        if not data['password'] == data['confirm_password']:
            flash('passwords must match', 'register')
            is_valid = False


        return is_valid


    @staticmethod
    def validate_login(data):
        is_valid = True

        # checks all users in database, if either their email or passwords dont exist or match validation is false
        for row in User.get_all():
            if not data['email'] in row.email or not data['password'] in row.password:
                flash("email/password incorrect", 'login')
                is_valid = False

        return is_valid



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name, email , password , created_at , updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );"
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(MyCustomDB).query_db(query,data)
        # returns a list of disctionaries containing users with matching emails, if that list has anything in it, an email already exists and the validation is false, if it unique, return the information
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_with_owners(cls):
        query = "SELECT * FROM users JOIN cars ON users.id = cars.users_id;"
        
        results = connectToMySQL(MyCustomDB).query_db( query)

        all_cars = []
        # Iterate over the db results and create instances of users with cls.
        for row in results:
            all_cars.append( cls(row) )
        return all_cars