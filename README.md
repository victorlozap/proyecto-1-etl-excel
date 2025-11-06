# Proyecto 1: Pipeline ETL de Reporte de Ventas

Este proyecto es el primero de mi portafolio como Ingeniero en Analítica de Datos. El objetivo es demostrar la automatización de un proceso ETL (Extract, Transform, Load) para limpiar y preparar un reporte de ventas de Excel para su análisis.

## 📝 Escenario

Cada mes, se recibe un reporte de ventas (`SaleData.xlsx`) que necesita ser limpiado y validado antes de cargarse al sistema central de análisis. Este script de Python automatiza todo el proceso.

## ⚙️ Tecnologías Utilizadas

* **Python 3**
* **Pandas:** Para la extracción, manipulación y limpieza de datos.
* **Jupyter Notebook:** Para la exploración inicial de datos (ver `exploracion.ipynb`).

## 🔄 El Pipeline ETL

El script `etl_ventas.py` ejecuta las siguientes tareas:

### 1. Extract (Extracción)
* Carga los datos desde el archivo `SaleData.xlsx`.

### 2. Transform (Transformación)
* **Limpieza de Nulos:** Elimina filas que tienen datos faltantes (NaN) para asegurar la integridad de los datos.
* **Estandarización de Nombres:** Renombra las columnas de `CamelCase` (ej. `OrderDate`) a `snake_case` (ej. `order_date`) para consistencia y compatibilidad con bases de datos.
* **Validación de Lógica:** Verifica que la lógica de negocio (`units * unit_price = sale_amount`) sea correcta en todas las filas.

### 3. Load (Carga)
* Exporta el DataFrame limpio y validado a un nuevo archivo: `reporte_ventas_limpio.csv`.

## 🚀 Cómo Ejecutar

1.  Clonar este repositorio.
2.  Instalar las dependencias: `pip install -r requirements.txt`
3.  (Opcional) Colocar un nuevo archivo `SaleData.xlsx` en la carpeta.
4.  Ejecutar el script: `python etl_ventas.py`