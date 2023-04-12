import os
import json
import requests

url = 'https://raw.githubusercontent.com/SorenKazam/NOSAV/main/list.json'
response = requests.get(url)
data = json.loads(response.text)

files = []
cleanFiles = 0
infectedFiles = 0
totalFiles = 0

for file in os.listdir("folder/"):  # aqui é a pasta que ira ser analisado
    print(f"Examinando ficheiro: {file}")
    if file == "av.py":
        continue
    files.append(file)

for file in files:
    for item in data:
        if item['name'] == file:
            print(
                f"O arquivo {file} existe na lista JSON tipo: {item['type']}.")
            infectedFiles += 1
            totalFiles += 1
            break
    else:
        print(f"O arquivo {file} não existe na lista JSON.")
        cleanFiles += 1
        totalFiles += 1

print(
    f"{totalFiles} Ficheiros analisados, existem {cleanFiles} ficheiros limpos e {infectedFiles} ficheiros infetados!")
