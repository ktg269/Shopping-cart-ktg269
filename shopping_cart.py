#shopping_cart.py

def to_usd(store_price):   # The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
    return '${:,.2f}'.format(store_price)

def find_product(item_id, item_products):
    matching_products = [p for p in item_products if str(p["id"]) == str(item_id)]
    matching_product = matching_products[0]
    return matching_product

def human_friendly_timestamp(time):
    from datetime import datetime
    t = datetime.today()
    return t.strftime("%Y-%m-%d %I:%M %p")
    
if __name__ == "__main__":

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
         
    # INFO DISPLAY/OUTPUT

    print("------------------------------")
    print("BEST IN TOWN GROCERY") # grocery store name of my choice
    print("100 UNIVERSITY ROAD") # A grocery store phone number and/or website URL and/or address of choice
    print("NEW YORK, NY 10020")
    print("TEL: 212-555-7777")
    print("WWW.BESTINTOWNGROCERY.COM")
    print("------------------------------")

    from datetime import datetime # The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
    t = datetime.today()    
    print("CHECKOUT AT: " + t.strftime("%Y-%m-%d %I:%M %p"))   # Referece: The datetime Module guide (official Python guide)
    print("------------------------------")    

    print("SELECTED PRODUCT(S): ")

    for selected_id in selected_ids:
            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            matching_product = matching_products[0]
            subtotal_price = subtotal_price + matching_product["price"]
            print("... "  + matching_product["name"] + " (" + to_usd(matching_product["price"])+")")   # The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices

    tax_rate = 0.0875
    sales_tax = subtotal_price * tax_rate  # The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
    total_price = subtotal_price + sales_tax

    print("------------------------------")
    print("SUBTOTAL:      " + to_usd(subtotal_price))
    print("TAX (8.75%):   " + to_usd(sales_tax))
    print("               " + "-------")
    print("TOTAL:         " + to_usd(total_price)) # The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
    print("------------------------------")
          
    import os, time
    
    file_name = t.strftime("%Y-%m-%d-%H-%M-%S.%f") + ".txt" # Writing text file with timestamp in the txt file name. Reference: Per slack discussion with classmate.   
    myFile = open((os.path.join(os.path.dirname(__file__), "receipts", file_name)), "w")
    myFile.write("------------------------------\n")
    myFile.write("YOUR RECEIPT:\n")
    myFile.write("------------------------------\n")
    myFile.write("BEST IN TOWN GROCERY\n")
    myFile.write("100 UNIVERSITY ROAD\n")
    myFile.write("NEW YORK, NY 10020\n")
    myFile.write("TEL: 212-555-7777\n")
    myFile.write("WWW.BESTINTOWNGROCERY.COM\n")
    myFile.write("------------------------------\n")
    myFile.write("CHECKOUT AT: " + t.strftime("%Y-%m-%d %I:%M %p\n"))
    myFile.write("------------------------------\n")
    
    for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]      
        myFile.write("... "  + matching_product["name"] + " (" + to_usd(matching_product["price"])+")\n")

    myFile.write("------------------------------\n")
    myFile.write("SUBTOTAL:      " + to_usd(subtotal_price))
    myFile.write("\n")
    myFile.write("TAX (8.75%):   " + to_usd(sales_tax))
    myFile.write("\n")
    myFile.write("------------------------------")
    myFile.write("\n")
    myFile.write("TOTAL:         " + to_usd(total_price))
    myFile.write("\n")
    myFile.write("------------------------------\n")
    myFile.write("THANK YOU FOR SHOPPING AT BEST IN TOWN GROCERY. WE HOPE TO SEE YOU AGAIN !") # A friendly message thanking the customer and/or encouraging the customer to shop again
    myFile.write("\n")
    myFile.write("------------------------------\n")

    receipt_print = input("WOULD YOU LIKE YOUR RECEIPT VIA EMAIL AS WELL? Press y to receive or any other key to finish:") # Ask customer whether he or she also want receipt in the email. 
    while True:
        
        if receipt_print =="y":   # sending email receipt
        
            user_input = input("PLEASE ENTER YOUR EMAIL ADDRESS: ") # asking user email address for input.

            import os
            from dotenv import load_dotenv
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            
            load_dotenv()
            
            SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")  #private information included in .env
            SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'") #private information included in .env
            MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'") #private information included in .env
            
            template_data = {   # showing the checkout timestamp and the total price on the email receipt (minimum level of information per instruction)
                "total_price_usd": str(to_usd(total_price)),
                "human_friendly_timestamp": str(t.strftime("%Y-%m-%d %I:%M %p")),
                
            }
            client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
            print("CLIENT:", type(client))

            message = Mail(from_email=MY_ADDRESS, to_emails=user_input) # For to_emails, MY_ADDRESS is replaced with user_input from line 133.
            print("MESSAGE:", type(message))

            message.template_id = SENDGRID_TEMPLATE_ID

            message.dynamic_template_data = template_data

            try:
                response = client.send(message)
                print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
                print(response.status_code) #> 202 indicates SUCCESS
                print(response.body)
                print(response.headers)

            except Exception as e:
                print("OOPS", e.message)

            print("YOUR RECEIPT HAS BEEN SENT. THANK YOU AND WE HOPE TO SEE YOU AGAIN !") # A friendly message thanking the customer and/or encouraging the customer to shop again
            break

        else:
            print("PLEASE TAKE YOUR PAPER RECEIPT. THANK YOU AND WE HOPE TO SEE YOU AGAIN !") # No email receipt if customer does not select y.
            break


                    
            
