###############################################
#   login.py
###############################################
#   Universidad del Valle de Guatemala
#   Bases de datos 1
#   Proyecto 1
#   Presentado por:
#   Andres de la Roca
#   Jun Woo Lee
#   
#   Ver 1.0
###############################################
import psycopg2
import bcrypt

conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
cur = conn.cursor()

def loginInfo(usuario, contraseña):
    
    fetchLoginInfo_Query = "SELECT nombre_usuario,contraseña FROM usuario WHERE usuario.nombre_usuario = '{0}'".format(usuario)
    cur.execute(fetchLoginInfo_Query)
    login_records = cur.fetchall()

    if not login_records:
        print("No existe ese usuario")
        return False
    contraseñaSQL = login_records[0][1]
    contraseña = bytes(contraseña, 'utf-8') 
    contraseñaSQL = bytes(contraseñaSQL, 'utf-8')
    if bcrypt.hashpw(contraseña, contraseñaSQL) == contraseñaSQL:
        return True
    else:
        print("Esa contraseña no es la correcta...")
        return False

