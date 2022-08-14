import os
from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


url = "https://www.dbs.com/in/treasures/rates-online/foreign-currency-foreign-exchange.page"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# Getting Date and Time
date_detail = driver.find_element(By.ID, "mainCurrency").text
s = date_detail.split(' ')

date = s[3]
updated = s[-1]

# Header Names
header = driver.find_elements(By.XPATH, "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/thead/tr/th")
col_names = []

for head in header:
    col_names.append(head.text)

# Locators
col = driver.find_elements(By.XPATH, "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/tbody/tr")
row = driver.find_elements(By.XPATH, "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/tbody/tr[1]/td")

num_row = len(row)
num_col = len(col) 

results = []
for i in range (1, num_col + 1):
    result = []
    for j in range (1, num_row + 1):
        d = driver.find_element(By.XPATH, "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        result.append(d)
    results.append(result)

df = pd.DataFrame(data=results, columns=col_names)

df["Date"] = date
df["Time"] = updated

print(df)