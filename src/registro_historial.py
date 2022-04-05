import psycopg2
from datetime import date

conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
cur = conn.cursor()

def registrar_historial(id_contenido, id_perfil):
    fecha_visualizacion = date.today()
    cur.execute("""
        INSERT INTO historial (
	        id_contenido, fecha_visualizacion, capitulo, id_perfil
        )
        VALUES 
            (%(id_contenido)s, %(fecha_visualizacion)s, NULL, %(id_perfil)s)

    """, {
        'id_contenido': id_contenido,
        'fecha_visualizacion':fecha_visualizacion,
        'id_perfil': id_perfil
    })

    conn.commit()

    """
    INSERT INTO historial (
	    id_contenido, fecha_visualizacion, capitulo, id_perfil
    )
    VALUES 
	    ('', '', NULL, '')
    """

def UI_historial(usuario):
    return 0

#registrar_historial()