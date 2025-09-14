import requests
import json
import csv

#API CONFIG
URL = "https://www.singaporepools.com.sg/_layouts/15/FourD/FourDCommon.aspx/Get4DNumberCheckResultsJSON"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.singaporepools.com.sg/en/product/Pages/4d_cpwn.aspx",
    "Origin": "https://www.singaporepools.com.sg"
}

def get_win_count(number):
    payload = {
        "numbers": [str(number).zfill(4)],
        "checkCombinations": "true",
        "sortTypeInteger": "1"
    }
    try:
        response = requests.post(URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        data = json.loads(response.json()['d'])
        return data[0]['NumberOfAppearances']  # e.g., 5
    except Exception as e:
        print(f"Error for {number}: {e}")
        return 0

#
with open("4d_results.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["number", "number_of_times_appeared"])  

    for num in range(0, 10000):  
        formatted_num = str(num).zfill(4)
        win_count = get_win_count(num)
        writer.writerow([formatted_num, win_count])
        print(f"{formatted_num} → {win_count} wins")
        

print("Saved to '4d_results.csv'")