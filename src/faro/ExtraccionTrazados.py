'''
Autor: Carlos Wong <br/>
email: carlosawongca@gmail.com <br/>
Fecha: 2023_06_11 <br/>
Objetivo: Extracción de trazados ATLAS de cualquier central -En función del código de la Central <br/>
Entrada: Código de la central, por ejemplo, S.Ta, Z.To, etc. <br/>
Salida: Trazados <br/>
Propósito: Extracción de trazados desde excel sin códigos, simbolos o desplegables <br/>
'''
import pandas as pd

def Extraccion_Trazados(codigo):
    equivalencias = {
        "B.SR": r'\\10.8.0.1\apagado centrales\2023\10_Test\trazados_BSr.xlsx',
        "S.TA": r'\\10.8.0.1\apagado centrales\2023\10_Test\trazados_STa.xlsx',
        "B.ND": r'\\10.8.0.1\apagado centrales\2023\10_Test\trazados_BNd.xlsx',
        "M.US": r'\\10.8.0.1\apagado centrales\2023\10_Test\trazados_MUs.xlsx',
        "Z.TO": r'\\10.8.0.1\apagado centrales\2023\10_Test\trazados_ZTo.xlsx',
        "ELL.MO": r'\\10.8.0.1\apagado centrales\2023\10_Test\trazados_EllMo.xlsx'
    }

    try:
        ruta_archivo = equivalencias[codigo]
    except KeyError:
        raise ValueError("Código no válido o ruta del fichero no válida")
    
    try:
        # Leer el archivo Excel
        excel_file = pd.ExcelFile(ruta_archivo)
        
        # Crear un diccionario vacío para almacenar los dataframes de cada hoja
        dataframes_por_hoja = {}
        
        # Iterar a través de cada hoja del archivo Excel
        for nombre_hoja in excel_file.sheet_names:
            # Leer la hoja y seleccionar las columnas a partir de la tercera columna
            hoja = pd.read_excel(excel_file, sheet_name=nombre_hoja, header=1)
            hoja = hoja.iloc[:, 2:]
            
            try:
                # Eliminar filas con valores nulos en la columna 'Codificación Común'
                if 'Codificación Común' in hoja.columns:
                    hoja = hoja.dropna(subset=['Codificación Común'])
                else:
                    print("La columna 'Codificación Común' no se encuentra en la hoja", nombre_hoja)
            except Exception as e:
                print("Error al procesar la hoja", nombre_hoja, "del archivo Excel:", e)
            
            # Agregar el dataframe a nuestro diccionario con el nombre de la hoja como clave
            dataframes_por_hoja[nombre_hoja] = hoja
        
        excel_file.close()  # Cerrar el archivo Excel
        
        return dataframes_por_hoja
    
    except Exception as e:
        print("Error al procesar el archivo Excel:", e)
        return None