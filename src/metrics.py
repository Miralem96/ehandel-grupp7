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

    plt.bar(city_rev_df['city'], city_rev_df['revenue'], color='pink',  width=0.4)
    plt.text(
        0.95, 0.95,
        f"Medelvärde: {mean_revenue:.2f}\nStd-avvikelse: {std_revenue:.2f}",
        transform=plt.gca().transAxes, 
        ha='right', va='top',
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
    )
    plt.title('Revenue per city: ')
    plt.xlabel('city')
    plt.ylabel('revenue')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    plt.legend()
    plt.show()

    print("\nAlla städer och intäkt: ")
    print(city_rev_df)
    print(f"\nMedelintäkt: {mean_revenue:.2f}")
    print(f"Standardavvikelse: {std_revenue:.2f}")   
    print(type(city_rev))  
    print(type(df))   

  



