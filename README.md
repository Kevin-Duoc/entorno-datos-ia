# Actividades: Entorno de Datos IA
**Estudiante:** Kevin Fuenzalida  
**Institución:** Duoc UC  
**Carrera:** Ingeniería en Informática mención en Inteligencia Artificial

## Descripción del Repositorio
Este repositorio contiene el desarrollo de las actividades prácticas del ramo **Entorno de Datos e IA**. Aquí se implementan flujos de trabajo basados en metodologías DataOps, cubriendo desde la ingesta de datos hasta el despliegue de modelos.

## Contenidos del Ramo
A continuación se detallan las actividades e hitos desarrollados durante el semestre:

### Unidad 2: Fundamentos de Pipelines e Ingesta
* **2.1 Pipeline de Datos – Ingesta de datos automatizada:** Creación de un script en Python para la captura de datos crudos (CSV) y organización de la arquitectura inicial de carpetas (`fuente` -> `data/raw`).

### Unidad 2: Limpieza y transformación de datos
* **2.2 Pipeline de Datos – Limpieza y transformación del dataset:** Implementación de un script en Python (`limpieza.py`) utilizando la librería `pandas` para depurar y estandarizar datos. El proceso aplicado asegura la calidad estructural y semántica e incluye:
  * Eliminación de registros duplicados exactos.
  * Manejo de valores nulos y estandarización de textos (nombres de ciudades y métodos de pago).
  * Imputación de datos faltantes matemáticamente (uso de promedios para montos y medianas para edades).
  * Tratamiento de valores atípicos (outliers, ej. edades fuera de rango).
  * Estandarización del formato de fechas a `AAAA-MM-DD`.
  * Generación de un dataset limpio en la ruta `data/processed/`.

## Herramientas Utilizadas
* **Lenguaje:** Python 3.x (Librerías: Pandas, NumPy)
* **Control de Versiones:** Git & GitHub
* **Entorno:** Visual Studio Code