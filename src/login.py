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
import pandas as pd
import psycopg2
from sympy import false
import bcrypt

conn = psycopg2.connect("host=localhost dbname=proyecto2 user=postgres password=rwby123")
cur = conn.cursor()

def loginInfo(usuario, contraseña):
    

    fetchLoginInfo_Query = "SELECT nombre_usuario,contraseña FROM usuario WHERE usuario.nombre_usuario = '{0}' and usuario.contraseña = '{1}'".format(usuario, contraseña)
    cur.execute(fetchLoginInfo_Query)
    login_records = cur.fetchall()
    print(login_records)
    contraseñaSQL = login_records[0][1]
    print(contraseñaSQL)
    '''
    passwd = bytes(contraseña, 'utf-8') 
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt(10)) 
    matched = bcrypt.checkpw(passwd, hashed)
    '''


    if not login_records:
        return False
    else:
        return True

print(loginInfo('AndresDLR', 'Andres1234'))
