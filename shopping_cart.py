#shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# INFO CAPTURE/INPUT

valid_ids = [str(p["id"]) for p in products] # doing comparisons with string versions of these ids
#print("VALID IDS:", valid_ids)

subtotal_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier, or DONE: ") #> "9" (string)
    #> "DONE"
    if selected_id == "DONE":
        break # stops the loop
    elif str(selected_id) in valid_ids:
        selected_ids.append(selected_id)
    else:
        print("Invalid input. Please try again...")
            
        #matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        #matching_product = matching_products[0]
        #total_price = total_price + matching_product["price"]
        #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))
        #selected_ids.append(selected_id)

# INFO DISPLAY/OUTPUT

# A grocery store name of your choice &
# A grocery store phone number and/or website URL and/or address of choice
print("------------------------------")
print("BEST IN TOWN GROCERY")
print("100 UNIVERSITY ROAD")
print("NEW YORK, NY 10020")
print("TEL: 212-555-7777")
print("WWW.BESTINTOWNGROCERY.COM")
print("------------------------------")

# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
# Referece: The datetime Module guide (official Python guide)

from datetime import datetime
t = datetime.today()
print("CHECKOUT AT: " + t.strftime("%Y-%m-%d %I:%M %p"))
print("------------------------------")


# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)

def to_usd(store_price):
    return '${:,.2f}'.format(store_price)

print("SELECTED PRODUCT(S): ")

for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        subtotal_price = subtotal_price + matching_product["price"]
        print("... "  + matching_product["name"] + " (" + to_usd(matching_product["price"])+")")

# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
# The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)

tax_rate = 0.0875
sales_tax = subtotal_price * tax_rate
total_price = subtotal_price + sales_tax

# The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
print("------------------------------")
print("SUBTOTAL:      " + to_usd(subtotal_price))
print("TAX (8.75%):   " + to_usd(sales_tax))
print("               " + "-----")
print("TOTAL:         " + to_usd(total_price))
print("------------------------------")

# A friendly message thanking the customer and/or encouraging the customer to shop again
print("THANK YOU FOR SHOPPING AT BEST IN TOWN GROCERY. WE HOPE TO SEE YOU AGAIN !")
print("------------------------------")



