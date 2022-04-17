
import psycopg2

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from busqueda_contenido import *

background = '#ffe4e1'
foreground = '#79a1e0'
root = Tk()
mf = Frame(root)
mc = Canvas(mf, width=400, height=500,)
mc.grid_propagate(False)
mc.pack_propagate(False)
ms = ttk.Scrollbar(mf, orient=VERTICAL, command=mc.yview)
window = Frame(mc)

botonesFont = tkFont.Font(family="@MS UI Gothic", size=16, weight="bold" )
loginFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )

usuario = ""
def setUsuario(usuarioinput):
    global usuario

    usuario = usuarioinput

def nuevo():
    for widgets in window.winfo_children():
      widgets.destroy()
    window.entry = Entry(window)
    window.entry.pack(padx=0, pady=0)
    window.entry.configure(highlightbackground=foreground)
    window.e=Button(window, text="Aceptar", command=click, height = 3, width = 20, bg=background, font=botonesFont)
    window.e.pack()
    window.e=Button(window, text="Volver", command=perfiles, height = 3, width = 20, bg=background, font=botonesFont)
    window.e.pack()
    window.mainloop()



def click():
    name = window.entry.get()
    connection = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
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
    for widgets in window.winfo_children():
      widgets.destroy()
    if subscription == 1 and perfiles < 1:
        l = Label(window, text = "Nuevo Perfil Añadido!")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{usuario}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 1 and perfiles >=1:
        l = Label(window, text = "Ya no puede crear perfiles. Debe de mejorar su cuenta.")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
    if subscription == 2 and perfiles < 4:
        l = Label(window, text = "Nuevo Perfil Añadido!")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
        print(name)
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{usuario}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 2 and perfiles >=4:
        l = Label(window, text = "Ya no puede crear perfiles. Debe de mejorar su cuenta.")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
    if subscription == 3 and perfiles < 8:
        l = Label(window, text = "Nuevo Perfil Añadido!")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
        cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{usuario}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
    elif subscription == 3 and perfiles >=8:
        l = Label(window, text = "Ha llegado a la mayor cantidad de perfiles disponibles.")
        l.config(font =("Courier", 14))
        window.configure(bg=foreground)
        l.pack()
    connection.commit()
    connection.close()
    
    window.e=Button(window, text="Volver", command=hola, height = 3, width = 20, bg=background, font=botonesFont)
    window.e.pack()
    window.mainloop()
    
def hola():
    for widgets in window.winfo_children():
      widgets.destroy()
    connection = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
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
    l = Label(window, text = "Seleccione!")
    l.config(font =("Courier", 14))
    window.configure(bg=foreground)
    l.pack()
    e=Button(window, text="Crear Nuevo Perfil", command=nuevo, height = 3, width = 20, bg=background, font=botonesFont)
    e.pack()
    for x in range(perfiles):
        e=Button(window, text=result2[x][1], command= lambda x=x: select(x), height = 3, width = 20, bg=background, font=botonesFont)
        e.pack()
    window.mainloop()
    connection.commit()
    connection.close()
    
def select(X):
    connection = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
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
    print("lol")
    elegido = result2[X][1]
    print("El usario elegido fue " + elegido + "\n")
    cursor.execute(f'''SELECT * FROM favoritos WHERE perfil_id = '{result2[X][2]}';''')
    result4 = cursor.fetchall()
    root.destroy()
    UI_busqueda(result2[X][2])
    #print(f"Contenido Visto:\n {result4}")



def perfiles():
    print(usuario)
    print("Usuario arriba")
    mf.pack(fill=BOTH, expand=1)
    window.bind('<Configure>', lambda e: mc.configure(scrollregion = mc.bbox("all")))
    mc.create_window((0,0), window=window, anchor = 'nw')
    mc.configure(yscrollcommand=ms.set)
    mf.place(relx =0.5, rely =0.5, anchor= "center")
    mc.pack(side='left', fill='both', expand = True)
    mc.config(bg=background)
    ms.pack(side=RIGHT, fill=Y)
    for widgets in window.winfo_children():
      widgets.destroy()
    connection = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
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
    root.geometry("420x500")
    l = Label(window, text = "Seleccione!")
    l.config(font =("Courier", 14))
    mc.configure(bg=foreground)
    l.config(bg=background)
    l.pack()
    e=Button(window, text="Crear Nuevo Perfil", command=nuevo, height = 3, width = 20, bg=background, font=botonesFont)
    e.pack()
    for x in range(perfiles):
        e=Button(window, text=result2[x][1], command= lambda x=x: select(x), height = 3, width = 20, bg=background, font=botonesFont)
        e.pack(side=TOP)
    window.mainloop()
    connection.commit()
    connection.close()









