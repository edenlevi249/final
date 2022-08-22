import streamlit as st
import pickle
import numpy as np
import psycopg2


#load data from Jupyter note book
def load_model():
    with open('save_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

LogisticRegressionLoad=data["model"]    
le_Age=data["le_Age"]
le_Sex=data["le_Sex"]
le_settlement_type=data["le_settlement_type"]
le_city_name=data["le_city_name"]
le_economic_status=data["le_economic_status"]

#create connection to DB
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

def create_usertable2():
    cur.execute('CREATE TABLE IF NOT EXISTS public."UsersInfo" (id int, age varchar(50), sex varchar(50), studydegree varchar(100), settlementtype varchar(50), cityname varchar(100), economicstatus varchar(50), fieldofstudy varchar(100), academicinstitution varchar(100), chooseagainfieldofstudy varchar(50), workinfieldofstudied varchar(50), creativeperson int, sociableperson int, clearrulesframeworks int, provideshelpothers int, developingfuturecomputers int, humanpsyche int, developingalgorithm int, researchedanddeveloped int, personalissues int, writtenbroadcastpress int, bodystructure int, technologicalinnovations int, trainingandguidance int, logicalthinking int,feedback int)')

def add_userdata2(id,age,sex,studydegree,settlementtype,cityname,economicstatus,fieldofstudy,academicinstitution,chooseagainfieldofstudy,
                  workinfieldofstudied,creativeperson,sociableperson,clearrulesframeworks,provideshelpothers,developingfuturecomputers,
                  humanpsyche,developingalgorithm,researchedanddeveloped,personalissues,writtenbroadcastpress,bodystructure,
                  technologicalinnovations,trainingandguidance,logicalthinking,feedback):
      
      insert_script_userdata2='INSERT INTO public."UsersInfo" ("id","age","sex","studydegree","settlementtype","cityname","economicstatus","fieldofstudy","academicinstitution","chooseagainfieldofstudy","workinfieldofstudied","creativeperson","sociableperson","clearrulesframeworks","provideshelpothers","developingfuturecomputers","humanpsyche","developingalgorithm","researchedanddeveloped","personalissues","writtenbroadcastpress","bodystructure","technologicalinnovations","trainingandguidance","logicalthinking","feedback") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
      insert_userdata2=(id,age,sex,studydegree,settlementtype,cityname,economicstatus,fieldofstudy,academicinstitution,chooseagainfieldofstudy,
                       workinfieldofstudied,creativeperson,sociableperson,clearrulesframeworks,provideshelpothers,developingfuturecomputers,
                       humanpsyche,developingalgorithm,researchedanddeveloped,personalissues,writtenbroadcastpress,bodystructure,
                       technologicalinnovations,trainingandguidance,logicalthinking,feedback)   

      cur.execute(insert_script_userdata2,insert_userdata2)
      conn.commit()

def update_feedback(new_feedback,id):
    upd_feedback='update public."UsersInfo" set feedback=%s where id=%s'
    insert_upd_feedback=(new_feedback,id)
    cur.execute(upd_feedback,insert_upd_feedback)
    conn.commit()




def show_predict_page():
    st.title("👩🏽‍🎓Study guidance questionnaire")

    st.write("## Please fill in your personal details")

    citys=(
    "Ashkelon",
    "Beit Shean",
    "Bnei Brak",
    "Betzet",
    "Bat Hefer",
    "Bat Yam",
    "Givat Avni",
    "Givat Shmuel",
    "Dali'at el Carmel",
    "Deir al-Asad",
    "Zichron Yaakov",
    "Holon",
    "Haifa",
    "Tiberias",
    "Turan",
    "Tirat Carmel",
    "Yifat",
    "Yokneam",
    "Jerusalem",
    "Tel Adashim ",
    "Deir al-Asad",
    "Carmiel",
    "Liman",
    "Migdal HaEmeq",
    "Megiddo",
    "Maccabi",
    "Mishmar HaEmek",
    "Nahariya",
    "Nof HaGalil",
    "Nesher",
    " Natanya",
    " Sakhnin",
    " Acre",
    "Afula",
    "Pekiin",
    "Pardes Hanna",
    "Zefat",
    "Kiryat ata",
    "Kiryat Bialik",
    "Qiryat Gat",
    "Kiryat Haim",
    "Kiryat Yam",
    "Kiryat Motzkin",
    "Rishon Lezion",
    "Rekhasim",
    "Ramat Gan",
    "Raanana",
    "Shefaram",
    "Tel Aviv",
    )

    age=(
    "20-25",
    "26-30",
    "31-35",
    "36-40",
    )

    sex=(
    "Male",
    "Female",
    )

    Economic=(
    "High",
    "Medium",
    "Low",
    )

    LivingType=(
    "City",
    "Moshav",
    "Kibbutz",
    "Village",
    )


    CurrentAge=st.selectbox("Your Age", age)
    sexType=st.selectbox("Your Sex", sex)
    livingType=st.selectbox("Your settlement type", LivingType)
    citysName=st.selectbox("Name of your childhood city ", citys)
    EconomicStatus=st.selectbox("Your famaliy Economic Status", Economic)

    st.write("## Rate your degree of agreement with the following sentences:")
    st.write("### 1=I don't agree at all, 5=I strongly Agree")

    creative_person=st.slider("I'm define myself as a creative person",1,5,4)
    sociable_person=st.slider("I'm define myself as a sociable person",1,5,4)
    clear_rules=st.slider("I prefer work frameworks with clear rules and precise work instructions",1,5,4)
    help_others=st.slider("Provides me to help others",1,5,4)
    developing_computers=st.slider("I am interested in joining a research team that is developing the future generation of computers",1,5,3)
    human_psyche=st.slider("The human psyche fascinates me, I would love to develop scientific tools to understand it",1,5,3)
    mathematical_algorithm =st.slider("I am interested in developing a mathematical algorithm for deciphering an encrypted transmission",1,5,2)
    researched_developed=st.slider("I want to work in a place where new things are being researched and developed",1,5,3)
    personal_issues=st.slider("I want to work in a field that takes care of people and helps them with personal issues",1,5,3)
    written_or_broadcast=st.slider("I am interested in joining a field that allows me to join the written or broadcast press",1,5,2)
    structure_body=st.slider("The structure of the human body interests me",1,5,3)
    technological_innovations=st.slider("Am I updated and interested in technological innovations",1,5,3)
    Guidance=st.slider("Training and guidance give me satisfaction",1,5,4)
    logical_thinking=st.slider("I have logical thinking",1,5,4)
    
    #Setting values ​​not for use
    studydegree="null"
    academicinstitution="null"
    chooseagainfieldofstudy="null"
    workinfieldofstudied="null"
    feedback=0
    
    
    #id= total number of rows
    n_rows='SELECT COUNT(*) FROM public."UsersInfo"'
    n_data=[]
    cur.execute(n_rows,n_data)
    results = cur.fetchone()
    for r in results:
        id=r
    
   
    #Feedback section
    st.sidebar.subheader("📩Feedback")
    new_feedback=st.sidebar.selectbox("Have you registered for a field of study that we have offered you?",('Yes','No'))
    SubmitFeedback=st.sidebar.button("Submit feedback")
    if SubmitFeedback:
        if new_feedback=='Yes':
            new_feedback=1
            create_usertable2()
            update_feedback(new_feedback,id)
            st.sidebar.success("Thank you, your feedback has been received")
        else:
            st.sidebar.success("Thank you for your feedback!")
        

    OK=st.button("Submit")
    if OK:
        x_test=np.array([[CurrentAge,sexType, livingType,citysName,EconomicStatus,creative_person,sociable_person,
                         clear_rules,help_others, developing_computers,human_psyche,mathematical_algorithm,researched_developed
                        ,personal_issues,written_or_broadcast,structure_body,technological_innovations,Guidance, logical_thinking]])
        x_test[:,0]=le_Age.transform(x_test[:,0])
        x_test[:,1]=le_Sex.transform(x_test[:,1])
        x_test[:,2]=le_settlement_type.transform(x_test[:,2])
        x_test[:,3]=le_city_name.transform(x_test[:,3])
        x_test[:,4]=le_economic_status.transform(x_test[:,4])
        x_test=x_test.astype(float)

        FieldOfStudy=LogisticRegressionLoad.predict(x_test)
        pred_value=FieldOfStudy[0]

        if pred_value==0:
            pred_value= "Humane"
        else:
            pred_value= "Realistic"

        st.subheader("Your fit Field of study is:")
        st.write(pred_value)
        
        #update the num of rows 
        id=id+1

        create_usertable2()
        add_userdata2(id,CurrentAge,sexType,studydegree,livingType,citysName,EconomicStatus,pred_value,academicinstitution,chooseagainfieldofstudy,
                       workinfieldofstudied,creative_person,sociable_person,clear_rules,help_others,developing_computers,
                       human_psyche,mathematical_algorithm,researched_developed,personal_issues,written_or_broadcast,structure_body,
                       technological_innovations,Guidance,logical_thinking,feedback)
        

         
                



