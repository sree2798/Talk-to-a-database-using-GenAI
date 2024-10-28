# text to SQL Converter using Gemini Pro

Project : Text to SQL query converter with Gemini Pro 

Description: The main goal of this project is to create a chatbot using streamlit interface where we can ask the chatbot in natural language to retrieve data 
from a SQLite database.


<img width="536" alt="text-to_SQL_architecture" src="https://github.com/user-attachments/assets/ef834a89-8742-4c64-9a6a-2b46cb8b1c1d">

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

<img width="956" alt="image" src="https://github.com/user-attachments/assets/53b2bfbc-b789-4e1a-8a9d-c02b6f4e6330">

4) Go to the terminal and run the following command 
pip install -r requirements.txt (we are installing all the libraries mentioned in the requirements.txt file)

<img width="461" alt="image" src="https://github.com/user-attachments/assets/05e5f23f-44ce-44fe-998a-d8cef28b1e92">


5) Create .env file  (for env file, we require google geminipro API) (go to https://aistudio.google.com/apikey) , copy API key and load it in the .env file 
<img width="464" alt="image" src="https://github.com/user-attachments/assets/5ba59831-98c4-4453-8bea-cfa82b581d16">


6) Create new python file (sqlite.py) (The code in this file is responsible for inserting any records in the SQLite database) go to terminal and type, python sqlite.py (you can find the actual file in repo)

Upon the successful run, we see the following output in the terminal along with a “student.db” file in the explorer

<img width="460" alt="image" src="https://github.com/user-attachments/assets/7c1608da-3ee6-4bd1-8f27-8105123dc348">

7) Create a new file sql.py (find the actual code in the repo) and execute (go to terminal and type streamlit run sql.py)
you can find the streamlit output as below

<img width="464" alt="image" src="https://github.com/user-attachments/assets/24f11296-711a-41a2-993e-f4067e57cf8e">






   
