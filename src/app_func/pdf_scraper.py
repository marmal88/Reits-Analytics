import tabula
import pandas as pd

pdf = "/home/oem/Documents/coding/personal/Reits-Analytics/data/Ascendas-Reit-Annual-Report-2021.pdf"


def pdf_scraper(pdf):
    tables = tabula.read_pdf(pdf, pages=[72])
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
    # split out completion date parsed incorrectly
    def split_completion_date(text):
        if isinstance(text, str):
            x = text[:9]
            return x

    df["completion_date"] = df["development_cost"].apply(
        lambda x: split_completion_date(x)
    )
    # split out development cost parsed incorrectly
    def split_development_cost(text):
        if isinstance(text, str) and len(text) > 11:
            amt = text[10:]
            return amt

    df["development_cost"] = df["development_cost"].apply(
        lambda x: split_development_cost(x)
    )
    df = df.dropna(how="any", subset=["development_cost", "completion_date"])

    return df
