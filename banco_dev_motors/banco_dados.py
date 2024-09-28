import mysql.connector


def conectar():
        conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="a1s2d3f4",
        database="dev_motors" 
        )
        return conexao