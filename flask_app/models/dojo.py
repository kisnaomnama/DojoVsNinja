# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from flask import flash

class Dojo:
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas_list = []  # will hold the ninjas

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        dojo_object_list = []
        if len(results) == 0:
            return []
        else:
            for this_dojo_dictionary in results:
                dojo_object_list.append(cls(this_dojo_dictionary))
        return dojo_object_list

    @classmethod
    def create_dojo(cls, data):
        query = """
            INSERT INTO dojos (name) VALUES (%(name)s);
        """
        # comes back as the new row id
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_one_dojo(cls, data):
        query = """
            SELECT * FROM dojos WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)

        if len(results) == 0:
            return None
        else:
            # result is a list so first index
            new_dojo_object = cls(results[0])
        return new_dojo_object

    @classmethod
    def get_one_dojo_with_ninjas(cls, data):
        query = """
            SELECT * FROM ninjas
            JOIN dojos
            ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)

        if len(results) == 0:
            return []
        else:
            new_dojo_object = cls(results[0])
            for each_row in results:
                print(each_row)
                
                new_ninja_dict = {
                    "id" : each_row['id'],
                    "first_name" : each_row['first_name'],
                    "last_name" :  each_row['last_name'],
                    "age" : each_row['age'],
                    "dojo_id": each_row["dojo_id"],
                    "created_at" : each_row['created_at'],
                    "updated_at" : each_row['updated_at'],
                }

                new_dojo_object.ninjas_list.append(ninja.Ninja(new_ninja_dict))
        return new_dojo_object

    @classmethod
    def delete_one_dojo(cls, data):
        query = """
            DELETE FROM dojos WHERE dojos.id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update_dojo(cls, data):
        query = """
        UPDATE dojos SET name = %(name)s,
                        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
    

    @classmethod
    def delete_one_ninja(cls, data):
        query = """
            DELETE FROM ninjas WHERE ninjas.id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def create_date(cls, data):
        query = """
            INSERT INTO date_tables (date) VALUES (%(rdate)s);
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_one_date(cls, data):
        query = """
            SELECT * FROM date_tables
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results