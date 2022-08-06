
class Specific_Product():
    """This is the class that stores the url, website (amazon, target, OR walmart) and the price that is returned from the scraper. ONE WEBSITE LINK per specific product instance. Each product can have up to three specific product instances."""

    def __init__(self, website, url, price):
        self.website = website
        self.url = url
        self.price = price

    def __repr__(self):
        return f'\nProduct Page\n  ' \
               f'Website: {self.website}\n  ' \
               f'Current Price: ${self.price}\n  ' \
               f'URL: {self.url}'

    def __str__(self):
        return f'\nProduct Page\n  ' \
               f'Website: {self.website}\n  ' \
               f'Current Price: ${self.price}\n  ' \
               f'URL: {self.url}'
