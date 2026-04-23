import os
import shutil
import logging

# 1. Configurar la "trazabilidad" (Los mensajes que avisarán qué está pasando)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ingestar_datos():
    logging.info("Iniciando el proceso de ingesta de datos...")

    # 2. Definir dónde está el archivo y a dónde va
    ruta_origen = 'fuente/riesgo_hipertension_dataset.csv'
    ruta_destino = 'data/raw/riesgo_hipertension_dataset.csv'

    # 3. Verificar si el archivo realmente existe en la carpeta fuente
    if not os.path.exists(ruta_origen):
        logging.error(f"¡Error! No se encontró el archivo en: {ruta_origen}")
        return

    # 4. Crear la carpeta de destino por si a caso no existe
    os.makedirs('data/raw', exist_ok=True)

    # 5. Intentar copiar el archivo
    try:
        shutil.copy(ruta_origen, ruta_destino)
        logging.info(f"Éxito: Archivo copiado de '{ruta_origen}' a '{ruta_destino}'")
        logging.info("Proceso de ingesta finalizado correctamente.")
    except Exception as e:
        logging.error(f"Ocurrió un problema al copiar el archivo: {e}")

# Esto hace que el código se ejecute cuando le des "Play"
if __name__ == "__main__":
    ingestar_datos()