# Aplicacion Ask Recipe
import os
import json
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import PorterStemmer

###############
#    FLAGS    #
###############

flag_receta_unica = False




##################
#    PROGRAMA    #
##################

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


dirpath = os.listdir(os.getcwd() + "/Documentos/")
query_receta = ""

resultados = []
#Se ha separado las preguntas en dos clases: el usuario busca el nombre de la receta,
#es decir, una id, no aparece, en cambio, si aparece una id, el usuario esta buscando datos
#especificos de una receta

for name_file in dirpath:
    if name_file[:-5] in query: #El usuario busca datos específicos de una receta
        flag_receta_unica
        print("EXITOOOOO")


#El usuario busca el nombre de una o varias receta/s porque ha dado datos


    receta = open(doc)
    datos = json.load(receta)

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
    
"""
