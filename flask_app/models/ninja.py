from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data["dojo_id"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo= None 
        

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        ninja_object_list = []
        if len(results) == 0:
            return []
        else:
            for this_ninja_dictionary in results:
                ninja_object_list.append(cls(this_ninja_dictionary))
        return ninja_object_list

    @classmethod
    def create_ninja(cls, data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        # comes back as the new row id
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_one_ninja(cls, data):
        query = """
            SELECT * FROM ninjas WHERE ninjas.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            new_ninja_object = cls(results[0])
        return new_ninja_object

    @classmethod
    def delete_one_ninja(cls, data):
        query = """
            DELETE FROM ninjas WHERE ninjas.id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update_ninja(cls, data):
        query = """
        UPDATE ninjas SET first_name = %(first_name)s,
                        last_name =%(last_name)s,
                        age = %(age)s,
                        dojo_id = %(dojo_id)s 
                        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
