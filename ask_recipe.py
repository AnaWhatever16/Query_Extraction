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

print("\n---------------------------------------------------------------------------------\n")
print("En este programa puede preguntar sobre los siguientes tipos de informacion sobre recetas:")
print(" --> Nombres de receta segun sus caracteristicas (enumeradas abajo)")
print(" --> Dificultad")
print(" --> Tiempo de preparacion")
print(" --> Raciones")
print(" --> Coste por persona") # EXPLICAR TEMA PRECIOS
print(" --> Calorias")
print(" --> Ingredientes")
print(" --> Preparacion (incluido los bloques de pasos)")

print("\nPresione ENTER despues de escribir su pregunta.")

while(True):
    print("\n---------------------------------------------------------------------------------\n")
    #Obtener la pregunta por pantalla del usuario
    print("Porfavor introduzca la busqueda (Ctrl + C para salir): " )
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
        if name_file[:-5] in query: #El usuario busca datos especificos de una receta
            flag_receta_unica = True
            datos = open(os.getcwd() + "/Documentos/" + name_file)
            receta = json.load(datos)


            #### TIEMPO DE PREPARACION ####
            if ("tiempo" in s_token or "tarda" in s_token or "minuto" in s_token or "min" in s_token):
                print("La receta " + receta["Nombre_receta"] + " tiene un tiempo de preparación de" + str(receta["Tiempo_preparacion"]) + " minutos")

            #### PRECIO ####
            elif ("cuesta" in s_token or "precio" in s_token or "dinero" in s_token):
                print("La receta " + receta["Nombre_receta"] + " cuesta " + str(receta["Precio"]) +"€/persona")

            #### DIFICULTAD ###
            elif("dificultad" in s_token or "dificil" in s_token or "facil" in s_token):
                print("La receta " + receta["Nombre_receta"] + " tiene dificultad " + receta["Dificultad"])
            
            #### RACIONES ####
            elif ("racion" in s_token or "plato" in s_token or "porcion" in s_token or "persona" in s_token):
                print("La receta " + receta["Nombre_receta"] + " tiene cantidad para " + str(receta["Raciones"]) + " raciones")

            #### CALORIAS ####
            elif("caloria" in s_token or "kcal" in s_token or "kilocaloria" in s_token or "cal" in s_token):
                print("La receta " + receta["Nombre_receta"] + " tiene cantidad para " + str(receta["Calorias_por_100g"]) + " kcal/100g")
            

            break

        

