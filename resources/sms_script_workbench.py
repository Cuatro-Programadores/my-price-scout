import smtplib
import ssl
import dotenv
from dotenv import dotenv_values

dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv_values(".env")

carrier_gates_dict = {
    "ATT": "@txt.att.net",
    "BOOST": "@sms.myboostmobile.com",
    "CRICKET": "@sms.cricketwireless.net",
    "GOOGLEFI": "@msg.fi.google.com",
    "METROPCS": "@mymetropcs.com",
    "MINT": "@mailmymobile.net",
    "SIMPLEMOBILE": "@smtext.com",
    "SPRINT": "@messaging.sprintpcs.com",
    "TMOBILE": "@tmomail.net",
    "VERIZON": "@vtext.com",
    "VIRGIN": "@vmobl.com",
    "XFINITY": "@vtext.com"
}
port = 465  # For SSL
password = config['EMAIL_PASSWORD']
smtp_server = "smtp.gmail.com"
sender_email = config['SENDER_EMAIL']  # Enter your address
receiver_email = "4252298247@tmomail.net"  # Enter receiver address

message = """\
Hello there """

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

# https://realpython.com/python-send-email/


class App:
    def __init__(self, users=[]):
        self.users = users

    def __repr__(self):

        return f"{self.users}"

    def get_users(self):
        return self.users

    def add_user(self, user):
        self.users.append(user)


class User:
    def __init__(self, name, phone_number, items=[]):
        self.name = name
        self.phone_number = phone_number
        self.items = items

    def __repr__(self):

        return f"name:{self.name}, cell: {self.phone_number}, items: {self.items}"

    def add_item(self, item):
        self.items.append(item)


class Item:
    def __init__(self, name, target_price, active=True, links=[]):
        self.name = name
        self.active = active
        self.links = links
        self.target_price = target_price

    def __repr__(self) -> str:

        return f"name: {self.name}, active: {self.active}, links: {self.links}, target price: {self.target_price}"

    def add_link(self, link):
        self.links.append(link)


if __name__ == '__main__':
    new_app = App()
    bob = User("bob", 2043322)
    john = User("john", 331122)
    new_app.add_user(bob)
    new_app.add_user(john)
    tv = Item("tv", 200)
    tv.add_link(
        "https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level")
    tv.add_link(
        "https://www.reddit.com/r/LightPhone/comments/f6vpd9/list_of_email_to_sms_gateways/")
    tv.add_link(
        "https://realpython.com/python-send-email/")
    john.add_item(tv)
    print(new_app)
