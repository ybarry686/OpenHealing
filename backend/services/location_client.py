import requests


def get_user_location():
    url = "https://ipapi.co/json/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is None or longitude is None:
            return {
                "success": False,
                "message": "Please enter your ZIP code.",
            }

        return {
            "success": True,
            "city": data.get("city"),
            "state": data.get("region"),
            "zip_code": data.get("postal"),
            "latitude": latitude,
            "longitude": longitude,
        }

    except Exception as error:
        print("Location error:", error)

        return {
            "success": False,
            "message": "Please enter your ZIP code.",
        }
