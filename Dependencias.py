# Autores: Ana Maria Casado y Ana Sanmartin
## Este script instala en el sistema todas las dependencias necesarias para poderejecutar los programas

# Paquetes necesarios para el funcionamiento del programa
import os


#Lista de paquetes a instalar
dependencies = ['nltk', 'Unidecode']

#Instalacion del comando pip3
os.system("sudo apt update")
os.system("sudo install python3-pip")

for s in dependencies:
    os.system("pip3 install " + s)
