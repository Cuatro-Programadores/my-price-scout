# This file will test the Product class.
import pytest


from files.product import Product
from files.specific_product import Specific_Product


def test_exists():
    assert Product


def test_add_new_specific_product(specific_product):
    product = Product("ups", 180)
    print(product)

    product.add_new_specific_product(specific_product)

    expected = [
        "ups",
        180,
        ["amazon",
        "https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dp/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1"]
    ]

    assert product.product_name == expected[0]
    assert product.target_price == expected[1]
    assert product.specific_product_list[0].website == 'amazon'
    assert product.specific_product_list[0].url == "https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dpu/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1"
    assert product.specific_product_list[0].price == 10

def test_remove_old_specific_product(specific_product):
    product = Product("ups", 180)

    product.remove_old_specific_product("amazon", "https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dp/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1")
    print(product)

    expected = [
        "ups",
        180,
        ["amazon",
        "`https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dp/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1`"]
    ]

    print(product.specific_product_list)

    assert product.product_name == expected[0]
    assert product.target_price == expected[1]
    assert product.specific_product_list == []


#@pytest.mark.skip
def test_change_url_for_specific_product(specific_product, website,
                                         specific_product2):
    product = Product("ups", 180)
    print(product)

    product.add_new_specific_product(specific_product)

    product.change_url_for_specific_product(specific_product, website, specific_product2)

    expected = [
        "ups",
        180,
        ["amazon",
        "https://www.amazon.com/APC-Battery-Protector-Back-UPS-BE600M1/dp/B01FWAZEIU/ref=sr_1_3?keywords=ups+battery+backup&qid=1659656709&sprefix=ups+bat%2Caps%2C193&sr=8-3"]
    ]

    assert product.product_name == expected[0]
    assert product.target_price == expected[1]
    assert product.specific_product_list[0].website == 'amazon'
    assert product.specific_product_list[0].url == "https://www.amazon.com/APC-Battery-Protector-Back-UPS-BE600M1/dp/B01FWAZEIU/ref=sr_1_3?keywords=ups+battery+backup&qid=1659656709&sprefix=ups+bat%2Caps%2C193&sr=8-3"
    assert product.specific_product_list[0].price == 10


@pytest.fixture
def product(specific_product):
    product_name = "ups"
    target_price = 180
    listspecificproducts = []
    listspecificproducts.append(specific_product)

    return Product(product_name, target_price, listspecificproducts)


@pytest.fixture
def specific_product():
    website = "amazon"
    url = "https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dpu" \
          "/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1"
    price = 10

    return Specific_Product(website, url, price)


@pytest.fixture
def specific_product2():
    website = "amazon"
    url = "https://www.amazon.com/APC-Battery-Protector-Back-UPS-BE600M1/dp/B01FWAZEIU/ref=sr_1_3?keywords=ups+battery+backup&qid=1659656709&sprefix=ups+bat%2Caps%2C193&sr=8-3"
    price = 10

    return Specific_Product(website, url, price)


@pytest.fixture
def website():
    website = "amazon"

    return website
