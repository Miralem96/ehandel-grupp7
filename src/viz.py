
import matplotlib.pyplot as plt
import datetime as dt
from io_utils import cal

def plot_date_category_amount(_dict: dict, _category: str) -> None:
    # Bar plot x and y values
    x_bar = []
    y_bar = []

    # Average line stretch on x
    # First line (January) stretches from x_line_min[0] to x_line_max[0]
    x_line_min = []
    x_line_max = []

    # Average line y values
    y_lines = []

    # Calculates x_line_min, x_line_max and average for each month
    temp_list = list(_dict.values())
    cur_day_count = 0
    for i in range(1, 7):
        average = 0

        temp_min = dt.datetime.strptime("2024"+(str(f"-{i}-")+"01"), "%Y-%m-%d").date()
        x_line_min.append(temp_min)
        #print(temp_min)

        temp_max = temp_min + dt.timedelta(days=cal.monthrange(temp_min.year, temp_min.month)[1] - 1)
        x_line_max.append(temp_max)
        #print(temp_max)

        #print(cal.monthrange(temp_min.year, temp_min.month)[1])
        for j in range(cal.monthrange(temp_min.year, temp_min.month)[1]):
            #print(temp_list[j][_category])
            average += temp_list[cur_day_count + j][_category]

        cur_day_count += cal.monthrange(temp_min.year, temp_min.month)[1]
        average = average / cal.monthrange(temp_min.year, temp_min.month)[1]
        y_lines.append(average)
        #print(average)

    # x and y values for bar plot
    for date in _dict:
        temp_date = dt.datetime.strptime(date, "%Y-%m-%d").date()
        x_bar.append(temp_date)

    for order in _dict.values():
        if _category in order:
            y_bar.append(order[_category])

    # Plot settings
    fig, ax = plt.subplots()
    ax.bar(x_bar, y_bar)
    ax.hlines(y=y_lines, xmin=x_line_min, xmax=x_line_max, linestyles="-",
              linewidth=2, color="black", label="Monthly average")
    ax.set_title(_category)
    ax.set_xlabel("Date")
    ax.set_ylabel("Units sold")
    ax.legend()

    # Show plot
    plt.show()


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