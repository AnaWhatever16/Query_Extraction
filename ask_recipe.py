# Aplicacion Ask Recipe
import os
import json
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import PorterStemmer


#Obtener la pregunta por pantalla del usuario
print("Porfavor introduzca la búsqueda: " )
query = input()

#Tokenizacion y limpieza de la query
stemmer = PorterStemmer()
tokens = wordpunct_tokenize(query)
clean = [stemmer.stem(token) for token in tokens
                 if all(c.isalnum() for c in token)
                 ]

print("tokens: ", clean)

#Carga de los archivos json
# f1 = open(os.getcwd() + "/Documentos/arbol_hojaldre.json")
# f2 = open(os.getcwd() + "/Documentos/panettone.json")
# data1 = json.load(f1)
# data2 = json.load(f2)


path = listdir(os.getcwd() + "/Documentos/")
query_receta = ""

for doc in path:
    receta = open(doc)
    datos = json.load(receta)
    for token in clean:
        if token == datos["id"]:
            query_receta = doc

for token in clean:
    if token == "dificil":
        
    elif token == "facil":
    elif token == "es" or token == "son":
    elif token == "media":
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == "dificultad":
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :
    elif token == :


#Asumimos que si no aparece la id de ninguna de las recetas en la query se está preguntando por nombres de recetas
if query_receta == "": 
    

