from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# function to take user inputs, load gemini model and provide queries as response.
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# function that takes the response of the model and hits the SQL database
def read_sql_db(sql,db):
    connect = sqlite3.connect(db)
    cur=connect.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    connect.commit()
    connect.close()
    for row in rows:
        print(row)
    return rows
# defining prompt
prompt = [
    '''
        You are an expert in converting english text to SQL code
        The SQL database has the name student_test, it has a table named STUDENT_TEST with 
        columns NAME, CLASS, SECTION.\n\n For example, \n Example1 if the english text is, how many records are
        present in STUDENT_TEST table?. The SQL query will be like, SELECT count(*) FROM STUDENT_TEST;\n
        example2, if the english text is, give me the list of names in STUDENT_TEST table?
        The SQL query will be like, SELECT NAME FROM STUDENT_TEST.\n example 3, if the english text
        is, give me the names of the students from Gen_AI class?  the SQL query will be like, 
        SELECT name FROM STUDENT_TEST where CLASS="Gen_AI"; also the SQL code should not have 
        ``` in the beginning or end and sql word in output

 
    '''
]

# configuring streamlit app (Basically this provides the UI to ask questions)
st.set_page_config(" Can I help u with the data you need today?. Try me to feel amazed ")
st.header("Gemini app to retrieve data")
question=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")
if submit:
    response=get_gemini_response(question,prompt)
    response=read_sql_db(response,"student_test.db")
    st.subheader("The response is: ")
    for row in response:
        print(row)
        st.header(row)


