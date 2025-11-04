
import csv
import datetime as dt
import pandas as pd
import calendar as cal

# läser in i csv filen
def load_sales(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    
    # räknar ut pris * antal
    if "revenue" not in df.columns and {"price", "units"}.issubset(df.columns):
        df["revenue"] = df["price"] * df["units"]

    return df


# Matches the column name with an index for easy access with some_dict[column["city"]
column = {"order_id": 0, "date": 1, "city": 2, "category": 3, "price": 4, "units": 5, "revenue": 6}

"""
To get access to all orders from the .csv-file create a variable
and set it equal to extract_orders_from_csv()
    ex:
        orders = extract_orders_from_csv()

To access to an order i.e order 5 and its category
    ex:
        order5 = orders[4][column["category"]]]

Extracts data from .csv-file and returns a list of tuple
"""
def extract_orders_from_csv():
    # List of tuples containing each order
    temp_orders = []

    with open("../data/ecommerce_sales.csv", "r", encoding="utf-8") as file:
        # Create csv-reader
        reader = csv.DictReader(file)

        # Loop over each line in .csv-file
        for line in reader:
            # Append each line from .csv-file as tuple to list of orders
            temp_orders.append((int(line["order_id"]), line["date"], line["city"], line["category"],
                           float(line["price"]), int(line["units"]), float(line["revenue"])))

        return temp_orders

"""
Given a list
    orders = extract_orders_from_csv()
sort it by price and descending order with
    orders = sort_list(orders, "price", True)

# Returns a sorted list of tuples based on category, choose descending/ascending order with True/False
"""
def sort_list(_list_to_sort, _category_to_sort_by, _descending_order):
    return sorted(_list_to_sort, key=lambda k: k[column[_category_to_sort_by]], reverse=_descending_order)



def sort_date_category_units(_df: pd.DataFrame) -> dict:
    temp_sorted_orders = {}

    # Loop over unique dates and category
    for date in _df.date.unique():
        for category in _df.category.unique():
            cat_units = _df.loc[(_df["date"] == date) &
                         (_df["category"] == category), "units"].sum()
            #print(f"Date: {date} {category} units sold {cat_units}") # Debug

            # Check if the date was added. If not, add it.
            if date not in temp_sorted_orders:
                temp_sorted_orders[date] = {category: int(cat_units)}
            # If date was already added. Add order to dict of orders
            else:
                temp_sorted_orders[date][category] = int(cat_units)

    return temp_sorted_orders
