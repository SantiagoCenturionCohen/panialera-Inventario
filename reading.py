import csv
import requests
from io import StringIO

# URL de tu hoja de Google Sheets en formato CSV
SHEET_URL = "https://docs.google.com/spreadsheets/d/1Py-GpC4P0czNpEygGOfijd-PVV_8raj4347KS2Ujj2Q/export?format=csv"


# Lee el contenido del archivo una sola vez y lo almacena en una lista
def leer_dataset():
    response = requests.get(SHEET_URL)
    contenido = response.text  # El contenido CSV como string

    # Usamos StringIO para tratar el texto como si fuera un archivo
    f = StringIO(contenido)
    reader = csv.reader(f)
    data = list(reader)
    
    return data

# Llamar a la función para ver el contenido
dataset = leer_dataset()
#for fila in dataset:
 #   print(fila)

# Filtra los productos según el nombre y devuelve el producto, precio y stock
def filtrar_producto(data, nombre_producto):
    productos_filtrados = []
    for fila in data:
        if nombre_producto.lower() in fila[1].lower():  # Busca el nombre en la columna de producto
            productos_filtrados.append((fila[1], fila[2], fila[3]))  # Devuelve el producto, precio y stock
    return productos_filtrados
# Ejemplo de uso
#nombre_producto = "producto1"  # Cambia por el producto que desees buscar
#resultado = filtrar_producto(dataset, nombre_producto)
#for producto, precio in resultado:
#    print(f"Producto: {producto}, Precio: {precio}")