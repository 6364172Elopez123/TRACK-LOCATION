from services.phone_info import get_phone_details
from services.map_generator import generate_map

def main():
    print("Bienvenido a la aplicación de localización de números de teléfono")

    # Solicitar número de teléfono al usuario
    number = input("Por favor, ingrese un número de teléfono con el código de país: ")

    # Obtener detalles del número
    details = get_phone_details(number)
    if details:
        print("Detalles del número:")
        for key, value in details.items():
            print(f"{key}: {value}")

        # Generar mapa si hay coordenadas
        if details.get("Coordinates"):
            lat = details["Coordinates"]["latitude"]
            lng = details["Coordinates"]["longitude"]
            generate_map(lat, lng, details["Country"])
        else:
            print("No se encontraron coordenadas para generar el mapa.")
    else:
        print("No se pudo obtener información del número.")

if __name__ == "__main__":
    main()