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