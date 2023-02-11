import os
from dotenv import load_dotenv
import requests

load_dotenv()


class google_api:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_KEY")

    def return_lat_long(self, query, country):
        query = self.custom_query(query, country)
        path = f"https://maps.googleapis.com/maps/api/geocode/json?address={query}?,+CA&key={self.api_key}"
        response = requests.get(path)
        jsonresponse = response.json()
        if jsonresponse["status"] == "OK":
            lat = jsonresponse["results"][0]["geometry"]["location"]["lat"]
            long = jsonresponse["results"][0]["geometry"]["location"]["lng"]
            return lat, long
        return None

    def custom_query(self, query, country):
        if query == "1, 3 & 5 Changi Business Park Crescent":
            query = "3 Changi Business Park Crescent"
        query = query + f", {country}"
        query = query.replace(" ", "%20")

        return query
