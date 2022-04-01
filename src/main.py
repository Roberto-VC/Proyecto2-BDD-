from create_account import *
from login import *
from busqueda_contenido import *
from perfiles import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont


background = '#ffe4e1'
foreground = '#79a1e0'

def renderLogin():
    botonlogin.place_forget()
    botonsignup.place_forget()
    botonsalir.place_forget()
    inputUsuario.delete(0, tk.END)
    inputUsuario.insert(0, "Usuario")
    inputUsuario.place(relx=0.5, rely=0.2, anchor="center")
    inputContra.delete(0, tk.END)
    inputContra.insert(0, "Contraseña")
    inputContra.place(relx=0.5, rely=0.4, anchor="center")
    volverMenu.place(relx=0.07, rely=0.7, anchor="w")
    loguearse.place(relx=0.92, rely=0.7, anchor="e")

    entryarea.configure(width=200, height=150)

def renderStart():
    inputUsuario.place_forget()
    inputContra.place_forget()
    volverMenu.place_forget()
    loguearse.place_forget()
    botonlogin.place(relx=0.5, rely=0.2, anchor="center")
    botonsignup.place(relx=0.5, rely=0.5, anchor="center")
    botonsalir.place(relx=0.5, rely=0.8, anchor="center")
    entryarea.configure(width=350, height=300)

def clear_entradas(event, entry):
    entry.delete(0, tk.END)
    if entry == inputContra:
        entry.configure(show="*")

def logueandose(usuario, contraseña):
    nombreuser = usuario.get()
    contra = contraseña.get()
    if loginInfo(nombreuser, contra):
        mensajelogin= f"Bienvenido {nombreuser}!"
        tk.messagebox.showinfo("Login", mensajelogin)
    else:
        tk.messagebox.showwarning("Login", "No te has logrado loguear")

window = tk.Tk(className="Streameo (Working title)")

botonesFont = tkFont.Font(family="@MS UI Gothic", size=16, weight="bold" )
loginFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )

#Render del logo de la aplicacion
logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
logo = tk.PhotoImage(file="src/assets/streameologo.png")
logoCanvas.create_image(130,10, anchor="ne", image=logo)
logoCanvas.place(relx=0.49, rely=0.15, anchor="center")

#Area de inicio, con botones para ir a login, sign up y salir de la aplicacion
entryarea = tk.Canvas(window, width=350, height=300, bg=foreground)
entryarea.place(relx=0.5, rely=0.62, anchor="center")

botonlogin = tk.Button(entryarea, bg=background, width=20, height=3, text="Login", font=botonesFont, command=lambda: renderLogin())
botonlogin.place(relx=0.5, rely=0.2, anchor="center")

botonsignup = tk.Button(entryarea, bg=background, width=20, height=3, text="Sign Up", font=botonesFont)
botonsignup.place(relx=0.5, rely=0.5, anchor="center")

botonsalir = tk.Button(entryarea, bg=background, width=20, height=3, text="Exit", font=botonesFont, command=window.destroy)
botonsalir.place(relx=0.5, rely=0.8, anchor="center")


#Area de login
inputUsuario = tk.Entry(entryarea, width=30)
inputUsuario.bind("<Button-1>", lambda event: clear_entradas(event, inputUsuario))
inputContra = tk.Entry(entryarea, width=30)
inputContra.bind("<Button-1>", lambda event: clear_entradas(event, inputContra))
volverMenu = tk.Button(entryarea, bg=background, width=10, height=2, text="Volver", font=loginFont, command=lambda: renderStart())
loguearse = tk.Button(entryarea, bg=background, width=10, height=2, text="Login", font=loginFont, command=lambda: logueandose(inputUsuario, inputContra))

#Configuraciones extra de ventana
window.configure(bg=background)
window.geometry("900x500")
window.resizable(False,False)
window.mainloop()



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
                print("--Menu de selección de perfiles--")
                perfiles(inputusuario)
            else:
                print("\nNo se ha logrado loguear al sistema\n")
        elif inputmenuprincipal == "2":
            signup()
        elif inputmenuprincipal == "3":
            print("\nSaliendo del programa...")
            run = False
        else:
            print("\nIngreso una opcion invalida\n")
