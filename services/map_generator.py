import folium

def generate_map(latitude, longitude, location_name, output_file="mylocation.html"):
    """
    Genera un mapa interactivo con un marcador en la ubicación especificada.

    :param latitude: Latitud de la ubicación.
    :param longitude: Longitud de la ubicación.
    :param location_name: Nombre de la ubicación para el marcador.
    :param output_file: Nombre del archivo HTML de salida.
    """
    # Crear el mapa centrado en la ubicación
    my_map = folium.Map(location=[latitude, longitude], zoom_start=9)

    # Agregar un marcador con un popup
    folium.Marker([latitude, longitude], popup=location_name).add_to(my_map)

    # Guardar el mapa en un archivo HTML
    my_map.save(output_file)
    print(f"Mapa guardado en {output_file}")