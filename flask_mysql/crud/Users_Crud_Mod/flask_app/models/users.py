xitfrom flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB
class User:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(MyCustomDB).query_db(query)
    # Create an empty list to append our instances of users
        my_users = []
    # Iterate over the db results and create instances of users with cls.
        for row in results:
            my_users.append( cls(row) )
        print('from the get all method')
        return my_users


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name, email ,created_at , updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def delete_user(cls, data):
        print("delete is running")
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(MyCustomDB).query_db( query, data )

    @classmethod
    def edit(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s , updated_at = NOW() WHERE id = %(id)s'
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        return cls(results[0])
