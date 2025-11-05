# Importamos la librería necesaria
import pandas as pd

def limpiar_datos_ventas(archivo_excel):
    """
    Función que implementa el pipeline ETL para los datos de ventas.
    E (Extract): Carga los datos desde un archivo Excel.
    T (Transform): Limpia, estandariza y valida los datos.
    L (Load): Guarda los datos limpios en un archivo CSV.
    """
    
    print(f"Iniciando pipeline ETL para '{archivo_excel}'...")

    # --- (E)XTRACT ---
    try:
        # Cargamos los datos del archivo Excel
        df = pd.read_excel(archivo_excel)
        print("1. (E) Extracción de datos completada.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_excel}'.")
        return
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return

    # --- (T)RANSFORM ---
    
    # Paso 1: Manejar valores nulos (NaN)
    # Guardamos el número de filas antes y después para el log
    filas_antes = df.shape[0]
    df.dropna(inplace=True)
    filas_despues = df.shape[0]
    print(f"2. (T) Transformación: {filas_antes - filas_despues} filas con nulos eliminadas.")

    # Paso 2: Estandarizar nombres de columnas
    nuevos_nombres = {
        'OrderDate': 'order_date',
        'Region': 'region',
        'Manager': 'manager',
        'SalesMan': 'sales_man',
        'Item': 'item',
        'Units': 'units',
        'Unit_price': 'unit_price',
        'Sale_amt': 'sale_amount'
    }
    df.rename(columns=nuevos_nombres, inplace=True)
    print("3. (T) Transformación: Nombres de columnas estandarizados.")

    # Paso 3: Validación de lógica de negocio (Opcional pero recomendado)
    # Verificamos si hay discrepancias sin guardar columnas extra
    diferencia = (df['units'] * df['unit_price']) - df['sale_amount']
    if diferencia.sum() != 0:
        print("¡Alerta! Se encontraron discrepancias en la lógica de 'sale_amount'.")
    else:
        print("4. (T) Transformación: Lógica de negocio validada (sale_amount es correcto).")

    # --- (L)OAD ---
    archivo_salida = 'reporte_ventas_limpio.csv'
    
    # Seleccionamos solo las columnas finales (ya están renombradas)
    columnas_finales = list(nuevos_nombres.values())
    df_limpio = df[columnas_finales]
    
    # Guardamos en CSV
    df_limpio.to_csv(archivo_salida, index=False, encoding='utf-8')
    print(f"5. (L) Carga completada. Archivo guardado como '{archivo_salida}'.")
    print("--- Pipeline ETL finalizado con éxito ---")


# Esta es la parte estándar de Python que ejecuta el código
# solo si se corre este archivo directamente (no si se importa)
if __name__ == "__main__":
    limpiar_datos_ventas('SaleData.xlsx')