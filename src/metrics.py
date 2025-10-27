<<<<<<< HEAD

=======
import pandas as pd

def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    # räknar ut intäkt per kategori och sorteral från högsta till lägsta
    result = (df.groupby("category")["revenue"]
              .sum() # räknar alla intäkt per kategori
              .reset_index() # görs till en tabell
              .sort_values("revenue", ascending=False) # sorterar fallande
              )
    return result
>>>>>>> feat/miralem
