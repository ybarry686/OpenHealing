import os

import requests
from dotenv import load_dotenv

load_dotenv()


def search_resources(query, latitude=None, longitude=None, zip_code=None):
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        return []

    params = {
        "engine": "google_maps",
        "q": query,
        "type": "search",
        "api_key": api_key,
    }

    if latitude is not None and longitude is not None:
        params["ll"] = "@" + str(latitude) + "," + str(longitude) + ",14z"

    elif zip_code:
        params["q"] = query + " near " + zip_code

    else:
        return []

    url = "https://serpapi.com/search"

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

    except Exception as error:
        print("SerpApi error:", error)
        return []

    resources = []

    for place in data.get("local_results", []):
        resources.append(
            {
                "name": place.get("title", "Unknown resource"),
                "address": place.get("address", "No address available"),
                "category": place.get("type", "Support resource"),
                "rating": place.get("rating"),
                "phone": place.get("phone"),
                "website": place.get("website"),
                "latitude": place.get("gps_coordinates", {}).get("latitude"),
                "longitude": place.get("gps_coordinates", {}).get("longitude"),
            }
        )

    return resources
