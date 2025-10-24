import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "/Users/lindahansson/Desktop/Gruppuppgift_1/data/ecommerce_sales.csv"

df = pd.read_csv(CSV_PATH) 
df.columns = df.columns.str.strip() 

def revenue_per_city(csv_path=CSV_PATH):
    city_revenue = (
        df.groupby('city')['revenue']
            .sum()
            .sort_values(ascending=False)
    )
    return city_revenue, df

if __name__ == "__main__": 
    city_rev, df = revenue_per_city() 
    city_rev_df = city_rev.reset_index()

    mean_revenue = df['revenue'].mean()
    std_revenue = df['revenue'].std()

    fig, ax = plt.subplots()
    ax.bar(city_rev_df['city'], city_rev_df['revenue'], color='pink',  width=0.5, edgecolor='black')
    ax.text(
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

    print("\nAlla städer och intäkt: ")
    print(city_rev_df)
    print(f"\nMedelintäkt: {mean_revenue:.2f}")
    print(f"Standardavvikelse: {std_revenue:.2f}")   
    print(type(city_rev))  
    print(type(df))   

  



