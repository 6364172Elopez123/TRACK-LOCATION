import phonenumbers
from phonenumbers import geocoder, carrier
import requests

def get_phone_details(number):
    try:
        parsed_number = phonenumbers.parse(number, "CO")
        country = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")

        # 1. Intentar con país
        url = f"https://nominatim.openstreetmap.org/search?q={country}&format=json&limit=1"
        response = requests.get(url, headers={"User-Agent": "geoapiExercises"}, verify=False)
        coordinates = None
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            coordinates = {
                "latitude": float(data["lat"]),
                "longitude": float(data["lon"])
            }
        else:
            # 2. Intentar con país + operador
            if operator:
                query = f"{country} {operator}"
                url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&limit=1"
                response = requests.get(url, headers={"User-Agent": "geoapiExercises"}, verify=False)
                if response.status_code == 200 and response.json():
                    data = response.json()[0]
                    coordinates = {
                        "latitude": float(data["lat"]),
                        "longitude": float(data["lon"])
                    }
        # 3. Fallback manual para Colombia
        if not coordinates and country == "Colombia":
            coordinates = {"latitude": 4.099917, "longitude": -72.9088133}
        return {
            "Country": country,
            "Operator": operator,
            "Coordinates": coordinates
        }
    except phonenumbers.NumberParseException as e:
        print(f"Error al procesar el número: {e}")
        return None
    except Exception as e:
        print(f"Error general: {e}")
        return None