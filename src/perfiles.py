
import psycopg2


usuario = input("Ingrese su usuario: ")


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
    print("1. Crear Nuevo Perfil")
    for x in range(perfiles):
        print(str(x+2) + ". " + result2[x][1])
    cursor.execute(f'''SELECT * FROM usuario INNER JOIN subscripcion ON usuario.nombre_usuario = subscripcion.usuario WHERE nombre_usuario = '{user}';''')
    result3 = cursor.fetchall()
    subscription = int(result3[0][6])
    opcion = int(input("Ingrese su opcion: \n"))
    if opcion == 1:
        if subscription == 1 and perfiles < 1:
            name = input("Ingrese el nombre del perfil:\n")
            cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{user}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
        elif subscription == 1 and perfiles >=1:
            print("Ya no puede crear perfiles. Debe de mejorar su cuenta")
        if subscription == 2 and perfiles < 4:
            name = input("Ingrese el nombre del perfil:\n")
            cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{user}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
        elif subscription == 2 and perfiles >=4:
            print("Ya no puede crear perfiles. Debe de mejorar su cuenta:\n")
        if subscription == 3 and perfiles < 8:
            name = input("Ingrese el nombre del perfil")
            cursor.execute(f'''INSERT INTO perfil(usuario, nombre, id, estado_vista, estado_perfil) VALUES ('{user}', '{name}', '{cantidad+1}', 'Activo', 'Activo'); ''')
        elif subscription == 3 and perfiles >=8:
            print("Ya no puede crear perfiles. Debe de mejorar su cuenta")
    else:
        if opcion > 0 and opcion <= perfiles+1:
            elegido = result2[opcion-2][1]
            print("El usario elegido fue " + elegido + "\n")
        else: 
            print("Ingrese un valor válido:\n")
    connection.commit()
    connection.close()

 


perfiles(usuario)






