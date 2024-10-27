import streamlit as st
import Langchai_helper
from secret_key import api_key

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine",("Indian", "Italian","Mexican","Japanese","American","Koarean","Vietnamese"))

if cuisine:
    response = Langchai_helper.getnerate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write(" Menu Items ")
    for items in menu_items:
        st.write("-",items)