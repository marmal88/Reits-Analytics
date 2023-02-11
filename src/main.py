import numpy as np


from src.app_func.pdf import pdf_scraper
from src.app_func.dbs_fx import WebScraper
from src.app_func.api import google_api


# URL = "https://www.dbs.com/in/treasures/rates-online/foreign-currency-foreign-exchange.page"

# exchange_df = WebScraper(URL).get_exchange()

pdf = "/home/oem/Documents/coding/personal/Reits-Analytics/data/Ascendas-Reit-Annual-Report-2021.pdf"

buildings_df = pdf_scraper(pdf)

buildings_df["address_cord"] = buildings_df["address"].apply(
    lambda x: google_api().return_lat_long(x, "Singapore")
)
buildings_df["property_cord"] = buildings_df["property"].apply(
    lambda x: google_api().return_lat_long(x, "Singapore")
)

buildings_df["lat_lng"] = np.where(
    buildings_df["address_cord"].isna(),
    buildings_df["property_cord"],
    buildings_df["address_cord"],
)

buildings_df.drop(columns=["address_cord", "property_cord"], inplace=True)

print(buildings_df.head())
