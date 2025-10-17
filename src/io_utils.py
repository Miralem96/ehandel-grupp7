import csv

"""
To get access to all orders from the .csv-file create a variable
and set it equal to extract_orders_from_csv()
    ex:
        orders = extract_orders_from_csv()

To access to an order i.e order 5 and its category
    ex:
        order5 = orders[4][column["category"]]]
"""

# Matches the column name with an index for easy access
column = {"order_id": 0, "date": 1, "city": 2, "category": 3, "price": 4, "units": 5, "revenue": 6}

def extract_orders_from_csv():
    # List of tuples containing each order
    temp_orders = []

    with open("..\\data\\ecommerce_sales.csv", "r", encoding="utf-8") as file:
        # Create csv-reader
        reader = csv.DictReader(file)

        # Loop over each line in .csv-file
        for line in reader:
            # Append each line from .csv-file as tuple to list of orders
            temp_orders.append((line["order_id"], line["date"], line["city"], line["category"],
                           line["price"], line["units"], line["revenue"]))

        return temp_orders
