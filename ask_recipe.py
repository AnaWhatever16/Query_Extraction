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

s_token = "".join([" "+i if not i.startswith("'") else i for i in clean]).strip()

print("tokens: ", s_token)

dirpath = os.listdir(os.getcwd() + "/Documentos/")

resultados = []
#Se ha separado las preguntas en dos clases: el usuario busca el nombre de la receta,
#es decir, una id, no aparece, en cambio, si aparece una id, el usuario esta buscando datos
#especificos de una receta

for name_file in dirpath:
    if name_file[:-5] in query: #El usuario busca datos específicos de una receta
        flag_receta_unica = True
        print("EXITOOOOO")


#El usuario busca el nombre de una o varias receta/s porque ha dado datos

if flag_receta_unica == False
    if "facil"in s_token or "dificil"in s_token or "media"in s_token or "alta"in s_token or "baja"in s_token
    
    receta = open(doc)
    datos = json.load(receta)

