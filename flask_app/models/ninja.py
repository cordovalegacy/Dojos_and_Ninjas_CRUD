from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, ninja_data):
        self.id = ninja_data['id']
        self.first_name = ninja_data['first_name']
        self.last_name = ninja_data['last_name']
        self.age = ninja_data['age']
        self.created_at = ninja_data['created_at']
        self.updated_at = ninja_data['updated_at']

    @classmethod
    def display_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas