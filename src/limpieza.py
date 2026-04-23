import pandas as pd
import numpy as np
import os
import logging

# Configurar logs
log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'pipeline.log')
logging.basicConfig(filename=log_path, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def limpiar_datos(ruta_entrada, ruta_salida):
    try:
        logging.info("Iniciando la limpieza de datos avanzada...")
        print("Cargando y limpiando datos...")
        
        # 1. Leer el archivo CSV
        df = pd.read_csv(ruta_entrada)
        
        # 2. Eliminar filas duplicadas
        df = df.drop_duplicates()
        
        # 3. Convertir espacios en blanco a valores nulos reales (NaN)
        df = df.replace(r'^\s*$', np.nan, regex=True)
        
        # 4. Estandarizar textos (Ciudades tipo 'Título' y pagos en minúsculas)
        # Esto convierte 'VALPARAISO' y 'santiago' a 'Valparaiso' y 'Santiago'
        df['ciudad'] = df['ciudad'].str.title().str.strip()
        df['metodo_pago'] = df['metodo_pago'].str.lower().str.strip()
        
        # 5. Rellenar nombres y montos vacíos
        df['nombre'] = df['nombre'].fillna('Cliente Desconocido')
        # Convertir monto a número primero, y rellenar vacíos con el promedio
        df['monto'] = pd.to_numeric(df['monto'], errors='coerce')
        df['monto'] = df['monto'].fillna(df['monto'].mean())
        
        # 6. Limpiar Edades (Quitar edades imposibles y rellenar vacíos)
        df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
        df.loc[df['edad'] > 100, 'edad'] = np.nan # Borrar edad de 150 años
        df['edad'] = df['edad'].fillna(df['edad'].median()) # Rellenar con la mediana
        df['edad'] = df['edad'].astype(int) # Asegurar que sean números enteros
        
        # 7. Estandarizar Fechas (Convierte todo a formato estándar AAAA-MM-DD)
        # Las fechas imposibles (como mes 13) se volverán nulas (NaT)
        df['fecha_compra'] = pd.to_datetime(df['fecha_compra'], errors='coerce')
        
        # 8. Guardar el archivo limpio
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        df.to_csv(ruta_salida, index=False)
        
        logging.info(f"Limpieza exitosa. Archivo guardado en {ruta_salida}")
        print(f"Datos realmente limpios y guardados en {ruta_salida}!")

    except Exception as e:
        logging.error(f"Error en la limpieza: {e}")
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    archivo_sucio = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'ventas_sucias.csv')
    archivo_limpio = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'ventas_limpias.csv')
    
    limpiar_datos(archivo_sucio, archivo_limpio)