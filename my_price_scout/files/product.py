
class Product:
    def __init__(self, product_name, target_price,
                 specific_product_list=None, is_product_being_tracked=True):
        self.product_name = product_name
        self.is_product_being_tracked = is_product_being_tracked
        self.specific_product_list = specific_product_list if specific_product_list else []
        self.target_price = target_price

    def __repr__(self):
        return f"\nProduct Information\n  " \
               f"Product Name: {self.product_name}\n  " \
               f"Target Price: ${self.target_price}\n  " \
               f"Notifications: {self.is_product_being_tracked}\n  " \
               f"Specific Product: {self.specific_product_list}"

    def __str__(self):
        return f"\nProduct Information\n  " \
               f"Product Name: {self.product_name}\n  " \
               f"Target Price: ${self.target_price}\n  " \
               f"Notifications: {self.is_product_being_tracked}\n  " \
               f"Specific Product: {self.specific_product_list}"

    def add_new_specific_product(self, specific_product):
        """
        Arguments:
            self: specific instance of the Product class
            specific_product: object consisting of product_name, websites, urls,
            and actual_price.
        Return:
            confirmation_string: confirms the specific_product was added.
        """
        print("SPECIFIC PRODUCT LIST", self.specific_product_list)
        print("SPECIFIC PRODUCT", specific_product)
        self.specific_product_list.append(specific_product)

    def remove_old_specific_product(self, website, url):
        """
        Arguments:
             website: The website to remove the link for.  The values may be
             'amazon,' 'target,' or 'walmart'.
        Return:
            string: Confirmation that the method worked.
        """
        for specific_product in self.specific_product_list:
            if url == specific_product.url:
                self.specific_product_list.remove(specific_product)

                return f"{specific_product} link from {website} removed."

        return f"Specific product on {website} not found."


    def change_url_for_specific_product(self, specific_product, website,
                                        specific_product2):

        """This function allows a user to change the link to a product
        Arguments:
            self: specific instance of the Product class
            specific_product: object consisting of product_name, websites, urls,
            and actual_price.
            website: The website to remove the link for.  The values may be
            'amazon,' 'target,' or 'walmart'.
        Return:
            string: Confirmation that the method worked."""

        self.remove_old_specific_product(website, specific_product.url)
        print("Specific Product", specific_product2)
        self.add_new_specific_product(specific_product2)


        return f"Specific product link has been updated."

    def toggle_notifications(self):
        self.is_product_being_tracked = not self.is_product_being_tracked

    # def product_url_count(self):
    #     """
    #     Arguments:
    #         product_name: product to get the url count for.
    #     Return:
    #         int: total number of urls between 1 and 3 for a given product.
    #     """
    #     return len(self.specific_product_list)
    # This function is in case we need additional count functionality at some point to add or remove specific product links
