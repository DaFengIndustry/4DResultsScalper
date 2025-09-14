import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import defaultdict

# Load your data
df = pd.read_csv("4DResults.csv")  # Columns: 'number', 'number_of_times_appeared'

# Dictionary to count trio frequencies
trio_counts = defaultdict(int)

# Process each row
for index, row in df.iterrows():
    number_str = str(row['number']).zfill(4)  # Ensure 4-digit string, e.g., 5 → "0005"
    win_count = row['number_of_times_appeared']

    # Generate all unordered 3-digit combinations
    # e.g., "1234" → ('1','2','3'), ('1','2','4'), ('1','3','4'), ('2','3','4')
    digits = list(number_str)
    for trio in combinations(digits, 3):      # All 3-digit combos, unordered
        # Sort to make "321" = "123"
        sorted_trio = tuple(sorted(trio))
        trio_key = ''.join(sorted_trio)       # e.g., ('1','2','3') → "123"
        trio_counts[trio_key] += win_count

# Get top trios
top_trios = sorted(trio_counts.items(), key=lambda x: x[1], reverse=True)[:-1]
top_labels = [trio[0] for trio in top_trios]   # e.g., ["123", "234", ...]
top_values = [trio[1] for trio in top_trios]   # e.g., [320, 315, ...]

# Plot
plt.figure(figsize=(14, 8))
bars = plt.bar(top_labels, top_values, color='#A23B72', edgecolor='black', linewidth=1.2)

plt.title('Top 10 Most Frequent 3-Digit Trios in Winning 4D Numbers\n(Order Does Not Matter • Data Since May 1986)', 
          fontsize=15, fontweight='bold')
plt.xlabel('3-Digit Trio', fontsize=13)
plt.ylabel('Total Appearances Across All Winning Tickets', fontsize=13)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + max(top_values)*0.01,
             f'{int(height):,}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()