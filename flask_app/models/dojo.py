from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:

    def __init__(self, dojo_data):
        self.id = dojo_data['id']
        self.name = dojo_data['name']
        self.created_at = dojo_data['created_at']
        self.updated_at = dojo_data['updated_at']
        self.ninjas = []

    @classmethod
    def display_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    # @classmethod
    # def show_dojo(cls, data):
    #     query = "SELECT * FROM ninjas JOIN dojos on dojos.id = ninjas.dojo_id WHERE dojos.id= %(id)s"
    #     result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
    #     print(result)
    #     return cls(result[0])

    @classmethod
    def show_dojo(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for table_row in results:
            dojo.ninjas.append( Ninja({
                'id': table_row['ninjas.id'],
                'first_name': table_row['first_name'],
                'last_name': table_row['last_name'],
                'age': table_row['age'],
                'created_at': table_row['ninjas.created_at'],
                'updated_at': table_row['ninjas.updated_at']
            }) )
        return dojo
