# Project Framework
#   * get_or_create_user: inputs - email, phone, carrier, outputs - User instance
#     * helper methods: get_user, create_user, save_user
#     * save_user will parse the User instance into key values and save to Db
#       using Database Utils
#   * start: inputs - none, outputs - screen prompts or return information
#     * helpers: IO Utils, User, and Item
#   * menu: Routing the user through the options they have available. inputs - None outputs - function calls based on the users selections.(Different options for where they would like to go and some sort of back function)
#
# * remove_url: calls the remove_url method in Item
#     * inputs - website name (i.e., Amazon), outputs - confirmation
#       string
#     * if removing the only link, then prompt user for new link or to
#       remove item
#   * manage_user_items: logic for when a user has items to add, remove, or
#     edit items

# To Do :
# create a menu for the user with the options for the things they can change. Create methods that call the other class' functions that hold those methods
# Create the board that gives the other classes the info they need/build out the user with the products and build out the products with the specific products

# Need the team - Somewhere we need to add the sleep function that calls the scraper every 10 minutes. Not sure how that gets integrated with the serverless portion.
# View Tracked Products and View Products and Pricing have been combined into view product info since that would be returning all of the product objects. This only works if we move get summary to user
# Looks like there would need to be another edit product section to incorporate functions from temp_product and_name, add_target_price. These functions may not be necessary since we are passing this to the product to start with.


# To Do List
# Hitting enter from io utils - especially in input carrier.
# ioutils testing
# Toggle Notifications not saving in User
# Handle Error Message to User before breaking
# Product name not saving in user


import sys
from ioutils import IOUtils
from dbutils import DBUtils
from user import User
from product import Product
from specific_product import Specific_Product
from scraper import Scraper
from temptracker import Tracker

# The scraper function will return a string if the url is wrong or something but an integer if the scraper work - need to update ioutils


class App_Logic:
    def __init__(self) -> None:
        self.user_inputs = IOUtils()
        self.database = DBUtils()
        self.scraper = Scraper()
        self.tracker = Tracker()
        self.user = None
        self.user_data = {}
        self.product = None
        self.specific_product = None

    def start(self):
        """This method displays the original user welcome and introduces them to how to quit. THis is where the user interface lives and calls functions to handle the inputs and route the user."""

        print("Welcome to My Price Scout where you can track product pricing from Amazon, Walmart, and Target!\nPress q to quit at any time")

        self.get_or_create_new_user()

        self.manage_user_items_menu()

    def get_or_create_new_user(self):
        """Takes in the users email as an input and checks the database for the user. Routes to create a new user or return user information based on Database returned info."""

        email = self.user_inputs.capture_email()
        # print(email)

        if self.database.get_user(email) == None:
            self.create_user(email)
        else:
            self.get_user(email)

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
        """Parse the data from the users input and send it to the DBUtils as an object"""

        self.database.set_user(self.user)
        # Part of this is voided since we are parsing through the db utils function

    def get_user(self, email):
        """Parse the data from the database and make a new user object.
        The get_user function from the database sends back a user object fully put together."""
        # This is where we need to set up the retrieval for the user object - depends on how we input the user information

        if self.database.get_user(email) is None:
            return None

        else:
            print("Welcome back!")

            papaya = self.database.get_user(email)

            self.user = papaya

    def manage_user_items_menu(self):
        # See the example Sergii sent

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

        # There should be some sort of input in these cases for the user to go back without adjusting anything.

        # Adjust price etc should show the current value before asking the user to change things.

    def menu_view_product_info(self):
        print("View Product Info")
        self.get_user(self.user.email)
        print(self.user)
        # product_object_list = self.user.get_watchlist()

    def menu_input_new_product(self):
        """Creating a new Product Object"""
        print(
            "Input A New Product. All new items are automatically tracked for notifications")

        name = self.user_inputs.capture_product_name()
        strike_price = self.user_inputs.capture_strike_price()
        # notifications = self.user_inputs.capture_notification()
        watchlist = []

        number = self.user_inputs.how_many_links()
        # print(f"number={number}")

        for _ in range(number):
            # This just calls adds specific products to the watchlist based on how many the user says they would like to add.
            watchlist.append(self.add_specific_product())

        # self.product = Product(name, strike_price, notifications, watchlist)
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
        print("Remove A Product")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are removing a product")

        name = self.user_inputs.capture_product_name()

        self.user.remove_item(name)
        self.save_user()
        # Getting an error -  name 'product_name' is not defined. Error between fetching from user and product classes.

        print(f"{name} has been removed from tracking")

    def menu_add_product_links(self):
        print("Add Product Links")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are adding a link for a product")

        name = self.user_inputs.capture_product_name()

        self.product = self.user.get_item(name)

        self.specific_product = self.add_specific_product()

        # print (self.specific_product)

        self.product.add_new_specific_product(self.specific_product)

    def menu_remove_product_links(self):
        print("Remove Product Links")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are removing a link for a product")

        name = self.user_inputs.capture_product_name()

        print("Which website's link would you like to remove? Copy and paste the website and link that is currently being tracked from above.")
        website, url = self.user_inputs.capture_website()

        self.product = self.user.get_item(name)

        self.product.remove_old_specific_product(website, url)
        self.save_user()

    def change_product_links(self):
        print("Change a Product Link")

        print("Here is the list of products you currently have saved:")
        self.menu_view_product_info()
        print("You are changing a link for a product")

        name = self.user_inputs.capture_product_name()

        self.product = self.user.get_item(name)

        print("Which website's link would you like to remove? Copy and paste the website and link that is currently being tracked from above.")
        website, url = self.user_inputs.capture_website()

        self.specific_product = self.add_specific_product()

        self.product.change_url_for_specific_product(
            self.specific_product, website, url)
        self.save_user()

    def menu_toggle_product_notifications(self):
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


if __name__ == "__main__":
    try:
        new_app = App_Logic()
        new_app.start()

    except KeyboardInterrupt:
        new_app.keyboard_quit('You have pressed CTRL-C so Goodbye!')
