#Imports
from variables import Items, saveFolder

from json import loads
from random import uniform as uni
from os import listdir, remove, path






#Functions
def filesFromFolder() -> list:
    global saveFolder
    return [file for file in listdir(saveFolder) if file.endswith('.bin')]



def saveCount() -> list:
    return len(filesFromFolder())



def ParseSave(file) -> list | bool:
    global saveFolder
    
    try:
        with open(f'{saveFolder}\\{file}', 'r', errors = 'ignore') as f:
            information = ''.join([line for line in f]).split('|')
            mainInformation = loads(information[1])
            return mainInformation
    except: return False



def RemoveSave(slot: int) -> bool:
    if not path.isfile(f'{saveFolder}\\Save{slot}.bin'): return False
    remove(f'{saveFolder}\\Save{slot}.bin')



def AddSave(slot: int, content: str) -> bool:
    try:
        with open(f'{saveFolder}\\Save{slot}.bin', 'w+', errors = 'ignore') as f: f.write(content)
    except: return False
    return True



def itemFromID(itemID: str) -> str:
    global Items
    return Items['ID'][itemID]



def itemFromName(itemName: str) -> str:
    global Items
    return Items['NAME'][itemName]



def generateOutsideItem(item) -> dict:
    return {
        'persistentID' : item,
        'posX' : uni(-10.0, 10.0),
        'posY' : 2.0,
        'poxZ' : uni(-10.0, 10.0),
        'rotX' : uni(1.0, -1.0),
        'rotY' : uni(1.0, -1.0),
        'rotZ' : uni(1.0, -1.0),
        'rotW' : uni(1.0, -1.0),
    }