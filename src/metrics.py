import pandas as pd
from io_utils import dt, plt

# Read csv file, sort and reset index
df = pd.read_csv("..\\data\\ecommerce_sales.csv")
df.sort_values(by=['date'], ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)

# Sort dict
def sort_date_category_units(_df: pd.DataFrame) -> dict:
    temp_sorted_orders = {}

    # Loop over unique dates and category
    for date in df.date.unique():
        for category in df.category.unique():
            cat_units = df.loc[(df["date"] == date) &
                         (df["category"] == category), "units"].sum()
            #print(f"Date: {date} {category} units sold {cat_units}") # Debug

            # Check if the date was added. If not, add it.
            if date not in temp_sorted_orders:
                temp_sorted_orders[date] = {category: int(cat_units)}
            # If date was already added. Add order to dict of orders
            else:
                temp_sorted_orders[date][category] = int(cat_units)

    return temp_sorted_orders

# Plot the orders by category
def plot_date_category_amount(_dict: dict, _category: str):
    x = []
    y = []

    for date in _dict:
        x.append(dt.datetime.strptime(date, "%Y-%m-%d").date())

    for order in _dict.values():
        if _category in order:
            y.append(order[_category])

    plt.bar(x, y)
    plt.title(_category)
    plt.xlabel("Date")
    plt.ylabel("Units sold")
    plt.show()

# Get dict
sorted_orders = sort_date_category_units(df)

# Plot dict
for cat in df.category.unique():
    plot_date_category_amount(sorted_orders, cat)