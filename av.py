import requests
import os
import json

with open('list.json') as f:
    data = json.load(f)

files = []
cleanFiles = 0
infectedFiles = 0
totalFiles = 0

for file in os.listdir():
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


url = 'https://raw.githubusercontent.com/<username>/<reponame>/<branch>/<filepath>.json'
response = requests.get(url)
data = json.loads(response.text)

# Agora você pode acessar os dados do arquivo JSON como um objeto Python
print(data['key'])

print(
    f"{totalFiles} Ficheiros analisados, existem {cleanFiles} ficheiros limpos e {infectedFiles} ficheiros infetados!")
