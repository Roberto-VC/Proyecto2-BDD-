from cProfile import label
from matplotlib import container
import psycopg2
import tkinter as tk
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
import tkinter.font as tkFont
import vlc
import pafy
import time
import keyboard

from sympy import expand, false

conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
cur = conn.cursor()

def clear_entradas(event, entry):
    entry.delete(0, tk.END)

###Busqueda por Queries###
def busqueda_actores(busqueda):
    
    cur.execute("""
        SELECT 	nombre, links
        FROM	multimedia
        WHERE	multimedia.id IN(
            SELECT multimedia_id
            FROM actor_contenido
            WHERE actor_contenido.actor_id IN (
                SELECT id
                FROM actor
                WHERE nombre_completo = %(busqueda)s
            )
        );
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records


def busqueda_director(busqueda):
    cur.execute("""
    SELECT 	nombre, links
    FROM	multimedia
    WHERE	multimedia.id IN(
        SELECT multimedia_id
        FROM director_contenido
        WHERE director_contenido.id IN (
            SELECT id
            FROM director
            WHERE nombre_completo = %(busqueda)s
        )
    );
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records

def busqueda_categoria(busqueda):
    cur.execute("""
    SELECT 	nombre, links
    FROM	multimedia
    WHERE	multimedia.id IN(
        SELECT id_contenido
        FROM genero_contenido
        WHERE genero_contenido.id_genero IN (
            SELECT id_genero
            FROM generos
            WHERE nombre = %(busqueda)s
        )
    );
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records

def busqueda_entretenimiento(busqueda):
    cur.execute("""
    SELECT nombre,links
    FROM multimedia
    WHERE tipo_contenido = %(busqueda)s;
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records

def busqueda_premios(busqueda):
    cur.execute("""
    SELECT 	nombre, links
    FROM	multimedia
    WHERE	multimedia.id IN(
        SELECT multimedia_id
        FROM premios_contenido
        WHERE premios_contenido.id IN (
            SELECT id_premio
            FROM premios
            WHERE premio = %(busqueda)s
        )
    );
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records

def busqueda_estreno(busqueda):
    cur.execute("""
    SELECT nombre,links
    FROM multimedia
    WHERE EXTRACT(YEAR FROM fecha_estreno) = %(busqueda)s;
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records

def busqueda_nombre(busqueda):
    cur.execute("""
    SELECT nombre,links
    FROM multimedia
    WHERE nombre = %(busqueda)s;
    """, {
        'busqueda': busqueda
    })

    search_records = cur.fetchall()

    if search_records is None:
        print("No se ha encontrado ningun resultado")
        return False

    print(search_records)
    return search_records
###Fin de Busqueda por Queries###


#Busqueda de contenido por medio de queries
def busqueda(searchWindow, inputusuario, busqueda):

    listaBusqueda = []

    if busqueda == "":
        print("No se ha ingresado ningun valor")

    if inputusuario == "Actor":
        listaBusqueda = busqueda_actores(busqueda)
    elif inputusuario == "Director":
        listaBusqueda = busqueda_director(busqueda)
    elif inputusuario == "Categoria":
        listaBusqueda = busqueda_categoria(busqueda)
    elif inputusuario == "Tipo":
        listaBusqueda = busqueda_entretenimiento(busqueda)
    elif inputusuario == "Premio ganado":
        listaBusqueda = busqueda_premios(busqueda)
    elif inputusuario == "Fecha de estreno":
        listaBusqueda = busqueda_estreno(busqueda)
    elif inputusuario == "Nombre":
        listaBusqueda = busqueda_nombre(busqueda)
    else:
        print("No se ingreso un valor valido")

    count=0
    if not listaBusqueda:
        print("No se encontro ningun resultado :(")
    else:
        for widget in searchWindow.winfo_children():
            widget.destroy()

        for item in listaBusqueda:
            labelTitulo = tk.Label(searchWindow, text=item[0], bg='#ffe4e1')
            labelLink = tk.Button(searchWindow, text="Ver", bg='#ffe4e1', command=lambda x=item[1]:  visualizar(x)) #Temporal hasta reemplazar por boton
            labelTitulo.grid(row=count, column=0, padx=100, pady=5)
            labelLink.grid(row=count, column=1, padx=100)
            count = count + 1

#Visualizacion de contenido por medio de la libreria de VLC media player y pafy     
def visualizar(link):
    print(link)
    url=link
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    playing = True
    player.play()
    while True:
        if keyboard.read_key() == "s" and playing == True:
            player.pause()
            playing = False
        elif keyboard.read_key() == "p" and playing == False:
            player.play()
            playing == True
        elif keyboard.read_key() == "e":
            player.stop()
            print("Supposed to exit here")
            return False
            
#Interfaz de usuario de busqueda de contenido y visualizacion
def UI_busqueda():
    background = '#ffe4e1'
    foreground = '#79a1e0'
    #pastWindow.destroy()

    searchWindow = tk.Tk(className="Streameo (Working Title)")
    entryarea = tk.Canvas(searchWindow, width=750, height=650, bg=foreground)
    entryarea.place(relx=0.5, rely=0.5, anchor="center")
    searchFont = tkFont.Font(family="@MS UI Gothic", size=8, weight="bold" )

    #Render del logo de la aplicacion
    logoCanvas = tk.Canvas(searchWindow, width = 150, height = 150, highlightthickness=0, bg=foreground)
    logo = tk.PhotoImage(file="src/assets/streameologo.png")
    logoCanvas.create_image(130,10, anchor="ne", image=logo)
    logoCanvas.place(relx=0.49, rely=0.15, anchor="center")
    containerBusqueda = tk.Frame(searchWindow)
    
    resultadosBusqueda = tk.Canvas(containerBusqueda, width=600, height=300, bg=background)
    #resultadosBusqueda.pack()
    resultadosBusqueda.grid_propagate(false)
    resultadosBusqueda.pack_propagate(false)
    scrollbar = tk.Scrollbar(containerBusqueda, orient="vertical", command=resultadosBusqueda.yview)
    scrollable_frame = tk.Frame(resultadosBusqueda)
    scrollable_frame.configure(bg=background)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: resultadosBusqueda.configure(
            scrollregion=resultadosBusqueda.bbox("all")
        )
    )
    resultadosBusqueda.create_window((0,0), window=scrollable_frame, anchor="nw")
    resultadosBusqueda.configure(yscrollcommand=scrollbar.set)

    containerBusqueda.place(relx=0.5, rely=0.7, anchor="center")
    resultadosBusqueda.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    inputBusqueda = tk.Entry(entryarea, width=90)
    inputBusqueda.configure(bg=background)
    inputBusqueda.insert(0, "Busqueda...")
    inputBusqueda.bind("<Button-1>", lambda event: clear_entradas(event, inputBusqueda))
    inputBusqueda.place(relx=0.5, rely=0.28, anchor="center")

    opcionesBusqueda = ["Actor", "Director", "Categoria", "Tipo", "Premio ganado", "Fecha de estreno", "Nombre"]
    clicked = StringVar()
    clicked.set("Nombre")
    opcionesMenu = OptionMenu(searchWindow, clicked, *opcionesBusqueda)
    opcionesMenu.configure(bg=background)
    opcionesMenu.place(relx=0.4, rely=0.35, anchor="center")
    buscar = tk.Button(searchWindow, bg=background, width=8, height=3, text="Buscar", font=searchFont, command=lambda: busqueda(scrollable_frame, clicked.get(), inputBusqueda.get()))
    buscar.place(relx = 0.6, rely=0.35, anchor="center")

    favoritos = tk.Button(searchWindow, bg=background, width=15, height=3, text="Favoritos", font=searchFont)
    historial = tk.Button(searchWindow, bg=background, width=15, height=3, text="Historial", font=searchFont)
    recomendaciones = tk.Button(searchWindow, bg=background, width=15, height=3, text="Recomendaciones", font=searchFont)
    volver = tk.Button(searchWindow, bg=background, width=8, height=3, text="Volver", font=searchFont)
    favoritos.place(relx=0.3, rely=0.4)
    historial.place(relx=0.45, rely=0.4)
    recomendaciones.place(relx=0.6, rely=0.4)
    volver.place(relx=0.15, rely=0.05)

    #Configuraciones extra de ventana
    searchWindow.configure(bg=background)
    searchWindow.geometry("1000x700")
    searchWindow.resizable(False,False)
    searchWindow.mainloop()

UI_busqueda()

