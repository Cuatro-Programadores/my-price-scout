
class User:
    def __init__(self, email, phone_number, cell_carrier, watchlist=None):
        self.email = email
        self.phone_number = phone_number
        self.cell_carrier = cell_carrier
        self.watchlist = watchlist if watchlist else []

    def __repr__(self):

        return f"\nUser Information \n  " \
               f"Email: {self.email}\n  " \
               f"Phone Number: {self.phone_number}\n  " \
               f"Cell Carrier: {self.cell_carrier}\n  " \
               f"{self.watchlist}"

    def __str__(self):

        return f"\n\033[1;32mUser Information \033[0;37m\n  " \
               f"Email: {self.email}\n  " \
               f"Phone Number: {self.phone_number}\n  " \
               f"Cell Carrier: {self.cell_carrier}\n  " \
               f"{self.watchlist}"

    def get_item(self, item_name):
        """

        Args:
            item_name ():

        Returns:
            item
        """
        for item in self.watchlist:
            if item.product_name == item_name:

                return item

    def add_item(self, item):
        """

        Args:
            item ():

        Returns:
            None
        """
        self.watchlist.append(item)

    def remove_item(self, item_name):
        """

        Args:
            item_name ():

        Returns:
            None
        """

        for item in self.watchlist:
            if item.product_name == item_name:
                self.watchlist.remove(item)

    def replace_item(self, old_item_name, item):
        """

        Args:
            old_item_name ():
            item ():

        Returns:
            None
        """
        new_watchlist = []

        for old_item in self.watchlist:
            if old_item.product_name == old_item_name:
                new_watchlist.append(item)
            else:
                new_watchlist.append(old_item)

        self.watchlist = new_watchlist

    def get_watchlist(self):
        """

        Returns:
            watchlist
        """

        return self.watchlist
