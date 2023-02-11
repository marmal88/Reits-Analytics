import os
from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class WebScraper:
    def __init__(self, URL):
        self.url = URL
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(URL)

    def get_exchange(self, save=False):
        # Getting Date and Time
        date_detail = self.driver.find_element(By.ID, "mainCurrency").text
        elements = date_detail.split(" ")
        date = elements[3]
        time = elements[-1]

        # Header Names
        header = self.driver.find_elements(
            By.XPATH,
            "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/thead/tr/th",
        )
        col_names = []

        for head in header:
            col_names.append(head.text)

        # Locators
        col = self.driver.find_elements(
            By.XPATH, "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/tbody/tr"
        )
        row = self.driver.find_elements(
            By.XPATH,
            "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/tbody/tr[1]/td",
        )

        num_row = len(row)
        num_col = len(col)

        results = []
        for i in range(1, num_col + 1):
            result = []
            for j in range(1, num_row + 1):
                data = self.driver.find_element(
                    By.XPATH,
                    "//table[@class='sc-dxgOiQ dzHkKC tbl-primary mBot-16']/tbody/tr["
                    + str(i)
                    + "]/td["
                    + str(j)
                    + "]",
                ).text
                result.append(data)
            results.append(result)

        df = pd.DataFrame(data=results, columns=col_names)

        df["Date"] = date
        df["Time"] = time

        if save:
            df.to_csv("data/output.csv", index=False)

        return df
