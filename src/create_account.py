import psycopg2


x = False
while not x:
    try:
        username = str(input("Ingrese su usuario\n"))
        email = str(input("Ingrese su correo\n"))
        password = str(input("Ingrese su contrasena\n"))
        state = "activo"
        
        print(username)
        print(email)
        print(password)
        
        conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=12345")
        cur = conn.cursor()
        cur.execute("INSERT INTO usuario (nombre_usuario, contraseña, correo, estado) values (%s, %s, %s, %s)",
                    (username, password, email, state))

                        
        x = True
    except Exception:
        print("\nEl usuario ya se encuentra registrado, intente de nuevo")




conn.commit() #Commit de las tablas a base de datos SQL
conn.close()  #Cerrar la conexion

  


