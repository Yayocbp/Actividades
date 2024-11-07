import pandas as pd
import os
#import matplotlib.pyplot as plt #https://programacion.top/python/que-es-matplotlib-en-python/, se agrega Alias plt para reducir el nombre de la libreria

def cargar_dataset(ruta_dataset: str) -> pd.DataFrame:
    # Abre el archivo desde la misma carpeta donde se encuentra el script
    Abre_Archivo = os.path.join(os.path.dirname(__file__), ruta_dataset)
    
    # Cargar el dataset usando pandas
    df = pd.read_csv(Abre_Archivo)
    
    # Mostrar las primeras 5 filas (por defecto) del dataset para revisar su contenido
    print(df.head()) #le puedo agregar un valor dentro del parentesis de head() para visualizar más o menos filas
    
## Convertir la columna 'ID' a entero (por si alguna vez llega en otro formato)
    if df['ID'].dtype != 'int64':
        df ['ID'] = df ['ID'].astype(int)
   
#Convertir la columna 'Activo' a booleano
    if df['Activo'].dtype != 'bool':
          df['Activo']= df['Activo'].astype(bool)
    #print(df)
  

#Limpiar y convertir la columna 2016 a flotante
    #df['Unidades'] =pd.to_numeric(df['Unidades'], errors='coerce').fillna(0).astype(float) #con coerce, el valor no numerico, lo converte en NaN

# Limpiar y convertir la columna '2016' a flotante
    df['2016'] = df['2016'].replace('[\$,]', '', regex=True)  # Elimina el símbolo $ y las comas
    df['2016'] = pd.to_numeric(df['2016'], errors='coerce').fillna(0).astype(float)  # Convierte a float

# Visualizar los datos modificados
    print(df)



 # Limpiar y convertir la columna 'Unidades' a entero
    df['Unidades'] = pd.to_numeric(df['Unidades'], errors='coerce').fillna(0).astype(int)
    print("\nColumna'Unidades' convertida a entero:")
    print(df['Unidades'].head())

#Mostrar los tipos de variables de cada columna
    print("\nTipos de variables en cada columa:")
    print(df.info())

 # Retornar el dataset cargado
    return df
df_developers_info = cargar_dataset('ejemplo_data.csv')