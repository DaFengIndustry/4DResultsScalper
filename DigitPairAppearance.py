import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import defaultdict

df = pd.read_csv("4DResults.csv")  # Columns: 'number', 'number_of_times_appeared'

pair_counts = defaultdict(int)

for index, row in df.iterrows():
    number_str = str(row['number']).zfill(4)  # Ensure 4-digit string
    win_count = row['number_of_times_appeared']

    # Generate all unordered 2-digit combinations
    # e.g., "1234" → ('1','2'), ('1','3'), ('1','4'), ('2','3'), ('2','4'), ('3','4')
    digits = list(number_str)
    for pair in combinations(digits, 2):  # All 2-digit combos, unordered
        sorted_pair = tuple(sorted(pair))
        pair_key = ''.join(sorted_pair)  
        pair_counts[pair_key] += win_count

# Get top pairs
top_pairs = sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)[:-1]
top_labels = [pair[0] for pair in top_pairs]   
top_values = [pair[1] for pair in top_pairs]   


plt.figure(figsize=(12, 7))
bars = plt.bar(top_labels, top_values, color='#2E86AB', edgecolor='black', linewidth=0.5)

plt.title('Top 10 Most Frequent 2-Digit Combinations in Winning 4D Numbers\n(Order Does Not Matter • Data Since May 1986)', 
          fontsize=14, fontweight='bold')
plt.xlabel('2-Digit Combination', fontsize=12)
plt.ylabel('Total Appearances Across All Winning Tickets', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + max(top_values)*0.01,
             f'{int(height):,}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.xticks(rotation=45, fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()
plt.show()