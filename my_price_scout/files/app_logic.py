import os
import sys
from ioutils import IOUtils
from dbutils import DBUtils
from user import User
from product import Product
from specific_product import Specific_Product
from scraper import Scraper


class AppLogic:
    def __init__(self) -> None:
        self.user_inputs = IOUtils()
        self.database = DBUtils()
        self.scraper = Scraper()
        self.user = None
        self.user_data = {}
        self.product = None
        self.specific_product = None

    def start(self):
        """This method displays the original user welcome and introduces 
         them to how to quit. THis is where the user interface lives and 
          calls functions to handle the inputs and route the user."""
        self.title()
        print("Welcome to My Price Scout where you can track product pricing "
              "from Amazon, Walmart, and Target!\nPress q to quit at any time") 

        self.get_or_create_new_user()

        self.manage_user_items_menu()

    def get_or_create_new_user(self):
        """Takes in the users email as an input and checks the database for 
        the user. Routes to create a new user or return user information 
        based on Database returned info. """

        email = self.user_inputs.capture_email()

        if self.database.get_user(email) is None:
            self.create_user(email)
        else:
            self.get_user(email)

            print("Welcome back!")
            # print(self.user)

    def create_user(self, email):
        print("Welcome new user! Let's get you set up with an account!")

        number = self.user_inputs.capture_number()
        carrier = self.user_inputs.capture_carrier()

        current_user = User(email, number, carrier)
        self.user = current_user
        print(self.user)

        print("Let's track your first product")

        self.menu_input_new_product()

        self.save_user()

    def save_user(self):
        """Parse the data from the users input and send it to the DBUtils as 
        an object """

        self.database.set_user(self.user)

    def get_user(self, email):
        """Parse the data from the database and make a new user object. The 
        get_user function from the database sends back a user object fully 
        put together. """

        if self.database.get_user(email) is None:
            return None

        else:
            papaya = self.database.get_user(email)

            self.user = papaya

    def manage_user_items_menu(self):
        """
        Menu selection for the user to direct the code to each of the
         program functions.
        """
        steering = self.user_inputs.capture_menu_nav()

        if steering == 1:
            self.menu_view_product_info()
            self.manage_user_items_menu()

        if steering == 2:
            self.menu_input_new_product()
            self.manage_user_items_menu()

        if steering == 3:
            self.menu_remove_product()
            self.manage_user_items_menu()

        if steering == 4:
            self.menu_add_product_links()
            self.manage_user_items_menu()

        if steering == 5:
            self.menu_remove_product_links()
            self.manage_user_items_menu()

        if steering == 6:
            self.change_product_links()
            self.manage_user_items_menu()

        if steering == 7:
            self.menu_toggle_product_notifications()
            self.manage_user_items_menu()

    def menu_view_product_info(self):
        """
        Displays table of users current items and information.
        """
        print("\n\033[1;32mView Product Info \033[0;37m")
        self.get_user(self.user.email)
        print(self.user)

    def menu_input_new_product(self):
        """Creating a new Product Object"""
        print("Input A New Product. All new items are automatically tracked "
              "for notifications")

        name = self.user_inputs.capture_product_name()
        strike_price = self.user_inputs.capture_strike_price()
        watchlist = []

        number = self.user_inputs.how_many_links()

        for _ in range(number):
            """
            This just calls adds specific products to the watchlist based on 
            how many the user says they would like to add.
            """
            watchlist.append(self.add_specific_product())

        new_product = Product(name, strike_price, watchlist)

        self.user.add_item(new_product)

        self.save_user()

        print("New Product Added!")

    def add_specific_product(self):
        """Creating a new Specific Product Object"""

        print("Let's Collect some information about your product")
        website, url = self.user_inputs.capture_website()

        if website == "Amazon":
            current_price = self.scraper.scrape_amazon(url)

        if website == "Target":
            current_price = self.scraper.scrape_target(url)

        if website == "Walmart":
            current_price = self.scraper.scrape_walmart(url)

        self.specific_product = Specific_Product(website, url, current_price)

        print("Product Information has been added!")

        return self.specific_product

    def menu_remove_product(self):
        """
        Remove a product of the user's choosing.
        """
        print("Remove A Product")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are removing a product")

        name = self.user_inputs.capture_product_name()

        self.user.remove_item(name)
        self.save_user()

        print(f"{name} has been removed from tracking")

    def menu_add_product_links(self):
        """
        Add additional links to existing product of user's choice.
        """
        print("Add Product Links")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are adding a link for a product")

        name = self.user_inputs.capture_product_name()

        self.product = self.user.get_item(name)

        self.specific_product = self.add_specific_product()

        self.product.add_new_specific_product(self.specific_product)
        self.save_user()

    def menu_remove_product_links(self):
        """
        Remove link from a product of the user's choosing.
        """
        print("Remove Product Links")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are removing a link for a product")

        name = self.user_inputs.capture_product_name()

        print("Which website's link would you like to remove? Copy and paste "
              "the website and link that is currently being tracked from "
              "above.")
        website, url = self.user_inputs.capture_website()

        self.product = self.user.get_item(name)

        self.product.remove_old_specific_product(website, url)
        self.save_user()

    def change_product_links(self):
        """
        Guides a user through removing an existing link for a product and
        adding a new link for the same product.
        """
        print("Change a Product Link")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are changing a link for a product")

        name = self.user_inputs.capture_product_name()

        self.product = self.user.get_item(name)

        print("Which website's link would you like to remove? Copy and paste "
              "the website and link that is currently being tracked from "
              "above.")
        website, url = self.user_inputs.capture_website()

        self.specific_product = self.add_specific_product()

        self.product.change_url_for_specific_product(
            self.specific_product, website, url)
        self.save_user()

    def menu_toggle_product_notifications(self):
        """
        Allows the user to change whether to receive a notification or not
        for a given product.
        """
        print("Toggle Product Notifications")
        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are changing the notification tracking for a product")

        item_name = self.user_inputs.capture_product_name()

        selected_item = self.user.get_item(item_name)
        selected_item.toggle_notifications()
        self.save_user()

        print(self.user)

        print("This change has been captured")

    def keyboard_quit(self, message):
        sys.exit(message)

    def title(self):
        message = """\033[1;32m
8b    d8 Yb  dP     88""Yb 88""Yb 88  dP""b8 888888     .dP"Y8  dP""b8  dP"Yb  88   88 888888 d8b 
88b  d88  YbdP      88__dP 88__dP 88 dP   `" 88__       `Ybo." dP   `" dP   Yb 88   88   88   Y8P 
88YbdP88   8P       88'''  88"Yb  88 Yb      88""       o.`Y8b Yb      Yb   dP Y8   8P   88   `"' 
88 YY 88  dP        88     88  Yb 88  YboodP 888888     8bodP'  YboodP  YbodP  `YbodP'   88   (8) 
\033[0;37m"""
        print(message)


if __name__ == "__main__":
    try:
        new_app = AppLogic()
        os.system('clear')
        new_app.start()

    except KeyboardInterrupt:
        os.system('clear')
        new_app.keyboard_quit('You have pressed CTRL-C so Goodbye!')
