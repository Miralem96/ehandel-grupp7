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


