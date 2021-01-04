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