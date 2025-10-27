import io_utils as util
import pandas as pd

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


if __name__ == "__main__":
    orders = util.extract_orders_from_csv()
    # print("Average Order Value:", revenueSpread(orders))