# text to SQL Converter using Gemini Pro

Project : Text to SQL query converter with Gemini Pro 

Description: The main goal of this project is to create a chatbot using streamlit interface where we can ask the chatbot in natural language to retrieve data 
from a SQLite database.


Text (prompt) → LLM model → Gemini Pro or ChatGPT → Query →  SQL database → response

The text will be given to LLM model and it will specifically give you a QUERY, this QUERY will try to execute and read from a SQL database 

Implementation:
SQLite database → we will insert some records by using python programming language
LLM application →  This LLM application will communicate with the GeminiPro and Geminipro will communicate with the SQLite database to give the response 
Steps: 
1) The first step is to create an environment 
		Open New terminal in VS code, type 
conda create -p venv python==3.10 -y 
2) Execute  conda activate venv/  (The path will be changed to inside the virtual environment)
3) Create requirements.txt file (it basically says what libraries do I require)
   
