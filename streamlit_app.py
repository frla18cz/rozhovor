import streamlit as st

# Název aplikace
st.title('Moje první Streamlit aplikace')

# Zobrazení textu
st.write('Vítejte ve světě Streamlit! Toto je vaše první aplikace.')

# Tlačítko pro akci
if st.button('Stiskni mě'):
    st.write('Hurá! Stiskli jste tlačítko.')
