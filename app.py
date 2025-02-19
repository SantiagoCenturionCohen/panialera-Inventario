import streamlit as st

import reading


# Cargar el dataset
#dataset = reading.leer_dataset()

# Interfaz de usuario con Streamlit
st.title('Buscador de Productos')
nombre_producto = st.text_input('Introduce el nombre del producto:')

if nombre_producto:
    dataset = reading.leer_dataset()
    resultado = reading.filtrar_producto(dataset, nombre_producto)
    
    if resultado:
        for producto, precio, stock in resultado:
            st.write("**Producto:**")
            st.write(producto)
            st.write("**Precio:**")
            st.write(precio)
            st.write("**Stock:**")
            st.write(stock)
            st.write("")  # Salto de línea entre productos
    else:
        st.write("No se encontró ningún producto que coincida.")