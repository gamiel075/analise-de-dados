import pyodbc

nome_servidor = 'Mimosa\gabri' # Substitua pelo nome real do servidor
nome_banco_dados = 'VendasDB'  # Substitua pelo nome real do banco de dados

conn = pyodbc.connect(f'Driver={{SQL Server}};Server={nome_servidor};Database={nome_banco_dados};Trusted_Connection=yes;Timeout=40;')
