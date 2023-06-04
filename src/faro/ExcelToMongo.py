# -*- coding: utf-8 -*-
"""
Autor: Carlos Wong
email: carlosawongca@gmail.com
Fecha: 2023_06_04
Objetivo: Conexión con BBDD MongoDB
Entrada: 'CdM_xxxxxx.xlsx' por Central
Salida: -
Propósito: CRUD con MongoDB 
"""

def actualizar_datos(collection, historico):
    # Obtener la fecha y hora actual
    current_datetime = datetime.now()
    # Formatear la fecha y hora con formato personalizado (Año-Mes-Día Hora:Minutos:Segundos)
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Recorre cada fila del DataFrame df
    for index, row in df.iterrows():
        # Obtiene el valor de la columna "ID" como referencia de la fila
        row_id = row['ID.']
        # Recorre cada columna de la fila
        for col_name in df.columns:
            try:
                # Obtiene el valor de la celda
                cell_value = row[col_name]
                # Si el valor nuevo de cell_value es NaN o una cadena vacía, y no existe existing_data, pasa a evaluar el siguiente registro
                if (cell_value is None or pd.isna(cell_value)) and existing_data is None:
                    continue
                # Consulta la base de datos para verificar si ya existe un documento con la misma referencia de fila y nombre de columna
                existing_data = collection.find_one({'row_id': row_id, 'col_name': col_name})
                # Si ya existe, verifica si el valor de la celda (sin considerar el timestamp) es diferente al existente y actualiza el documento
                if existing_data is not None and existing_data['cell_value'] != cell_value:
                    existing_cell_value = existing_data['cell_value']
                    existing_timestamp = existing_data['timestamp']
                    # Si el valor nuevo es igual al valor anterior (sin considerar el timestamp), no se realiza ninguna actualización
                    if cell_value == existing_cell_value:
                        continue
                    if cell_value == "" and existing_cell_value != "":
                        # Guarda el NaN en la colección principal con el timestamp actual
                        collection.update_one({'row_id': row_id, 'col_name': col_name}, {'$set': {'cell_value': cell_value, 'timestamp': formatted_datetime}})
                        # Guarda el valor anterior en la colección histórica con el timestamp original
                        historico.insert_one({
                            'row_id': row_id,
                            'col_name': col_name,
                            'cell_value': existing_cell_value,
                            'timestamp': existing_timestamp
                        })
                    elif cell_value != "" and existing_cell_value == "":
                        # Guarda el valor nuevo en la colección principal con el timestamp actual
                        collection.update_one({'row_id': row_id, 'col_name': col_name}, {'$set': {'cell_value': cell_value, 'timestamp': formatted_datetime}})
                        # Guarda el NaN en la colección histórica
                        historico.insert_one({
                            'row_id': row_id,
                            'col_name': col_name,
                            'cell_value': None,
                            'timestamp': existing_timestamp
                        })
                    elif cell_value != "" and existing_cell_value != "" and cell_value != existing_cell_value:
                        # Guarda el valor nuevo en la colección principal con el timestamp actual
                        collection.update_one({'row_id': row_id, 'col_name': col_name}, {'$set': {'cell_value': cell_value, 'timestamp': formatted_datetime}})
                        # Guarda el valor anterior en la colección histórica con el timestamp original
                        historico.insert_one({
                            'row_id': row_id,
                            'col_name': col_name,
                            'cell_value': existing_cell_value,
                            'timestamp': existing_timestamp
                        })
                # Si no existe, inserta el nuevo documento con el timestamp actual
                elif existing_data is None:
                    if cell_value is not None:
                        data = {
                            'row_id': row_id,
                            'col_name': col_name,
                            'cell_value': cell_value,
                            'timestamp': formatted_datetime
                        }
                        collection.insert_one(data)
                        historico.insert_one(data)
                    else:
                        continue
            except Exception as e:
                # Manejo de la excepción
                print("Ocurrió un error:", e)