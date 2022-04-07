from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB                                #<-- links to the name of the currrent database to easily change all models to use a new database at same time
class Ninja:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(MyCustomDB).query_db(query)                                #<-- MyCustomDB is the name I chose as the variable that ties all 
    # Create an empty list to append our instances of users
        my_dojos = []                                                                       #<-- can be any name for variable
    # Iterate over the db results and create instances of users with cls.
        for row in results:                                                                 #<-- loops over the individual dictionaries from the database query
            my_dojos.append( cls(row) )                                                     #<-- appends them to the list variable
        print('from the get all method')
        return my_dojos                                                                     #<-- returns the list of dictionaries 


    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name, age , created_at , updated_at, dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() , %(dojo_id)s );"
        return connectToMySQL(MyCustomDB).query_db( query, data )                           #dojo_id is foreign key in database tables





    # @classmethod
    # def delete_user(cls, data):                                     #<-- data passed in from the route is an dictionary containing key: value pairings that can be used in queries
    #     print("delete is running")
    #     query = "DELETE FROM users WHERE id = %(id)s"               #<-- SQL injection and sanitization, %(some value)s takes the value from the key in the data passed in
    #     return connectToMySQL(MyCustomDB).query_db( query, data )

    # @classmethod
    # def edit(cls, data):
    #     query = 'UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s , updated_at = NOW() WHERE id = %(id)s'
    #     return connectToMySQL(MyCustomDB).query_db( query, data )


    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(id)s"
    #     results = connectToMySQL(MyCustomDB).query_db(query, data)
    #     return cls(results[0])                                          #<-- returns the result of the query at the 1st index position in the list which is the dictionary of row 1