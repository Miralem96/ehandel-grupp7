import pandas as pd
import matplotlib.pyplot as plt

# path to csv file:
CSV_PATH = "/Users/lindahansson/Desktop/Gruppuppgift_1/data/ecommerce_sales.csv"

df = pd.read_csv(CSV_PATH) # csv in to dataframe
df.columns = df.columns.str.strip() # remove whitespaces

def revenue_per_city(csv_path=CSV_PATH):
    # group by city and sum revenue, sorted descending
    city_revenue = (
        df.groupby('city')['revenue']
            .sum()
            .sort_values(ascending=False)
    )
    return city_revenue, df

if __name__ == "__main__":
    # get revenue per city and full DataFrame
    city_rev, df = revenue_per_city()
    # convert to DataFrame for nicer display
    city_rev_df = city_rev.reset_index()

     # Calculate mean and standard deviation of revenue
    mean_revenue = df['revenue'].mean()
    std_revenue = df['revenue'].std()

    plt.bar(city_rev_df['city'], city_rev_df['revenue'], color='pink')


    # Add text box inside the plot
    plt.text(
        0.95, 0.95,
        f"Medelvärde: {mean_revenue:.2f}\nStd-avvikelse: {std_revenue:.2f}",
        transform=plt.gca().transAxes,  # position relative to plot
        ha='right', va='top',
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
    )

    plt.title('Revenue per city: ')
    plt.xlabel('city')
    plt.ylabel('revenue')
    plt.xticks(rotation=45, ha='right')  # så att stadnamnen syns bättre
    plt.tight_layout()  # fixar layouten
    plt.legend()
    plt.show()

   


print("\nAlla städer och intäkt: ")
print(city_rev_df)
print(f"\nMedelintäkt: {mean_revenue:.2f}")
print(f"Standardavvikelse: {std_revenue:.2f}")   
print(type(city_rev))  
print(type(df))   

  



