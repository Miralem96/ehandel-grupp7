from io_utils import *
from metrics import *
from viz import *

# Database everyone will use
# Read csv file, sort and reset index
df = pd.read_csv("../data/ecommerce_sales.csv")


# Uppgift 1 - MIRALEM

def main():
    df = pd.read_csv("../data/ecommerce_sales.csv")

    print(type(df))
    df.head()
    cat_rev = revenue_by_category(df)
    cat_rev.head()


    # stapeldiagram
    plt.figure(figsize=(12, 6)) 
    plt.bar(cat_rev["category"], cat_rev["revenue"], color='skyblue')

    # lägger till rubriker
    plt.title("Intäkt per produktkategori", fontsize=16)
    plt.xlabel("Kategori", fontsize=16)
    plt.ylabel("Intäkt", fontsize=16)

    # rutnät
    plt.grid(axis="y", linestyle="-", alpha=0.5)
    plt.tight_layout()
    plt.show()
    

# Uppgift 2 - LINDA

    def revenue_per_city(df):  # function to calculate total revenue per city
        city_revenue = (
            df.groupby('city')['revenue']     # gorup data by city
                .sum()                        # sum revenue values
                .sort_values(ascending=False) # sort result decending
        )
        return city_revenue

    def plot_revenue_per_city(city_rev_df, mean_revenue, std_revenue):
        fig, ax = plt.subplots(figsize=(8, 5))  # create figure and axis for the bar chart
        ax.bar(city_rev_df['city'], city_rev_df['revenue'], color='skyblue',  width=0.5, edgecolor='black')
        ax.text(                              # text box showing mean and standard deviation
            0.95, 0.95,
            f"Medelvärde: {mean_revenue:.2f}\nStd-avvikelse: {std_revenue:.2f}",
            transform=ax.transAxes,
            ha='right', va='top',
            fontsize=10,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
        )

        ax.set_title('Revenue per city: ')
        ax.set_xlabel('city')
        ax.set_ylabel('revenue')
        ax.set_xticks(range(len(city_rev_df['city'])))
        ax.set_xticklabels(city_rev_df['city'], rotation=45, ha='right') 
        fig.tight_layout()
        plt.show()

        # print summary statistics and data types
        print("\nAlla städer och intäkt: ")
        print(city_rev_df)
        print(f"\nMedelintäkt: {mean_revenue:.2f}")
        print(f"Standardavvikelse: {std_revenue:.2f}")

    city_rev = revenue_per_city(df)
    city_rev_df = city_rev.reset_index()
    mean_revenue = df['revenue'].mean()
    std_revenue = df['revenue'].std()

    plot_revenue_per_city(city_rev_df, mean_revenue, std_revenue)


# Uppgift 3 - MARKUS
# Sort by date and reset index
    df.sort_values(by=['date'], ascending=True, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Create a dict containing all orders sorted for each month
    # sorted_orders = {"2024-01-01": {"category": []}}
    sorted_orders = sort_date_category_units(df)

    # Plots all orders
    for category in df.category.unique():
        plot_date_category_amount(sorted_orders, category)



# Uppgift 4 - UFFE

    orders = util.extract_orders_from_csv()
    df = pd.DataFrame(orders, columns=list(util.column.keys()))

    mean, median, std, q1, q3, iqr, spread = revMetrics(df, "revenue")

    print(f"Average Order Value: {mean:.2f}") 
    print(f"Median: {median:.2f}")
    print(f"Spread: {spread:.2f}")
    print(f"IQ3-IQ1: {q3:.2f}-{q1:.2f} = {q3 - q1} ")

    plotMetrics(df["revenue"], mean, median, std, q1, q3)

# Uppgift 5 - ANARKOLI
    top3_categories_by_revenue(df)

# Uppgift 6

    perCapita = revenue_per_capita(df)
    print(perCapita.to_string())
    plot_revenue_per_capita(perCapita)


if __name__ == '__main__': 
    main()



