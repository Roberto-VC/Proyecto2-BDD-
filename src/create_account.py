import psycopg2
import bcrypt
import re

disallowedchars="!#$%&/()='-|;"

def signup():
    x = False
    while not x:
        username = str(input("Ingrese su usuario\n"))
        if set(username) & set(disallowedchars):
            print("No se permiten caracteres especiales")
            x = True
        email = str(input("Ingrese su correo\n"))
        if set(email) & set(disallowedchars):
            print("No se permiten caracteres especiales")
            x = True
        password = str(input("Ingrese su contrasena\n"))
        if set(password) & set(disallowedchars):
            print("No se permiten caracteres especiales")
            x = True
        state = "activo"
        
        #Hashing del password
        pass_byte = bytes(password, 'utf-8')
        hashed = bcrypt.hashpw(pass_byte, bcrypt.gensalt(10))
        hashed = hashed.decode("utf-8")
        

        
        conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
        cur = conn.cursor()
        cur.execute("INSERT INTO usuario (nombre_usuario, contraseña, correo, estado) values (%s, %s, %s, %s)",
                    (username, hashed, email, state))
                        
        x = True



    conn.commit() #Commit de las tablas a base de datos SQL
    conn.close()  #Cerrar la conexion

signup()



