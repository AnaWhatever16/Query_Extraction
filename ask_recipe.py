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
print("################################# \n")
print("#    BIENVENIDO A ASK RECIPE    # \n")
print("#################################")

while(True):
    print("\n---------------------------------------------------------------------")
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
        


    #El usuario busca el nombre de una o varias receta/s porque ha dado datos
    if flag_receta_unica == False:
        for doc in dirpath:
            datos = open(os.getcwd() + "/Documentos/" + doc)
            receta = json.load(datos)

            if ("minuto" in s_token or "min" in s_token) :
                mins = 0
                mins = [int(s) for s in s_token.split() if s.isdigit()]
                if (mins):
                    if ("meno" in s_token):
                        if(receta["Tiempo_preparacion"] < mins[0]):
                            print(receta["Nombre_receta"] + " | Tiempo: " + str(receta["Tiempo_preparacion"]))
                    elif ("ma" in s_token):
                        if(receta["Tiempo_preparacion"] > mins[0]):
                            print(receta["Nombre_receta"]  + " | Tiempo: " + str(receta["Tiempo_preparacion"]))
                    else:
                        if(receta["Tiempo_preparacion"] == mins[0]):
                            print(receta["Nombre_receta"]  + " | Tiempo: " + str(receta["Tiempo_preparacion"]))
                else:
                    print("Por favor, si va a usar números no los escriba con letras.")
                    break
                
            elif ("facil" in s_token or "baja" in s_token):
                if ("no" in s_token):
                    if (receta["Dificultad"] == "dificil"):
                        print(receta["Nombre_receta"] + " |  Dificultad: " + receta["Dificultad"])
                else:
                    if (receta["Dificultad"] == "facil"):
                        print(receta["Nombre_receta"] + " |  Dificultad: " + receta["Dificultad"])

            elif ("dificil" in s_token or "alta" in s_token):
                if ("no" in s_token):
                    if (receta["Dificultad"] == "facil"):
                        print(receta["Nombre_receta"] + "Dificultad: " + receta["Dificultad"])
                else:
                    if (receta["Dificultad"] == "dificil"):
                        print(receta["Nombre_receta"] + " |  Dificultad: " + receta["Dificultad"])
            else:
                print("La pregunta no se reconoce, vuelva a intentarlo")