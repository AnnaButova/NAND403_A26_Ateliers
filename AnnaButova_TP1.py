import os
import json
import sys
from pathlib import Path

# Imports for UI
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
) 

# Find the json files ----------------------
path_small = Path("data_small.json")
path_large = Path("data_large.json")

if path_small.exists() or path_large.exists():
    print("I HAVE BEEN FOUND")
else:
    print("LOL NOPE")
# ------------------------------------------

# Open json file as an array ---------------
with open("data_small.json", "r", -1, "utf-8") as json_file_small:
    data_json_small = json.load(json_file_small)
# ------------------------------------------


for i in data_json_small:
    for id in i.keys():
        print ({id})
        
    for value in i.values():
        print({value})

print(data_json_small)

