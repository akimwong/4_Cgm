'''
Autor: Carlos Wong
email: carlosawongca@gmail.com
Fecha: 2023_05_07
Objetivo: Extracción de trazados ATLAS 
Entrada: 'trazados.xlsx' 
Salida: - 
Propósito: Prueba extracción de trazados desde excel sin códigos, simbolos o desplegables
'''
import pandas as pd

# Ruta del archivo Excel
ruta_archivo = r'.\trazados.xlsx'
excel_file = pd.ExcelFile(ruta_archivo)

# Crear un diccionario vacío para almacenar los dataframes de cada hoja
dataframes_por_hoja = {}
# Iterar a través de cada hoja del archivo Excel
for nombre_hoja in excel_file.sheet_names:
    
    # Leer la hoja y seleccionar las columnas a partir de la tercera columna
    hoja = pd.read_excel(excel_file, sheet_name=nombre_hoja, header=1)
    hoja = hoja.iloc[:, 2:]
    
    # Eliminar filas con valores nulos
    hoja = hoja.dropna(subset=['Codificación Común'])
    
    # Agregar el dataframe a nuestro diccionario con el nombre de la hoja como clave
    dataframes_por_hoja[nombre_hoja] = hoja

print(dataframes_por_hoja['Hoja2'])