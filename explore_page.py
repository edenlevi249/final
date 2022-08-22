
#from itertools import count
#from turtle import color
from re import template
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sqlalchemy import create_engine
import numpy as np
#connect to PostgreSQL
engine=create_engine('postgresql://postgres:EDENRONI@localhost/finalprojectdb')


#Load specific columns and Specific table
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

def show_explore_page():
    st.title("📊Statistical information about users")
    

    ####################################
    #Pie chart of the Users Sex 
    st.write("""### The number of women and men who used the site""")
    data1= df["sex"].value_counts()

    fig_sex, ax1 = plt.subplots()
    ax1.pie(data1, labels=data1.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig_sex)
    
    ####################################
    #Pie chart of the Users field of study 
    st.write("""### Real field VS humane field""")
    data2= df["fieldofstudy"].value_counts()

    fig_fieldof, ax2 = plt.subplots()
    ax2.pie(data2, labels=data2.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax2.axis("equal")  
    st.pyplot(fig_fieldof)
    

    #########################
    #Bar chart of citys names
    st.write("""### The number of people from each settlement""")
    
    city_options=sorted(df['cityname'].unique().tolist())
    city_select=st.multiselect('Which city would you like to see?',city_options,['Kiryat ata','Haifa','Carmiel'])

    city_confirm=df[df['cityname'].isin(city_select)]
    
    fig_city=px.bar(city_confirm,x="cityname",color="fieldofstudy",range_y=[0,100])
    
    fig_city.update_layout(width=800)

    st.write(fig_city)


    ###################################
    #Bar chart of users ages
    st.write("""### Users ages""")
    
    age_options=sorted(df['age'].unique().tolist())
    age_select=st.multiselect('What age range would you like to see?',age_options,['20-25','26-30'])

    age_confirm=df[df['age'].isin(age_select)]
    
    fig_age=px.bar(age_confirm,x="age",color="fieldofstudy")
    
    fig_age.update_layout(width=800)

    st.write(fig_age)

    #Bar chart of creativeperson
    st.write("""### The amount of people who rated themselves as creative people""")
    st.write("### 1=I don't agree at all, 5=I strongly Agree")
    temp_df_bar=df
    temp_df_bar['creativeperson']=temp_df_bar['creativeperson'].astype(str)
    creative_options=sorted(temp_df_bar['creativeperson'].unique().tolist())
    creative_select=st.multiselect('Select the range you want to see:',creative_options,['1','2','3','4','5'])

    creative_confirm=temp_df_bar[temp_df_bar['creativeperson'].isin(creative_select)]
    
    creative_fig=px.bar(creative_confirm,x="creativeperson")
    
    creative_fig.update_layout(width=800)

    st.write(creative_fig)
    

    #Bar chart of sociableperson
    st.write("""### The amount of people who rated themselves as sociable people""")
    st.write("### 1=I don't agree at all, 5=I strongly Agree")
    temp_df_bar['sociableperson']=temp_df_bar['sociableperson'].astype(str)
    sociable_options=sorted(temp_df_bar['sociableperson'].unique().tolist())
    sociable_select=st.multiselect('Select the range you want to see :',sociable_options,['1','2','3','4','5'])

    sociable_confirm=temp_df_bar[temp_df_bar['sociableperson'].isin(sociable_select)]
    
    sociable_fig=px.bar(sociable_confirm,x="sociableperson")
    
    sociable_fig.update_layout(width=800)

    st.write(sociable_fig)
    
    #Bar chart of logicalthinking
    st.write("""### People who defined that they have logical thinking""")
    st.write("### 1=I don't agree at all, 5=I strongly Agree")
    temp_df_bar['logicalthinking']=temp_df_bar['logicalthinking'].astype(str)
    logicalthinking_options=sorted(temp_df_bar['logicalthinking'].unique().tolist())
    logicalthinking_select=st.multiselect(' Select the range you want to see',logicalthinking_options,['1','2','3','4','5'])
    logicalthinking_confirm=temp_df_bar[temp_df_bar['logicalthinking'].isin(logicalthinking_select)]
    logicalthinking_fig=px.bar(logicalthinking_confirm,x="logicalthinking")
    logicalthinking_fig.update_layout(width=800)
    st.write(logicalthinking_fig)

    