import streamlit as st
import mysql.connector
import toml

local_debug_mode = True
try:
    # # config = toml.load("secrets.toml") #Načtení toml secrets souboru pro local_debug_mode
    #
    # # Připojení k databázi
    connection = mysql.connector.connect(
        # host=config['database']['DB_SERVER'],
        # user=config['database']['DB_USERNAME'],
        # password=config['database']['DB_PASSWORD'],
        # database=config['database']['DB_NAME'],

    )

    # cnx = mysql.connector(user='rozhovor_mysql', password='dadqUm-kizco4-fovqip',
    #                               host='rozhovor-mysql.mysql.database.azure.com',
    #                               database='rozhovor_schema')
    # cnx.close()
except Exception as e:
    print("Error: ", e)
