import os
import sys
import re


class IOUtils:
    """This is the class that validates all of the user inputs"""

    def __init__(self) -> None:
        pass

    def quit_app(self):
        """
        Clears the entire screen and then quits the entire program.
        """
        os.system('clear')
        print(f"Thanks checking in, see you next time!")
        sys.exit(1)

    def check(self, value):
        """

        Args:
            value

        Returns:
            value or none
        """
        print(f"{value} right? Type y or n")
        verify = input("> ").lower()
        if verify == "q":
            self.quit_app()
        if verify == "y":
            return value
        if verify == "n":
            print("Please enter again")
            return None

    def capture_email(self):
        """Capture email: inputs - email, outputs - validated email """

        print("Enter your email to get started")

        email = input("> ").lower()

        if email == "q":
            self.quit_app()

        regex_email = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

        if re.fullmatch(regex_email, email):
            email = self.check(email)
            if email is None:
                self.capture_email()
            else:
                return email

        else:
            print("Invalid Email\nPlease try to input your email again")
            email = None
            self.capture_email()

    def capture_number(self):
        """Capture number: inputs - 10 digit phone number, outputs - validated number """

        print("Please enter your 10 digit phone number")

        number = input("> ")

        if number == "q":
            self.quit_app()

        regex_number = r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'

        if re.fullmatch(regex_number, number):
            number = self.check(number)
            if number is None:
                self.capture_number()
            else:
                return number

        else:
            print("Invalid number\nPlease try to input your number again")
            number = None
            self.capture_number()

    def capture_carrier(self):
        """Capture cell phone carrier: inputs - carrier, outputs - String"""

        print("Please choose from the following phone carriers.\nATT, BOOST, CRICKET, GOOGLEFI, METROPCS, MINT, SIMPLEMOBILE, SPRINT, TMOBILE, VERIZON, VIRGIN, XFINITY\nIf your provider is not listed, we do not support your carrier at this time. Please press q to exit")

        phone_plan = input("> ").upper()

        if phone_plan == "Q":
            self.quit_app()

        list_of_carriers = ["Q", "ATT", "BOOST", "CRICKET", "GOOGLEFI", "METROPCS",
                            "MINT", "SIMPLEMOBILE", "SPRINT", "TMOBILE", "VERIZON", "VIRGIN", "XFINITY"]

        if phone_plan in list_of_carriers:

            phone_plan = self.check(phone_plan)

            if phone_plan is None:
                self.capture_carrier()

            if phone_plan == "TMOBILE":
                print(
                    "Please note it can take several hours for TMOBILE messages to be received by the user!")
                return phone_plan

            else:
                return phone_plan
        else:
            print("Invalid phone_plan\nPlease try to input your phone_plan again")
            phone_plan = None
            self.capture_carrier()

    def capture_product_name(self):
        """Capture product name to pass to the Item class"""

        print("What is the name of the product?")

        name = input("> ").lower()

        if name == "q":
            self.quit_app()

        name = self.check(name)
        if name is None:
            self.capture_product_name()
        else:
            return name

    def capture_website(self):
        """Asks the user whether they would input a link to Amazon, Target, or Walmart. Also collects the link and returns it together with the site name in lowercase."""

        print("Is the product URL from Amazon, Target or Walmart?")

        # This makes the store name Title case like Amazon, Target, or Walmart instead of being fully lowercase.
        store = input("> ").title()

        if store == "q":
            self.quit_app()

        list_of_sites = ["Amazon", "Target", "Walmart"]

        if store in list_of_sites:
            URL = self.capture_url(store)
            return store, URL

        else:
            print("Invalid store\nPlease try to input your store again")
            store = None
            self.capture_website()

    def capture_url(self, store_name):
        """Captures a URL for specific_product"""

        print(f"Please input the URL for the item from {store_name}")

        url = input("> ")

        if url == "q":
            self.quit_app()

        if store_name.lower() in url:
            url = self.check(url)
            if url is None:
                self.capture_url(store_name)
            else:
                return url

        else:
            print("Invalid link\nPlease try to input your URL again")
            url = None
            self.capture_url(store_name)

    def capture_strike_price(self):
        """Captures the price at which the person would like a notification on the product price."""

        print("At what price do you want to be notified about your product? Please enter a positive whole number like \"99\" for how many dollars you would be willing to pay ")

        price = input("> ")

        if price == "q":
            self.quit_app()

        regex_number = r'^\s*[0-9]{1,10}\s*$'

        if re.fullmatch(regex_number, price):
            price = self.check(price)
            if price is None:
                self.capture_strike_price()
            else:
                # print(price)
                return int(price)

        else:
            print("Invalid price\nPlease try to input your price again")
            price = None
            self.capture_strike_price()

    def capture_notification(self, override=None):
        """This is the boolean that activates the price tracking notifications. The optional input override is for the tracker to be able to turn off the notification when it sends out an alert"""

        notification = None

        if override == True:
            notification = True

        if override == False:
            notification = False

        if override == None:

            print("Would you like to receive text notifications when the product price drops below your ideal price? Please type y or n")

            notification = input("> ").lower()

            if notification == "q":
                self.quit_app()

            elif notification == "y":
                notification = True

            elif notification == "n":
                notification = False

            else:
                print("Invalid input\nPlease input y or n")
                notification = None
                self.capture_notification()
        return notification

    def capture_menu_nav(self):
        """Displays the main menu and takes in the input for where in the menu the user would like to navigate to."""

        menu = """
Main Menu

To navigate through the menu:
Press the number next to what you would like to do 

[1] View Product Prices
[2] Input A New Product
[3] Remove A Product
[4] Add Product Links for Tracked Products
[5] Remove Product Links for Tracked Products
[6] Change Product Links for Tracked Products
[7] Toggle Product Notifications

Press q to quit at any time
        """

        print(menu)

        # This makes the nav name Title case like Amazon, Target, or Walmart
        # instead of being fully lowercase.
        nav = input("> ")

        if nav == "q":
            self.quit_app()

        regex_menu_number = r'^([1-7])$'

        if re.fullmatch(regex_menu_number, nav):
            return int(nav)

        else:
            print("Invalid input\nPlease try to input your menu option number again")
            nav = None
            self.capture_menu_nav()

    def how_many_links(self):
        """User can add up to three links"""

        print("You can add up to three product links to track for this product - one each for Amazon, Walmart, or Target. How many links would you like to add at this time? Please enter an integer- 1, 2, or 3")

        count = input("> ")

        if count == "q":
            self.quit_app()

        regex_menu_number = r'^([1-3])$'

        if re.fullmatch(regex_menu_number, count):
            return int(count)

        else:
            print(
                "Invalid input\nthe amount of links you would like to track as an integer between 1-3")
            count = None
            self.how_many_links()
