import psycopg2


def recc():
    conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=12345")
    cur = conn.cursor()
    cur.execute("""
        SELECT  generos.id_genero, COUNT(generos.id_genero) 
        FROM    generos
        JOIN    genero_contenido ON genero_contenido.id_genero = generos.id_genero
        JOIN    multimedia ON multimedia.id = genero_contenido.id_contenido
        JOIN    historial ON historial.id_contenido = multimedia.id
        JOIN    perfil  ON  perfil.id = historial.id_perfil
        WHERE   perfil.id = historial.id_perfil
        AND     historial.id_contenido = multimedia.id
        GROUP BY    generos.id_genero
        ORDER BY    COUNT(generos.id_genero) DESC
        """)

    search_records = cur.fetchall()
    
    results = []
    
    for i in search_records:
        cur.execute("""
            SELECT  multimedia.nombre
            FROM    multimedia
            JOIN    genero_contenido ON genero_contenido.id_contenido = multimedia.id
            WHERE   id_genero = %(genre)s
        """, {
            'genre': i[0]
        })
        
        results_temp = cur.fetchall()
        for k in results_temp:
            results.append(k[0])
    
    for i in results:
        print(i)
        
    
    
    
recc()
