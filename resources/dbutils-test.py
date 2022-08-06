import os
import dotenv
from pymongo import MongoClient
import pprint
from bson.json_util import dumps, loads

dotenv.load_dotenv(dotenv.find_dotenv())
# config = dotenv_values(".env")

password = os.environ.get("MONGO_PASSWORD")
connection_string = f"mongodb+srv://mypricescout:{password}@my-price-scout-users.yugh3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
dbs = client.list_database_names()
user_db = client.user_data


printer = pprint.PrettyPrinter()


# class DBUtils():
#     def __init__(self):
#         self.connection = MongoClient(
#             f"mongodb+srv://mypricescout:{password}@my-price-scout-users.yugh3.mongodb.net/?retryWrites=true&w=majority")

#     def set_user(self, user):

#         user_document = {
#             "email": f"{user.email}",
#             "phone_number": user.phone_number,
#             "cell_carrier": f"{user.cell_carrier}",
#             "watchlist": [{"name": product.name, "is_being_tracked": product.is_being_tracked, "specific_product_list": [{"website": f"{specific_product.website}", "url": f"{specific_product.url}", "actual_price": f"{specific_product.actual_price}"} for specific_product in product.specific_product_list], "target_price": f"{product.target_price}"} for product in user.watchlist]
#         }

#         self.connection.user_data.user_data.insert_one(user_document)

#     def get_user(self, user_name):
#         found_user = self.connection.user_data.user_data.find_one(
#             {"email": f"{user_name}"})
#         parsed_user = User(found_user["email"], found_user["phone_number"], found_user["cell_carrier"], [Item(item["name"], item["target_price"], [
#             Link(link["website"], link["url"], link["actual_price"]) for link in item["specific_product_list"]]) for item in found_user["watchlist"]])

#         return parsed_user


class User:
    def __init__(self, email, phone_number, cell_carrier, watchlist=None):
        self.email = email
        self.phone_number = phone_number
        self.cell_carrier = cell_carrier
        self.watchlist = watchlist if watchlist else []

    def __repr__(self):

        return f"email: {self.email}, phone number: {self.phone_number}, cell carrier: {self.cell_carrier}, items: {self.watchlist}"

    def __str__(self):

        return f"email: {self.email}, phone number: {self.phone_number}, cell carrier: {self.cell_carrier}, items: {self.watchlist}"


class Item():
    def __init__(self, name, target_price, specific_product_list=[]):
        self.name = name
        self.is_being_tracked = True
        self.specific_product_list = specific_product_list
        self.target_price = target_price

    def __repr__(self):

        return f"name: {self.name}, is_being_tracked: {self.is_being_tracked}, specific_product_list: {self.specific_product_list}, target_price: {self.target_price}"

    def __str__(self):

        return f"name: {self.name}, is_being_tracked: {self.is_being_tracked}, specific_product_list: {self.specific_product_list}, target_price: {self.target_price}"


class Link():
    def __init__(self, website, url, price):
        self.website = website
        self.url = url
        self.price = price

    def __repr__(self):

        return f"website: {self.website}, url: {self.url}, price: {self.actual_price}"

    def __str__(self):

        return f"website: {self.website}, url: {self.url}, price: {self.actual_price}"


link1 = Link("amazon", "111.com", 50)
link2 = Link("walmart", "222.com", 100)
link3 = Link("target", "333.com", 150)
link4 = Link("bestbuy", "444.com", 200)

item1 = Item("tv", 444, [link1, link2])
item2 = Item("toaster", 000, [link3, link4])

new_user = User("555@gmail.com", 2062231333, "Walmart", [item1, item2])


def set_user(user):

    collection = user_db.user_data
    found_user = collection.find_one(
        {"email": f"{user.email}"})
    if found_user:
        collection.delete_one(
            {"email": f"{user.email}"})

    user_document = {
        "email": f"{user.email}",
        "phone_number": user.phone_number,
        "cell_carrier": f"{user.cell_carrier}",
        "watchlist": [{"name": product.name, "is_being_tracked": product.is_being_tracked, "specific_product_list": [{"website": f"{specific_product.website}", "url": f"{specific_product.url}", "actual_price": f"{specific_product.actual_price}"} for specific_product in product.specific_product_list], "target_price": f"{product.target_price}"} for product in user.watchlist]
    }

    collection.insert_one(user_document)


def get_user(user_name):
    found_user = user_db.user_data.find_one({"email": f"{user_name}"})
    parsed_user = User(found_user["email"], found_user["phone_number"], found_user["cell_carrier"], [Item(item["name"], item["target_price"], [
                       Link(link["website"], link["url"], link["price"]) for link in item["specific_product_list"]]) for item in found_user["watchlist"]])

    return parsed_user


def get_all_users():
    collection = user_db.user_data
    retrieved_users_cursor = collection.find({})
    user_list_cursor = list(retrieved_users_cursor)
    json_user_list = dumps(user_list_cursor)
    user_list = loads(json_user_list)

    return user_list


def update_all_users():
    user_list = get_all_users()

    for user in user_list:
        for product in user["watchlist"]:
            # target_price = product["target_price"]
            for specific_product in product["specific_product_list"]:
                # if specific_product["website"] == "Amazon":
                #     specific_product["price"] = scraper.scrape_amazon()
                # if specific_product["website"] == "Target":
                #     specific_product["price"] = scraper.scrape_target()
                # if specific_product["website"] == "Walmart":
                #     specific_product["price"] = scraper.scrape_walmart()
                specific_product["price"] = 888

    return user_list


def save_updated_users():
    collection = user_db.user_data
    updated_user_list = update_all_users()
    collection.delete_many({})
    # json_user_list = dumps(updated_user_list)
    collection.insert_many(updated_user_list)
    # return json_user_list


if __name__ == "__main__":
    # dbutils = DBUtils()
    # # printer = pprint.PrettyPrinter()
    # dbutils.set_user(new_user)
    # set_user(new_user)
    # print(get_user("444@gmail.com"))

    # user_list_json = get_all_users()
    # user_list_json[-1]["watchlist"][0]["specific_product_list"][0]["actual_price"] = 100
    # print(user_list_json[-1]["watchlist"][0]
    #       ["specific_product_list"][0]["actual_price"])
    # set_user(new_user)

    # updated_users = update_all_users()
    # print(updated_users)

    save_updated_users()

    # found_user = user_db.user_data.find_one({"email": "222@gmail.com"})
    # printer.pprint(get_user("222@gmail.com"))
    # print(dbutils.get_user("444@gmail.com"))
    # print(found_user)

    # dbutils = DBUtils()
    # link1 = Specific_Product("amazon", "111.com", 50)
    # link2 = Specific_Product("walmart", "222.com", 100)
    # link3 = Specific_Product("target", "333.com", 150)
    # link4 = Specific_Product("bestbuy", "444.com", 200)

    # item1 = Product("tv", 444, [link1, link2])
    # item2 = Product("toaster", 22, [link3, link4])

    # new_user = User("7777777@gmail.com", 2062231333, "ATT", [item1, item2])
    # dbutils.set_user(new_user)

    # print(dbutils.get_user("7777777@gmail.com"))
    pass
