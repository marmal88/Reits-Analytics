import tabula
import pandas as pd
import numpy as np

from src.app_func.api import google_api
from src.app_func.dbs_fx import WebScraper


class Pdf_Scraper:
    def __init__(self):
        pass

    def get_table(self, pdf, page):
        tables = tabula.read_pdf(pdf, pages=page)

        return tables

    def get_rates(self):
        URL = "https://www.dbs.com/in/treasures/rates-online/foreign-currency-foreign-exchange.page"
        exchange_df = WebScraper(URL).get_exchange()

        return exchange_df

    def get_bizpark_df(self, tables):
        df = tables[0]
        df = df.rename(
            columns={
                "Unnamed: 0": "num",
                "Unnamed: 1": "property",
                "Business & Science Park Properties": "development_cost",
                "Unnamed: 2": "valuations_(SGD:Mil)",
                "Unnamed: 3": "gfa_(Sqm)",
                "Unnamed: 4": "nla_(Sqm)",
                "Unnamed: 5": "address",
                "Unnamed: 6": "gross_revenue_(SGD:Mil)",
                "Unnamed: 7": "occupancy_rate",
            }
        )
        # remove first rows
        df = df.iloc[4:]

        df["completion_date"] = df["development_cost"].apply(
            lambda x: split_completion_date(x)
        )

        df["development_cost"] = df["development_cost"].apply(
            lambda x: split_development_cost(x)
        )
        df = df.dropna(how="any", subset=["development_cost", "completion_date"])

        charlist = ["#", "*", "^"]
        for char in charlist:
            df["property"] = df["property"].str.replace(char, "", regex=True)

        loc_dict = {
            "1, 3 & 5 Changi Business Park Crescent": "3 Changi Business Park Crescent",
            "77 & 79 Science Park Drive": "77 Science Park Drive",
            "41, 45 & 51 Science Park Road": "51 Science Park Road",
            "12, 14 & 16 Science Park Drive": "16 Science Park Drive",
        }

        df["address_cord"] = df["address"].apply(
            lambda x: google_api().return_lat_long(x, "Singapore", loc_dict)
        )
        df["property_cord"] = df["property"].apply(
            lambda x: google_api().return_lat_long(x, "Singapore", loc_dict)
        )

        df["lat_lng"] = np.where(
            df["address_cord"].isna(), df["property_cord"], df["address_cord"]
        )

        df["lattitude"] = df["lat_lng"].apply(lambda x: x[0])
        df["longitude"] = df["lat_lng"].apply(lambda x: x[1])

        df.drop(columns=["address_cord", "property_cord", "lat_lng"], inplace=True)

        floattypes = [
            "development_cost",
            "valuations_(SGD:Mil)",
            "gross_revenue_(SGD:Mil)",
        ]

        for each in floattypes:
            df[each] = df[each].apply(lambda x: to_numeric(x))

        return df


# split out completion date parsed incorrectly
def split_completion_date(text):
    if isinstance(text, str):
        x = text[:9]
        return x


# split out development cost parsed incorrectly
def split_development_cost(text):
    if isinstance(text, str) and len(text) > 11:
        amt = text[10:]
        return amt


def to_numeric(number):
    try:
        return float(number)
    except:
        return 0
