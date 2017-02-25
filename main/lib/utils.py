import os
import json

# Returns all files in the specified folder and child folders
def getFiles(path):
    for (dirpath, _, filenames) in os.walk(path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def saveData(nFile, data):
    target = open(nFile, 'w')
    target.write(data)
    target.close()
    return target

#Open file. Return info
def openFile(fName):
    with open(fName) as dFile:
        data = json.load(dFile)
    return data

def retUpTo(data, idx):
    if len(data) < idx:
        return data
    return data[:idx]
