import csv
import os
path = r"S:\Progamación\TG\Archivos\Reviews.csv\Reviews.csv"
if not os.path.exists(path):
    print(f"Error: El archivo no existe en {path}")
    exit()
file_name = "Reviews.csv"
id = []
ProductId = []
userId = []
ProfileName = []
HelpfulnessNumerator = []
HelpfulnessDenominator = []
Score = []
Time = []
Summary = []
Text = []
#Aqui se supone ya esta subido el archivo obtenido de la pagina de Kaggle
#https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews?resource=download
with open(path, 'r', encoding='utf-8') as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')
  next(readCSV)
  for row in readCSV:
    if len(row) >= 10:
      id.append(row[0])
      ProductId.append(row[1])
      userId.append(row[2])
      ProfileName.append(row[3])
      HelpfulnessNumerator.append(row[4])
      HelpfulnessDenominator.append(row[5])
      Score.append(row[6])
      Time.append(row[7])
      Summary.append(row[8])
      Text.append(row[9])
      #Para comrprobar si el archivo se subio correctamente ejecutar el siguiente comentario
      #una pizza de Pepperoni al Jorge")
      #Se va a repetir cada que el ciclo for sea exitoso por dato (Unas 5400 veces xd)
#Hasta aqui ya se supone esta subi e indexado el codigo
#Si lo quieren imprimir (Bajo su riesgo y su ram) Ejecuten el siguiente codigo
    else:
      print(f"Skipping malformed row due to insufficient columns: {row}") # Log malformed rows
#
#
#  print(id)
#  print(ProductId)
#  print(userId)
#  print(ProfileName)
#  print(HelpfulnessNumerator)
#  print(HelpfulnessDenominator)
#  print(Score)
#  print(Time)
#  print(Summary)
#  print(Text)
#Con esto dare por terminada la secion del 16 de Nov del 2025. Si añaden algo, porfi con comentario todo. Mantengamos orden xd
#
#
#outputs que nos sirven para las vainas que pide xd, hoy no quiero trabajar 
print(f"\n=== RESUMEN DE DATOS CARGADOS ===")
print(f"Total de registros: {len(id)}")
print(f"Total de usuarios {len(set(userId))}")
print(f"ProductIds únicos: {len(set(ProductId))}")
print(f"Rango de puntuaciones: {min(Score)} - {max(Score)}")