####################################################################################################################################
    #El usuario busca el nombre de una o varias receta/s porque ha dado datos
    if flag_receta_unica == False:
        for doc in dirpath:
            datos = open(os.getcwd() + "/Documentos/" + doc)
            receta = json.load(datos)

            # PARA PREGUNTAS NUMERICAS #
            if ("super" in s_token or "superen" in s_token or "superan" in s_token):
                valor = [int(s) for s in s_token.split() if s.isdigit()]
                if(valor):
                    if(valor[0]==0):
                        if("no" in s_token):   
                            if(receta["Precio"] <= valor[1]*0.1):
                                print(receta["Nombre_receta"] + " | Precio: " + str(receta["Precio"]) + "€/persona")
                        else:
                            if(receta["Precio"] > valor[1]*0.1):
                                print(receta["Nombre_receta"] + " | Precio: " + str(receta["Precio"]) + "€/persona")
                    
                    elif ("minuto" in s_token or "min" in s_token):
                        if("no" in s_token):
                            if(receta["Tiempo_preparacion"] <= valor[0]):
                                print(receta["Nombre_receta"] + " | Tiempo: " + str(receta["Tiempo_preparacion"]) + "minutos")
                        else:
                            if(receta["Tiempo_preparacion"] > valor[0]):
                                print(receta["Nombre_receta"] + " | Tiempo: " + str(receta["Tiempo_preparacion"]) + "minutos")
                    
                    elif ("racion" in s_token or "plato" in s_token or "porcion" in s_token or "persona" in s_token):
                        if("no" in s_token):
                            if(receta["Raciones"] <= valor[0]):
                                print(receta["Nombre_receta"] + " | Raciones: " + str(receta["Raciones"]))
                        else:
                            if(receta["Raciones"] > valor[0]):
                                print(receta["Nombre_receta"] + " | Raciones: " + str(receta["Raciones"]))
                    
                    elif ("caloria" in s_token or "kcal" in s_token or "kilocaloria" in s_token or "cal" in s_token):
                        if("no" in s_token):
                            if(receta["Calorias_por_100g"] <= valor[0]):
                                print(receta["Nombre_receta"] + " | Calorias: " + str(receta["Calorias_por_100g"]) + "kcal/100g")
                        else:
                            if(receta["Calorias_por_100g"] > valor[0]):
                                print(receta["Nombre_receta"] + " | Calorias: " + str(receta["Calorias_por_100g"]) + "kcal/100g")
                    
                    else:
                        print("Por favor, si va a usar numeros no los escriba con letras.")
                        break
            
            ### CALORIAS ###
            elif("caloria" in s_token or "kcal" in s_token or "kilocaloria" in s_token or "cal" in s_token):
                calorias = [int(s) for s in s_token.split() if s.isdigit()]
                if (calorias):
                    if ("meno" in s_token or "menor" in s_token):
                        if(receta["Calorias_por_100g"] < calorias[0]):
                            print(receta["Nombre_receta"] + " | Calorias: " + str(receta["Calorias_por_100g"]) + "kcal/100g")
                    elif ("ma" in s_token or "mayor" in s_token):
                        if(receta["Calorias_por_100g"] > calorias[0]):
                            print(receta["Nombre_receta"] + " | Calorias: " + str(receta["Calorias_por_100g"]) + "kcal/100g")
                    else:
                        if(receta["Calorias_por_100g"] == calorias[0]):
                            print(receta["Nombre_receta"] + " | Calorias: " + str(receta["Calorias_por_100g"]) + "/100g")
                else:
                    print("Por favor, si va a usar numeros no los escriba con letras.")
                    break


            #### PRECIO ####
            elif("coste" in s_token or "precio" in s_token or "valor" in s_token or "cuesten" in s_token or "cuestan" in s_token):
                euros = [int(s) for s in s_token.split() if s.isdigit()]
                if (euros):
                    if ("meno" in s_token or "inferior" in s_token):
                        if(receta["Precio"] < euros[1]*0.1):
                            print(receta["Nombre_receta"] + " | Precio: " + str(receta["Precio"]) + "€/persona")
                    elif ("ma" in s_token or "superior" in s_token):
                        if(receta["Precio"] > euros[1]*0.1):
                            print(receta["Nombre_receta"] + " | Precio: " + str(receta["Precio"]) + "€/persona")
                    else:
                        if(receta["Precio"] == euros[1]*0.1):
                            print(receta["Nombre_receta"] + " | Precio: " + str(receta["Precio"]) + "€/persona")
                else:
                    print("Por favor, si va a usar numeros no los escriba con letras.")
                    break

            #### RACIONES ####
            elif("racion" in s_token or "plato" in s_token or "porcion" in s_token or "persona" in s_token):
                racion = [int(s) for s in s_token.split() if s.isdigit()]
                if (racion):
                    if ("meno" in s_token or "menor" in s_token):
                        if(receta["Raciones"] < racion[0]):
                            print(receta["Nombre_receta"] + " | Raciones: " + str(receta["Raciones"]) )
                    elif ("ma" in s_token or "mayor" in s_token):
                        if(receta["Raciones"] > racion[0]):
                            print(receta["Nombre_receta"] + " | Raciones: " + str(receta["Raciones"]) )
                    else:
                        if(receta["Raciones"] == racion[0]):
                            print(receta["Nombre_receta"] + " | Raciones: " + str(receta["Raciones"]) )
                else:
                    print("Por favor, si va a usar numeros no los escriba con letras.")
                    break

            #### TIEMPO DE PREPARACION ####
            elif ("minuto" in s_token or "min" in s_token) :
                mins = [int(s) for s in s_token.split() if s.isdigit()]
                if (mins):
                    if ("meno" in s_token or "inferior" in s_token):
                        if(receta["Tiempo_preparacion"] < mins[0]):
                            print(receta["Nombre_receta"] + " | Tiempo: " + str(receta["Tiempo_preparacion"]) + " minutos")
                    elif ("ma" in s_token or "superior" in s_token):
                        if(receta["Tiempo_preparacion"] > mins[0]):
                            print(receta["Nombre_receta"]  + " | Tiempo: " + str(receta["Tiempo_preparacion"]) + " minutos")
                    else: 
                        if(receta["Tiempo_preparacion"] == mins[0]):
                            print(receta["Nombre_receta"]  + " | Tiempo: " + str(receta["Tiempo_preparacion"]) + " minutos")
                else:
                    print("Por favor, si va a usar numeros no los escriba con letras.")
                    break
            
            #### DIFICULTAD ####
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
                break