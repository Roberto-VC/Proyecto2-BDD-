import psycopg2
import bcrypt

conn = psycopg2.connect("host=localhost dbname=proyecto_2 user=postgres password=rwby123")
cur = conn.cursor()

def busqueda_actores():
    return 0
