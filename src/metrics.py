
import io_utils as util
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def top3_categories_by_revenue(df):
  # Group by category and sum revenue
  top3 = (
      df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
  )

  # Display
  print("Topp 3 kategorier efter intäkt:")
  print(top3)

  top3.plot(kind="bar", color="skyblue")
  plt.title("Topp 3 kategorier efter intäkt")
  plt.xlabel("Kategori")
  plt.ylabel("Intäkt (kr)")
  plt.xticks(rotation=0)
  plt.show()


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
     

def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    # räknar ut intäkt per kategori och sorteral från högsta till lägsta
    result = (df.groupby("category")["revenue"]
              .sum() # räknar alla intäkt per kategori
              .reset_index() # görs till en tabell
              .sort_values("revenue", ascending=False) # sorterar fallande
              )
    return result

def revMetrics(df, cat):
    if df.empty:
        return 0
    mean = df[cat].mean()
    median = df[cat].median()
    std = df[cat].std()
    q1 = df[cat].quantile(0.25)
    q3 = df[cat].quantile(0.75)
    iqr = q3 - q1
    spread = df[cat].max() - df[cat].min()
    
    return mean, median, std, q1, q3, iqr, spread

def revenue_per_capita(df):
    city_revenue = (df.groupby('city')['revenue'].sum().sort_values(ascending=False))
    # populations
    populations = {
        "Stockholm": 995600,
        "Göteborg": 609000,
        "Malmö": 365644,
        "Uppsala": 248016,
        "Västerås": 160763
    }

    city_revenue = pd.Series(city_revenue)

    # Calculate per capita revenue
    per_capita = pd.Series(
        {city: city_revenue[city] / populations[city] if city in populations else None
         for city in city_revenue.index}
    )

    return per_capita


if __name__ == "__main__":
    orders = util.extract_orders_from_csv()
    # print("Average Order Value:", revenueSpread(orders))


