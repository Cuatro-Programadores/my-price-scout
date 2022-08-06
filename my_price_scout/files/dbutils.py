import dotenv
import os
from pymongo import MongoClient
from user import User
from product import Product
from specific_product import Specific_Product


dotenv.load_dotenv(dotenv.find_dotenv())


password = os.environ.get("MONGO_PASSWORD")


class DBUtils:
    def __init__(self):
        self.connection = MongoClient(
             f"mongodb+srv://mypricescout"
             f":{password}@my-price-scout-users.yugh3.mongodb.net"
             f"/?retryWrites=true&w=majority")

    def set_user(self, user):
        """
        Arguments:
            user object

        Returns:
            None
        """
        found_user = self.connection.user_data.user_data.find_one(
            {"email": f"{user.email}"})
        if found_user:
            self.connection.user_data.user_data.delete_one(
                {"email": f"{user.email}"})

        user_document = {
            "email": f"{user.email}",
            "phone_number": user.phone_number,
            "cell_carrier": f"{user.cell_carrier}",
            "watchlist": [{"name": product.product_name,
                           "is_product_being_tracked":
                               product.is_product_being_tracked,
                           "specific_product_list": [{"website": f"{specific_product.website}", "url": f"{specific_product.url}", "price": f"{specific_product.price}"} for specific_product in product.specific_product_list], "target_price": f"{product.target_price}"} for product in user.watchlist]
        }

        self.connection.user_data.user_data.insert_one(user_document)

    def get_user(self, user_name):
        """
        Arguments:
            user_name

        Returns:
            user object
        """
        found_user = self.connection.user_data.user_data.find_one(
            {"email": f"{user_name}"})
        if found_user:
            parsed_user = User(found_user["email"], found_user["phone_number"], found_user["cell_carrier"], [Product(item["name"], item["target_price"], [
                Specific_Product(link["website"], link["url"], link["price"]) for link in item["specific_product_list"]], item["is_product_being_tracked"]) for item in found_user["watchlist"]])

            return parsed_user

        else:

            return None


if __name__ == "__main__":

    pass
