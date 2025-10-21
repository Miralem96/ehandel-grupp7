import pandas as pd

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
    
    # print results
    print("\nAlla städer med intäkt: ")
    print(city_rev_df)


