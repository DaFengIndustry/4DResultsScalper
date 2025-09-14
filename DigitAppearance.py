import pandas as pd
import matplotlib.pyplot as plt

# Load your scraped data
df = pd.read_csv("4d_results.csv")  # Columns: 'number', 'number_of_times_appeared'

# Initialize digit counter (0 to 9)
digit_counts = {str(d): 0 for d in range(10)}  # {'0':0, '1':0, ..., '9':0}

# Loop through each row in your data
for index, row in df.iterrows():
    number_str = str(row['number']).zfill(4)  # Ensures it's string and 4 digits (e.g., 5 → "0005")     # e.g., "1234"
    win_count = row['number_of_times_appeared']  # e.g., 5

    # Count how many times each digit appears IN THIS NUMBER
    for digit in number_str:            # digit = '1', then '2', then '3', then '4'
        digit_counts[digit] += win_count  # Add win_count to that digit's total

# Prepare data for plotting
digits = list(digit_counts.keys())      # ['0', '1', ..., '9']
counts = list(digit_counts.values())    # [total count for 0, total count for 1, ...]

# Create vertical bar chart
plt.figure(figsize=(10, 6))
plt.bar(digits, counts, color='orange', edgecolor='black')
plt.title('Frequency of Digits 0-9 in All Winning 4D Numbers (Since May 1986)', fontsize=14)
plt.xlabel('Digit', fontsize=12)
plt.ylabel('Total Appearances Across All Winning Tickets', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add value labels on top of bars
for i, count in enumerate(counts):
    plt.text(i, count + max(counts)*0.01, str(count), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()