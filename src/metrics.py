import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ecommerce_sales.csv")

df = pd.read_csv(CSV_PATH) 
df.columns = df.columns.str.strip()  # remove whitepaces

def revenue_per_city(csv_path=CSV_PATH):  # function to calculate total revenue per city
    city_revenue = (
        df.groupby('city')['revenue']     # gorup data by city
            .sum()                        # sum revenue values
            .sort_values(ascending=False) # sort result decending
    )
    return city_revenue, df

def plot_revenue_per_city(city_rev_df, mean_revenue, std_revenue):
    """Plot revenue per city as a bar chart"""
    fig, ax = plt.subplots()
    ax.bar(city_rev_df['city'], city_rev_df['revenue'],
           color='skyblue', width=0.5, edgecolor='black')
    
    ax.text(                              # text box showing mean and standard deviation
        0.95, 0.95,
        f"Medelvärde: {mean_revenue:.2f}\nStd-avvikelse: {std_revenue:.2f}",
        transform=ax.transAxes,
        ha='right', va='top',
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
    )
    # plot titles and axis labels
    ax.set_title('Revenue per city: ')
    ax.set_xlabel('city')
    ax.set_ylabel('revenue')

    # set tick positions and rotate labels for readability
    ax.set_xticks(range(len(city_rev_df['city'])))
    ax.set_xticklabels(city_rev_df['city'], rotation=45, ha='right') 

    fig.tight_layout()                    # adjust layout to prevent label overlap
    plt.show()                            # display the chart

    # print summary statistics and data types
    print("\nAlla städer och intäkt: ")
    print(city_rev_df)
    print(f"\nMedelintäkt: {mean_revenue:.2f}")
    print(f"Standardavvikelse: {std_revenue:.2f}")   
    print(type(city_rev_df))  
    print(type(df))   

  



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

import pandas as pd

def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    # räknar ut intäkt per kategori och sorteral från högsta till lägsta
    result = (df.groupby("category")["revenue"]
              .sum() # räknar alla intäkt per kategori
              .reset_index() # görs till en tabell
              .sort_values("revenue", ascending=False) # sorterar fallande
              )
    return result
