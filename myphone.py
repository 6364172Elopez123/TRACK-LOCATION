from services.phone_info import get_phone_details
import folium

def main():
    number = input("Por favor, ingrese un número de teléfono con el código de país: ")
    details = get_phone_details(number)
    if details:
        print("Detalles del número:")
        for key, value in details.items():
            print(f"{key}: {value}")

        # Generar mapa si hay coordenadas
        if details.get("Coordinates"):
            lat = details["Coordinates"]["latitude"]
            lng = details["Coordinates"]["longitude"]
            myMap = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=details["Country"]).add_to(myMap)
            myMap.save("mylocation.html")
            print("Mapa guardado como 'mylocation.html'.")
        else:
            print("No se encontraron coordenadas para generar el mapa.")
    else:
        print("No se pudo obtener información del número.")

if __name__ == "__main__":
    main()
