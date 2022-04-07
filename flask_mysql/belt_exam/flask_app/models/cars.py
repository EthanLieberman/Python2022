from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB
from flask import flash
from flask_app.models.user import User

class Car:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

        self.owner = []







    @classmethod
    def add_car(cls, data):
        query = "INSERT INTO cars ( price , model , make , year , description ,created_at , updated_at , users_id ) VALUES ( %(price)s , %(model)s , %(make)s , %(year)s , %(description)s , NOW() , NOW() , %(users_id)s );"
        return connectToMySQL(MyCustomDB).query_db( query, data )

    @classmethod
    def get_all_cars(cls):
        # query = "SELECT * FROM cars;"
        query = "SELECT * FROM cars JOIN users ON users.id = cars.users_id;"
        
        results = connectToMySQL(MyCustomDB).query_db( query)


        if results:
            all_cars = []
            for row in results:
                one_car = cls(row)
                user_data = {
                    **row,
                    'id': row['users_id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                one_car.owner = User(user_data)
                all_cars.append(one_car)
                return all_cars


        all_cars = []
        # Iterate over the db results and create instances of users with cls.
        for row in results:
            all_cars.append( cls(row) )
        return all_cars

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cars WHERE id = %(id)s"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        return cls(results[0])


    @classmethod
    def update_car(cls, data):
        query = "UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def delete_car(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s"
        return connectToMySQL(MyCustomDB).query_db( query, data )






    @classmethod
    def get_one_cars(cls, data):
        # query = "SELECT * FROM cars;"
        query = "SELECT * FROM cars JOIN users ON users.id = cars.users_id WHERE cars.id = %(id)s;"
        
        results = connectToMySQL(MyCustomDB).query_db( query, data)


        if results:
            all_cars = []
            for row in results:
                one_car = cls(row)
                user_data = {
                    **row,
                    'id': row['users_id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                one_car.owner = User(user_data)
                all_cars.append(one_car)
                return all_cars


        all_cars = []
        # Iterate over the db results and create instances of users with cls.
        for row in results:
            all_cars.append( cls(row) )
        return all_cars