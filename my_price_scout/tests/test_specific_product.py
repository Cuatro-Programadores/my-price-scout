import pytest

from files.specific_product import Specific_Product

def test_exists():
    assert Specific_Product

def test_sp_website():
    website = "amazon"
    url = "www.amazon.com"
    price = 5
    amazon_link = Specific_Product(website, url, price)
    expected = "amazon" 
    actual = amazon_link.website 
    assert actual == expected

def test_sp_website_not():
    website = "amazon"
    url = "www.amazon.com"
    price = 5
    amazon_link = Specific_Product(website, url, price) 
    assert amazon_link.website != "walmart"

def test_add_url():
    website = "amazon"
    url = "www.amazon.com"
    price = "priceless"
    amazon_link = Specific_Product(website, url, price) 
    assert amazon_link.url == "www.amazon.com"

def test_add_url_not():
    website = "amazon"
    url = "www.amazon.com"
    price = "priceless"
    amazon_link = Specific_Product(website, url, price) 
    assert amazon_link.url == "amazon"

def test_add_price():
    website = "amazon"
    url = "www.amazon.com"
    price = "priceless"
    amazon_link = Specific_Product(website, url, price) 
    assert amazon_link.price == 5

def test_price_type():
    website = "amazon"
    url = "www.amazon.com"
    price = "priceless"
    amazon_link = Specific_Product(website, url, price) 
    assert type(amazon_link.price) == str