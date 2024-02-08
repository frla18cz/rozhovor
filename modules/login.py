# login.py
import openai
import toml
import streamlit as st

def login(local_debug_mode):
    if local_debug_mode == True:
        config = toml.load("secrets.toml")
        openai.api_key = config['api']['API_KEY']
        assistant_id = config['api']['ASSISTANT_ID']
        print(f"Připojení k OpenAI API lokálním klíčem")
    else:
        #Inicializace api key a ID. Uloženo na cloudu streamlit v secret
        openai.api_key = st.secrets["API_KEY"]
        assistant_id = st.secrets["ASSISTANT_ID"]
        # assistant_id = "asst_atZWsxED84ngEs7lXxCAKR9Q" #Pro testovací účely, light prompt
        print("Připojení k OpenAI API secret klíčem na cloudu streamlit")

    return assistant_id
