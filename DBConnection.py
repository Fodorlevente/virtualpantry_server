import pymongo
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId



class DBConnection():

    def __init__(self, cluster_name: str, db_name: str, user_name: str, password: str):
        self.cluster_name = cluster_name
        self.db_name = db_name
        self.user_name = user_name
        self.password = password
        
        self.cluster = MongoClient(f"mongodb+srv://{self.user_name}:{self.password}@cluster0-zt5cg.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.cluster[self.cluster_name]
        self.collection = self.db[self.db_name]

        self.__food_types = [
            "sustainable food",
            "spices",
            "drinks",
            "perishable food"
        ]
    

    def insert_single_item_to_db(self, name: str, exp_date: datetime, type: str, location: str = "Unknown"):
        self.collection.insert_one({
            "name": name,
            "exp_date": exp_date,
            "location": location,
            "type": type,
            "date_of_shopping": datetime.utcnow()
        })

    def delete_single_item_from_db(self,ids):
        self.collection.delete_one({"_id": ObjectId(ids)})

    def delete_all_items_from_db(self):
        self.collection.delete_many({})

    def find_all_items(self):
        return self.collection.find()

    def find_all_items_2(self):
        foods = self.collection.find()
        return [item for item in foods]

    def find_items_by_name(self,name: str):
        return self.collection.find({"name": name})

    def print_results(self,results):
        for result in results:
            print(result)

    def get_count_of_all_items(self):
        return self.collection.count()

    def get_count_of_items_by_name(self, name: str):
        return self.collection.find({"name": name}).count()

    def get_count_of_items_by_type(self, type: str):
        return self.collection.find({"type": type}).count()

    def counts_per_type(self):
        tyepes_and_counts = []
        for i in self.__food_types:
            tyepes_and_counts.append(self.create_type_and_piece_object(i, self.get_count_of_items_by_type(i)))
        return tyepes_and_counts

    def create_type_and_piece_object(self, _name: str, _piece):
        return {
            'name' :  _name,
            'piece' : _piece
        }

# my_conn = DBConnection("virtualspiceapp", "spice", "SpiceAdmin","SpiceAdmin123")
# my_conn.print_results(my_conn.find_all_items())

# print(my_conn.get_count_of_all_items())