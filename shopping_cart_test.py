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

    matching_product = find_product("5", products) #If works.
    assert matching_product["name"] == "Green Chile Anytime Sauce"
    assert matching_product["department"] == "pantry"
    assert matching_product["price"] == 7.99

    with pytest.raises(IndexError):  # if not working. Looking up pre-defined using IndexError - resource: https://stackoverflow.com/questions/52077389/how-to-only-report-failures-from-a-type-of-exception-with-pytest
        find_product("10000000", products)

from shopping_cart import human_friendly_timestamp

def test_human_friendly_timestamp(): # to test timestamp
    from datetime import datetime
    t = datetime.today()
    assert human_friendly_timestamp(t) == t.strftime("%Y-%m-%d %I:%M %p")

