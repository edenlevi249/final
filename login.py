import streamlit as st
import psycopg2
from PIL import Image
from Manager_page import show_manager_page

hostname='localhost'
database='finalprojectdb'
user_name='postgres'
pwd='EDENRONI'
port_id=5432

conn=psycopg2.connect(
    host=hostname,
    dbname=database,
    user=user_name,
    password=pwd,
    port=port_id)

cur=conn.cursor()


def create_usertable():
    cur.execute('CREATE TABLE IF NOT EXISTS public."UsersInfo" (id int, age varchar(50), sex varchar(50), studydegree varchar(100), settlementtype varchar(50), cityname varchar(100), economicstatus varchar(50), fieldofstudy varchar(100), academicinstitution varchar(100), chooseagainfieldofstudy varchar(50), workinfieldofstudied varchar(50), creativeperson int, sociableperson int, clearrulesframeworks int, provideshelpothers int, developingfuturecomputers int, humanpsyche int, developingalgorithm int, researchedanddeveloped int, personalissues int, writtenbroadcastpress int, bodystructure int, technologicalinnovations int, trainingandguidance int, logicalthinking int,feedback int)')

def add_userdata(username,Password,email,age,sex,settlement):
      
      insert_script_userdata='INSERT INTO public."Auth" ("username","password","email","age","sex","settlementname") VALUES (%s,%s,%s,%s,%s,%s)'
      insert_userdata=(username,Password,email,age,sex,settlement)
      cur.execute(insert_script_userdata,insert_userdata)
      conn.commit()

def login_user(username,Password):
     insert_script_login_user='SELECT * FROM public."Auth" WHERE username=%s AND password=%s'
     insert_login_user=(username,Password)
     cur.execute(insert_script_login_user,insert_login_user)
     data=cur.fetchall()
     return data    



def main():
    image=Image.open('FullLogo.jpg')
    st.image(image, width=400)
    
    from streamlit_option_menu import option_menu
    with st.sidebar:
        choice = option_menu("Menu", ["Home","Login","SignUp","Maneger page"], 
                icons=['house','box-arrow-right','pencil','file-person'], menu_icon="cast", default_index=0)
            



    if choice =="Home":
        st.title("Welcome to RE CEIVE")
        st.write("### Do you want to study a bachelor's degree and do not know which field to choose?")
        st.write("#### You have come to the right place!")
        st.write("This site was developed to help prospective students understand which field of study is most suitable for them.")  
        st.write("### So what should you do?")   
        st.write("Register to the website and fill out the questionnaire, after that you will know which field of study is right for you.")
        st.write("Don't worry, we won't send you advertisements, this site is designed to serve you.")  
    
    elif choice =="Login":
        st.subheader("Login") 
        username=st.text_input("User Name")
        password=st.text_input("Password",type='password')
        if st.button("Login"):
            create_usertable()
            result=login_user(username,password)
            if result:   
               st.success("Logged In as {}".format(username))

               import os
               try:
                 os.system('cmd /k "streamlit run app.py"')
               except:
                 print('could not execute command') 
               
            else:
                st.warning("Incorrect Username/Password")        
            
    elif choice =="SignUp":
        st.subheader("Create new account")     
        new_user=st.text_input("Username")
        new_password=st.text_input("Password", type='password')
        new_email=st.text_input("Email address")
        new_age=st.text_input("Age")
        new_sex=st.selectbox("Sex",('Male','Female'))
        new_settlement=st.text_input("Settlement name")

        if st.button("SignUp"):
            create_usertable()
            add_userdata(new_user,new_password,new_email,new_age,new_sex,new_settlement)
            st.success("You have successfully create a valid Account")
            st.info("Go to Login Menu to login")

    elif choice =="Maneger page":
        show_manager_page()
        

             
       


if __name__=='__main__':
    main()    




