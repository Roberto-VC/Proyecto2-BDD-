
import psycopg2

from tkinter import *
import tkinter.font as tkFont

background = '#ffe4e1'
foreground = '#79a1e0'



usuario = input("Ingrese su usuario: ")
window = Tk(className="Streameo (Working title)")
window.title("Register")

botonesFont = tkFont.Font(family="@MS UI Gothic", size=16, weight="bold" )
loginFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )

def click():
    connection = psycopg2.connect(database="proyecto2", user="postgres", password="videogamesfan10", host="localhost", port=5432)
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM perfil''')
    cantidad = cursor.fetchall()
    cantidad = cantidad[0][0]
    cursor.execute(f'''SELECT COUNT(*) FROM perfil WHERE usuario = '{usuario}';''')
    result1 = cursor.fetchall()
    perfiles = int(result1[0][0])
    cursor.execute(f'''SELECT * FROM perfil WHERE usuario = '{usuario}';''')
    result2 = cursor.fetchall()
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{usuario}';''')
    result3 = cursor.fetchall()
    subscription = int(result3[0][6])
    if subscription == 1 and perfiles < 1:
        name = input("Ingrese el nombre del perfil:\n")
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{user}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 1 and perfiles >=1:
        print("Ya no puede crear perfiles. Debe de mejorar su cuenta.\n")
    if subscription == 2 and perfiles < 4:
        name = input("Ingrese el nombre del perfil:\n")
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{user}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 2 and perfiles >=4:
        print("Ya no puede crear perfiles. Debe de mejorar su cuenta.\n")
    if subscription == 3 and perfiles < 8:
        name = input("Ingrese el nombre del perfil")
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{user}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 3 and perfiles >=8:
        print("Ya no puede crear perfiles. Debe de mejorar su cuenta.\n")

def select(X):
    connection = psycopg2.connect(database="proyecto2", user="postgres", password="videogamesfan10", host="localhost", port=5432)
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM perfil''')
    cantidad = cursor.fetchall()
    cantidad = cantidad[0][0]
    cursor.execute(f'''SELECT COUNT(*) FROM perfil WHERE usuario = '{usuario}';''')
    result1 = cursor.fetchall()
    perfiles = int(result1[0][0])
    cursor.execute(f'''SELECT * FROM perfil WHERE usuario = '{usuario}';''')
    result2 = cursor.fetchall()
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{usuario}';''')
    result3 = cursor.fetchall()
    print(result3[0][6])
    subscription = int(result3[0][6])
    print(X)
    elegido = result2[X][1]
    print("El usario elegido fue " + elegido + "\n")
    cursor.execute(f'''SELECT * FROM favoritos WHERE perfil_id = '{result2[X][2]}';''')
    result4 = cursor.fetchall()
    print(f"Contenido Visto:\n {result4}")



def perfiles(user):
    connection = psycopg2.connect(database="proyecto2", user="postgres", password="videogamesfan10", host="localhost", port=5432)
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM perfil''')
    cantidad = cursor.fetchall()
    cantidad = cantidad[0][0]
    cursor.execute(f'''SELECT COUNT(*) FROM perfil WHERE usuario = '{user}';''')
    result1 = cursor.fetchall()
    perfiles = int(result1[0][0])
    cursor.execute(f'''SELECT * FROM perfil WHERE usuario = '{user}';''')
    result2 = cursor.fetchall()
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{user}';''')
    result3 = cursor.fetchall()
    print(result3[0][6])
    subscription = int(result3[0][6])
    window.geometry("300x350")
    l = Label(window, text = "Seleccione!")
    l.config(font =("Courier", 14))
    window.configure(bg=foreground)
    l.pack()
    e=Button(window, text="Crear Nuevo Perfil", command=click, height = 3, width = 20, bg=background, font=botonesFont)
    e.pack()
    for x in range(perfiles):
        e=Button(window, text=result2[x][1], command= lambda x=x: select(x), height = 3, width = 20, bg=background, font=botonesFont)
        e.pack()
    window.mainloop()
    connection.commit()
    connection.close()

 


perfiles(usuario)







