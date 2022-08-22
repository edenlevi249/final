import streamlit as st
from sqlalchemy import create_engine
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#connect to PostgreSQL
engine=create_engine('postgresql://postgres:EDENRONI@localhost/finalprojectdb')

#Load specific columns and Specific UsersInfo table
def load_data():
    df=pd.read_sql_table("UsersInfo",engine)
    df=df[["age","sex","settlementtype","cityname","economicstatus"
       ,"fieldofstudy","creativeperson","sociableperson"
       ,"clearrulesframeworks","provideshelpothers","developingfuturecomputers"
       ,"humanpsyche","developingalgorithm"
       ,"researchedanddeveloped","personalissues"
       ,"writtenbroadcastpress","bodystructure"
       ,"technologicalinnovations","trainingandguidance","logicalthinking"]]
    return df
df= load_data() 

#Load specific columns and Specific Auth table
def load_data():
    df_auth=pd.read_sql_table("Auth",engine)
    return df_auth

df_auth= load_data() 

#number of users
array = np.array(df)
rows, columns = array.shape


def show_manager_page():
    st.subheader("Login Manager") 
    username=st.text_input("User Name")
    password=st.text_input("Password",type='password')
    if st.button("Login"):
        if username=="EDENRONI" and password=="EDENRONI":
            st.success("You have successfully create a valid Account")
            st.title("Welcome to manager page")
            st.subheader("Total users in the site:")
            st.subheader(rows)
            st.write("## The answers of the users' questionnaires")
            st.write(df)
            st.write("## User details")
            st.write(df_auth) 
            st.header("Correletion Matrix Heatmap")
            corr=df.corr()
            mask=np.zeros_like(corr)
            mask[np.triu_indices_from(mask)]=True
            with sns.axes_style("white"):
                f,ax=plt.subplots(figsize=(7,5))
                ax=sns.heatmap(corr,mask=mask,vmax=1,square=True)
            st.set_option('deprecation.showPyplotGlobalUse', False)    
            st.pyplot()    

        else:
            st.warning("Incorrect Username/Password") 


