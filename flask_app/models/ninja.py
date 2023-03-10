from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:

    def __init__(self, ninja_data):
        self.id = ninja_data['id']
        self.first_name = ninja_data['first_name']
        self.last_name = ninja_data['last_name']
        self.age = ninja_data['age']
        self.created_at = ninja_data['created_at']
        self.updated_at = ninja_data['updated_at']
        self.dojo = None

    @classmethod
    def display_ninjas(cls):
        query = "SELECT * FROM ninjas JOIN dojos on dojos.id = ninjas.dojo_id;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        print(results)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ( %(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojo_name)s );"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def display_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, updated_at = NOW() WHERE id=%(id)s"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    # @classmethod
    # def display_ninjas(cls):
    #     query = "SELECT * FROM ninjas JOIN dojos on dojos.id = ninjas.dojo_id;"
    #     results = connectToMySQL('dojos_and_ninjas').query_db(query)
    #     print("results", results)
    #     list = []
    #     for e in results:
    #         n = cls(e)
    #         n.dojo = Dojo(
    #             {
    #             "id" : e["dojos.id"],
    #             "name" : e["name"],
    #             "created_at" : e["dojos.created_at"],
    #             "updated_at" : e["dojos.updated_at"]
    #         })
    #         list.append(n)
    #     return list