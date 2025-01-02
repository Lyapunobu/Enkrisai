import os
import json

dataFile = 'data/users_data.json'

def saveData(data):
    with open(dataFile, 'w') as file:
        json.dump(data, file, indent=4)

def loadData():
    if os.path.exists(dataFile):
        with open(dataFile, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    else:
        os.makedirs(os.path.dirname(dataFile), exist_ok=True)
        with open(dataFile, 'w') as file:
            json.dump({}, file)
        return {}