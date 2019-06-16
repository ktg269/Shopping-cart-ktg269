#shopping_cart_test.py

import pytest
from shopping_cart import to_usd

def test_to_usd():   # to test price formatting
    assert to_usd(18.50) == "$18.50"

    assert to_usd(18.5) == "$18.50"

    assert to_usd(18.5099999) == "$18.51"
    
    assert to_usd(3195849.65) == "$3,195,849.65"

from shopping_cart import find_product

def test_find_product(): # to test find_product using one example (name)
    products = [
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    ]

    matching_product = find_product("5", products)
    assert matching_product["name"] == "Green Chile Anytime Sauce"
    assert matching_product["department"] == "pantry"
    assert matching_product["price"] == 7.99

    with pytest.raises(IndexError):  # Looking up pre-defined, IndexError: https://stackoverflow.com/questions/52077389/how-to-only-report-failures-from-a-type-of-exception-with-pytest
        find_product("10000000", products)

#def test_human_friendly_timestamp(): # to test timestamp
    #assert human_friendly_timestamp("6/16/2019") == "t.strftime("%Y-%m-%d %I:%M %p\n")"

#from shopping_cart import calculate_total_price

#def test_calculate_total_price(): # to test total price
#    products = [
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#    ]
#    
#    matching_product = find_product("5", products)
#    matching_product = find_product("6", products)
#    assert test_calculate_total_price == 29.98