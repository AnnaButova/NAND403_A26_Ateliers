'''
À ce moment, tout le bar se tourna vers vous et votre ordinateur.
Aidez notre cowboy à commander son drink en lui bâtissant un outil pour afficher dans un tableau
les différents drinks à l'aide de PySide6.

'''
import sys
import json

json_file = sys.argv[1]
print("JSON FILE >>>> " + json_file)

try:
    file = open(json_file)
    data = json.load(file)
    print(type(data))
except:
    print(f"Could not load data from {json_file}")

for i in data:
    for k in i.keys():
        print({k})

#with open(json_file) as json_data:
#    data = json.load(json_data)
#    print(data)