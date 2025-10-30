import matplotlib.pyplot as plt
import pandas as pd

def plotMetrics(revenues, mean, median, std, q1, q3):
    plt.figure(figsize=(14,6))
    plt.hist(revenues, bins=250, color='skyblue')

    # Vertical lines
    plt.axvline(mean, color='red', linestyle='--', label=f"Mean: {mean:.2f}")
    plt.axvline(median, color='green', linestyle='--', label=f"Median: {median:.2f}")
    plt.axvline(mean + std, color='orange', linestyle=':', label=f"Mean+Std: {mean+std:.2f}")
    plt.axvline(mean - std, color='orange', linestyle=':', label=f"Mean-Std: {mean-std:.2f}")
    plt.axvline(q1, color='purple', linestyle='-.', label=f"Q1: {q1:.2f}")
    plt.axvline(q3, color='purple', linestyle='-.', label=f"Q3: {q3:.2f}")

    # Fills
    plt.axvspan(q1, q3, color='purple', alpha=0.1)
    plt.axvspan(mean + std, mean - std, color='orange', alpha=0.1)

    # Labels
    plt.xlabel("Revenue")
    plt.ylabel("Count")
    plt.title("Revenue Spread / Distribution")
    plt.legend()
    plt.show()



def plot_revenue_per_capita(per_capita_data):
    per_capita_clean = per_capita_data.dropna()
    
    avg_per_capita = per_capita_clean.mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    

    bars = ax.bar(per_capita_clean.index, per_capita_clean.values, color='steelblue')
    ax.axhline(y=avg_per_capita, color='red', linestyle='--', linewidth=2, label=f'Average: {avg_per_capita:.2f} SEK')
    ax.set_xlabel('City', fontsize=10)
    ax.set_ylabel('Revenue per Capita (SEK)', fontsize=10)
    ax.set_title('Revenue per Capita by City', fontsize=12)
    

    plt.xticks(rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()