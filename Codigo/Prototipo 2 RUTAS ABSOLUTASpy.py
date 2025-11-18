#Aqui solo cargamos y leemos el archivo. Sin las cosas que pide
#70% IA GENERATED - NO SE CONSIDERARA PARA LA PRESENTACION DEL TG
from pathlib import Path
import csv
import sys

#Use pathlib para que se pueda llamar al archivo sin necesidad de ruta xd
#Sys para terminar cuando me de la gana que termine 

#Aqui se llaman a los index
ids = []
ProductId = []
userId = []
ProfileName = []
HelpfulnessNumerator = []
HelpfulnessDenominator = []
Score = []
Time = []
Summary = []
Text = []

#Vamos a hacer con funciones pq es mas sencillos y para aprender bien xd

def procesar_csv_carpeta_diferente():
    # Call del archivo
    programa_dir = Path(__file__).parent
    carpeta_datos = programa_dir / "Archivos_TG"
    archivo_csv = carpeta_datos / "Reviews.csv"
    
    # Verificar que existe la carpeta
    if not carpeta_datos.exists():
        print(f"La carpeta {carpeta_datos} no existe en la carpeta")
        sys.exit()
    
    #Interfaz de verificacion seguramente lo quitemos o quien sabe
    print(f"Progama ubicado en: {programa_dir}")
    print(f"Carpeta buscada: {carpeta_datos}  Encontrado: {carpeta_datos.exists()}")
    print(f"Archivo .csv buscado: {archivo_csv}  Encontrado: {archivo_csv.exists()}")
   
    # Leer CSV
    try:
        filas_cargadas = 0
        with open(archivo_csv, 'r', encoding='utf-8') as file:
            readCSV = csv.reader(file, delimiter= ',')
            next(readCSV, None)
            for row in readCSV:
                if len(row) >= 10:
                    ids.append(row[0])
                    ProductId.append(row[1])
                    userId.append(row[2])
                    ProfileName.append(row[3])
                    HelpfulnessNumerator.append(row[4])
                    HelpfulnessDenominator.append(row[5])
                    #Cambie la de leer Score para indexe bien pq sabra dios pq no funcionaba
                    try:
                        Score.append(float(row[6]))
                    except:
                        Score.append(None)
                    Time.append(row[7])
                    Summary.append(row[8])
                    Text.append(row[9])
                    #Como estamos en ciclo try, debo poner un else
                else:
                    print(f"Skipping malformed row due to insufficient columns: {row}")
    except FileNotFoundError:
        print(f"El archivo {archivo_csv} no existe")
    except Exception as e:
        print(f"Error: {e}")
        sys.exist()
        

# Ejecutar
procesar_csv_carpeta_diferente()
print(f"\nRESUMEN DE DATOS CARGADOS")
print(f"Total de registros: {len(ids)}")
print(f"Total de usuarios {len(set(userId))}")
print(f"ProductIds únicos: {len(set(ProductId))}")
#esto indexa mejor las puntuaciones al hacerlo por lista nos servira si esq debemos dar solo las puntuaciones. 
puntuaciones_validas=[s for s in Score if s is not None]
if puntuaciones_validas:
    print(f"Rango de puntaciones {min(puntuaciones_validas)} - {max(puntuaciones_validas)}")
else:
    print(f"No hay puntuaciones cargadas en esta base de datos")    
