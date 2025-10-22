import pandas as pd

# läser in i csv filen
def load_sales(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    
    # räknar ut pris * antal
    if "revenue" not in df.columns and {"price", "units"}.issubset(df.columns):
        df["revenue"] = df["price"] * df["units"]

    return df