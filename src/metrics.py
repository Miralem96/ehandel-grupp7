import pandas as pd

# path to csv file:
CSV_PATH = "/Users/lindahansson/Desktop/Gruppuppgift_1/data/ecommerce_sales.csv"

def revenue_per_city(csv_path=CSV_PATH):
    df = pd.read_csv(csv_path) # csv in to dataframe
    df.columns = df.columns.str.strip() # remove whitespaces


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


