import psycopg2


def recc(id_perfil):
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
    cur = conn.cursor()
    cur.execute("""
        SELECT  generos.id_genero, COUNT(generos.id_genero) 
        FROM    generos
        JOIN    genero_contenido ON genero_contenido.id_genero = generos.id_genero
        JOIN    multimedia ON multimedia.id = genero_contenido.id_contenido
        JOIN    historial ON historial.id_contenido = multimedia.id
        JOIN    perfil  ON  perfil.id = historial.id_perfil
        WHERE   %(id_perfil)s = historial.id_perfil
        AND     historial.id_contenido = multimedia.id
        GROUP BY    generos.id_genero
        ORDER BY    COUNT(generos.id_genero) DESC
        """, {
            'id_perfil': id_perfil
        })

    search_records = cur.fetchall()
    
    
    movie_id = []
    
    for i in search_records:
        cur.execute("""
            SELECT  multimedia.id, multimedia.links
            FROM    multimedia
            JOIN    genero_contenido ON genero_contenido.id_contenido = multimedia.id
            WHERE   id_genero = %(genre)s
            LIMIT 10
        """, {
            'genre': i[0]
        })
        
        
        id_link = cur.fetchall()
        for k in id_link:
            movie_id.append(k[0])
    
    for i in movie_id:
        print(i)
        
    #id_link -> array con array de id de pelicula y link
    #movie_id -> lista de id de peliculas
        
    
    
    
recc("6")
