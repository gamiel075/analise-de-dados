def calcular (x,y):
    print( x + y)


import pyodbc
import pandas as pd


dados_conexao = (

    "driver={SQL Server};"
    "server= Mimosa\SQLEXPRESS;"
    "database = VendasDB;"
    "Timeout=30;"
)

conexão = pyodbc.connect(dados_conexao)

