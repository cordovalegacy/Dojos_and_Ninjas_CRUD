from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, dojo_data):
        self.id = dojo_data['id']
        self.name = dojo_data['name']
        self.created_at = dojo_data['created_at']
        self.updated_at = dojo_data['updated_at']

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

    @classmethod
    def show_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])
