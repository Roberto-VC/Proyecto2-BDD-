from create_account import *
from login import *
from selectprofile import *
from busqueda_contenido import *

def main():
    run = True
    while run: 
        print("---Bienvenido a Streameo (Working title)---")
        print("--Seleccione una opcion--\n")
        print("1. Login")
        print("2. Signup")
        print("3. Salir\n")

        inputmenuprincipal = input("\nOpcion: ")
        if inputmenuprincipal == "1":
            inputusuario = input("Ingrese su usuario: ")
            inputcontraseña = input("Ingrese su contraseña: ")
            if loginInfo(inputusuario, inputcontraseña):
                print("\nSe ha logrado loguear al sistema\n")
            else:
                print("\nNo se ha logrado loguear al sistema\n")
        elif inputmenuprincipal == "2":
            signup()
        elif inputmenuprincipal == "3":
            print("\nSaliendo del programa...")
            run = False
        else:
            print("\nIngreso una opcion invalida\n")

main()