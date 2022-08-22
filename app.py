import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from streamlit_option_menu import option_menu
from PIL import Image
from Manager_page import show_manager_page



image=Image.open('logo.jpg')
st.image(image, width=100)

#sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Questionnaire", "Explore","Manager"],     
            icons=['graph-up', 'bar-chart-line','file-person'], menu_icon="cast", default_index=0)
        


if selected== "Questionnaire":
    show_predict_page()
elif selected== "Explore":
    show_explore_page() 
elif selected== "Manager":
    show_manager_page()



