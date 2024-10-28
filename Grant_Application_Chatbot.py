__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from CrewAI.Crew_v3 import crew
from helper_functions.utility import check_password  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="GAC - Grant Application Chatbot"
)

st.title("Grant Application Chatbot")

#Check if the password is correct.  
if not check_password():  
    st.stop()

form = st.form(key="form")
form.subheader("""I am a chatbot designed to help you with your queries on applying for NEA RIE 2025 Grants.""")

st.markdown(
    """
    Use cases for chatbot include: application support and guidance, grant eligibility and requirements check, request for proposal clarification""")

user_prompt = form.text_area("Enter your prompt here:", height=200)

if form.form_submit_button("Submit"):
    if user_prompt:
        user_prompt = user_prompt.strip()
        print(f"User Input is: {user_prompt}")

        with st.spinner('Loading....'):
            response = crew.kickoff(inputs={"query": user_prompt})
        st.write("#####")
        st.text_area(label="Chatbot output:", value=response.raw, height=400)
   
    else:
        st.warning("Please enter a prompt before submitting.")

with st.expander("**IMPORTANT NOTICE** ❗❗❗:"):
    st.write('''This web application is developed as a proof-of-concept prototype. The information provided here is **NOT intended for actual usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**
Always consult with qualified professionals for accurate and personalised advice. ''')
    
# Add top padding
st.markdown(
    """
    <style>
    .top-padding {
        padding-top: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Apply the padding by creating an empty div
st.markdown("<div class='top-padding'></div>", unsafe_allow_html=True)

# Create three columns: left, center, right
col1, col2, col3 = st.columns([3, 2, 2])
# Insert the image in the rightmost column
with col2:
    st.image("https://www.nea.gov.sg/images/default-source/about-us/nea-logo.png", width=400)