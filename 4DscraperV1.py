from selenium import webdriver 
from selenium.webdriver.common.by import By
import time 


# initial configuration for chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
#Enter singapore pools website
driver.get("https://www.singaporepools.com.sg/en/product/Pages/4d_cpwn.aspx")
time.sleep(3)
#button mapping

number_input= driver.find_element(By.CLASS_NAME, "four-d-user-number") #finds the textbox
number_input.send_keys("1224")
results_button = driver.find_element(By.CLASS_NAME, "btnShowByPrize") #finds display button
results_button.click()


'''
This portion of the code attempts to find the number of times the number won but it is not functional
try:
    times_won = driver.find_element(By.CSS_SELECTOR, "p.summary.pTotalNumberOfAppearances")
    print("found results")
except:
    print("results not found")
else:
    times_won_text = times_won.text
    print(f"Element text: {times_won_text}")

'''

#time.sleep(3)
#number_input.clear()

time.sleep(2)
driver.quit()