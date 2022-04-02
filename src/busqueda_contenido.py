import psycopg2
import bcrypt

conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
cur = conn.cursor()

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

    """
    SELECT 	nombre, links
    FROM	multimedia
    WHERE	multimedia.id IN(
        SELECT multimedia_id
        FROM actor_contenido
        WHERE actor_contenido.actor_id IN (
            SELECT id
            FROM actor
            WHERE nombre_completo = 'Juanito Perez'
        )
    );
    """

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

    """
    SELECT 	nombre, links
    FROM	multimedia
    WHERE	multimedia.id IN(
        SELECT multimedia_id
        FROM director_contenido
        WHERE director_contenido.id IN (
            SELECT id
            FROM director
            WHERE nombre_completo = 'Brian de Palmas'
        )
    );
    """

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


    """
    SELECT 	nombre, links
    FROM	multimedia
    WHERE	multimedia.id IN(
        SELECT id_contenido
        FROM genero_contenido
        WHERE genero_contenido.id_genero IN (
            SELECT id_genero
            FROM generos
            WHERE nombre = 'Acción'
        )
    );
    """

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

    """
    SELECT nombre,links
    FROM multimedia
    WHERE tipo_contenido = 'Pelicula';
    """

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


    """
    SELECT 	nombre, links
    FROM	multimedia
    WHERE	multimedia.id IN(
        SELECT multimedia_id
        FROM premios_contenido
        WHERE premios_contenido.id IN (
            SELECT id_premio
            FROM premios
            WHERE premio = 'Sindicato de Productores'
        )
    );
    """

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


    """
    SELECT nombre,links
    FROM multimedia
    WHERE EXTRACT(YEAR FROM fecha_estreno) = '1996';
    """


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
    """
    SELECT nombre,links
    FROM multimedia
    WHERE nombre = 'Mision Imposible';
    """

def main_busqueda():
    print("Busqueda de contenido:\n")
    print("Eliga una opcion valida para filtrar la busqueda: ")
    print("1. Por nombre de actor")
    print("2. Por nombre de director")
    print("3. Por tipo de categoria (Genero)")
    print("4. Por titpo de entretenimiento (Pelicula, serie, etc)")
    print("5. Por nombre de premios ganados")
    print("6. Por fecha de estreno (Año)")
    print("7. Por nombre")

    inputusuario = int(input("Seleccione su opcion"))

    if inputusuario == 1:
        busqueda = input("Que actor busca?")
        busqueda_actores(busqueda)
    elif inputusuario == 2:
        busqueda = input("Que director busca?")
        busqueda_director(busqueda)
    elif inputusuario == 3:
        busqueda = input("Que categoria busca?")
        busqueda_categoria(busqueda)
    elif inputusuario == 4:
        busqueda = input("Que tipo de entretenimiento busca?")
        busqueda_entretenimiento(busqueda)
    elif inputusuario == 5:
        busqueda = input("Que premio ganado busca?")
        busqueda_premios(busqueda)
    elif inputusuario == 6:
        busqueda=input("Que fecha de estreno busca?")
        busqueda_estreno(busqueda)
    elif inputusuario == 7:
        busqueda = input("Que contenido busca?")
        busqueda_nombre(busqueda)
    else:
        print("Opcion invalida seleccionada")
    
main_busqueda()