
class Product:
    def __init__(self, product_name, target_price,
                 specific_product_list=None, is_product_being_tracked=True):
        self.product_name = product_name
        self.is_product_being_tracked = is_product_being_tracked
        self.specific_product_list = specific_product_list if specific_product_list else []
        self.target_price = target_price

    def __repr__(self):
        return f"\n\033[1;32mProduct Information \033[0;37m\n  " \
               f"Product Name: {self.product_name}\n  " \
               f"Target Price: ${self.target_price}\n  " \
               f"Notifications: {self.is_product_being_tracked}\n  " \
               f"{self.specific_product_list}"

    def __str__(self):
        return f"\nProduct Information\n  " \
               f"Product Name: {self.product_name}\n  " \
               f"Target Price: ${self.target_price}\n  " \
               f"Notifications: {self.is_product_being_tracked}\n  " \
               f"{self.specific_product_list}"

    def add_new_specific_product(self, specific_product):
        """
        Arguments:
            self: specific instance of the Product class
            specific_product: object consisting of product_name, websites, urls,
            and actual_price.
        """
        print("SPECIFIC PRODUCT LIST", self.specific_product_list)
        print("SPECIFIC PRODUCT", specific_product)
        self.specific_product_list.append(specific_product)

    def remove_old_specific_product(self, website, url):
        """
        Arguments:
             website: The website to remove the link for.  The values may be
             'amazon,' 'target,' or 'walmart'.
        """
        for specific_product in self.specific_product_list:
            if url == specific_product.url:
                self.specific_product_list.remove(specific_product)

                return f"{specific_product} link from {website} removed."

        return f"Specific product on {website} not found."

    def change_url_for_specific_product(self, specific_product, website, url):
        """This function allows a user to change the link to a product
        Arguments:
            self: specific instance of the Product class
            specific_product: object consisting of product_name, websites, urls,
            and actual_price.
            website: The website to remove the link for.  The values may be
            'amazon,' 'target,' or 'walmart'.
        Return:
            string: Confirmation that the method worked."""
        self.remove_old_specific_product(website, url)
        self.add_new_specific_product(specific_product)

        return f"Specific product link has been updated."

    def toggle_notifications(self):
        """
        Changes the boolean for the product being tracked on the user class.
        """
        self.is_product_being_tracked = not self.is_product_being_tracked
