import streamlit as st

st.set_page_config(
    page_title="🎉 About Us",
    page_icon="👋",
)

st.write("# About Us 👋")

st.markdown(
    """
    Welcome to our innovative project aimed at supporting grant applicants through an AI-powered chatbot. We are a dedicated team of three musketeers 🏇 behind the scenes, ready to assist with any queries regarding grant applications.

✨Our mission: :blue-background[**streamline the grant application process and enhance the applicant experience.**] ✨ 
""")

with st.expander("⚠️Current Challenge"):
    st.write('''
Responding to grant applicants' queries consumes about **10% of our work time** during grant call periods. We see an opportunity to leverage 🤖**Large Language Models (LLMs)** to develop an intelligent chatbot, designed to provide **consistent, accurate, and immediate** responses to queries.

The chatbot will learn, adapt, and improve over time, ensuring every interaction is better than the last. Future expansions may include support for all NEA-managed grant calls.
''')

with st.expander("📋 Project Scope"):
    st.write('''
        Project focuses on building a custom chatbot using Agentic Retrieval-Augmented Generation (RAG) technology to answer a variety of questions about grant calls and application processes. Here’s a breakdown of the key development areas:

        📑 **Step 1: Data Extraction and Forming of Vector Database from Grant Call Documents**:             
            - Extracting and combining text from grant call documents   
            - Text splitting and conversion to Vector Database
            
            
        ⚙️ **Step 2: Evaluation and Selection of LLM **:           
            - Fine-tuning parameters of vector database such as chunk size to improve accuracy and efficiency           
            - Using RAGAS to select between (a) Recursive chunking + naive retrival , (b) Semantic chunking and (c) Recursive chunking + Parent-child + Naive retirval   
            -  <ADD ASSESSMENT>
                          
        🔐 **Step 3: LLM Safety and Accuracy Assurance**:           
            - Integrating Crew AI for safe and reliable information retrieval using 4 Crew (query_filter_agent, query_rephraser_agent, query_retriever_agent, response_generator_agent)           
            - Features prevents malicious content generation, ensure information accuracy and format it to goverment style responses
             
        🛠️ **Step 4: Quality Assurance and Testing**:           
            - Testing chatbot responses across various query types           
            - Validating performance on complex and nuanced questions           
            - Enhancing relevance by incorporating historical FAQs           
            - <ADD ASSESSMENT>
    ''')

with st.expander("🎯 Objectives"):
    st.write('''
    Our primary goal is to create an **AI-powered chatbot** that efficiently handles grant-related queries, **reducing staff time** spent on routine inquiries from **10% to 5%** during grant call periods. We aim to provide:

    - **Consistent, accurate, and instant** responses to applicants
    - **Improved efficiency** in the grant application process
    - A **scalable solution** with potential future use across all NEA-managed grants
    ''')

with st.expander("📊 Data Sources"):
    st.write('''
    For this Proof of Concept (POC), we are using data from a recent close plastic grant call earlier this year.

    **Key Data Sources:**
    - 📄Grant-specific documents: Consist of 12 documents covering the application process, eligibility criteria, proposal template, and evaluation matrix 
    - ❓Frequently Asked Questions (FAQs): (a) Used to evaluated the chatbot through RAGAS and (b) incoperated into the final chatbot to improve response quality

    In a production environment, we have tested codes which can scrape NEA Grant call webpages for real-time updates of documents. For now, the POC uses locally stored grant documents to ensure reliable processing.''')

st.markdown(
    """ 
    Brought to you by the CTRL Grant Secretariat Team.
    """)

# # Add top padding
# st.markdown(
#     """
#     <style>
#     .top-padding {
#         padding-top: 100px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# Apply the padding by creating an empty div
st.markdown("<div class='top-padding'></div>", unsafe_allow_html=True)

# Create three columns: left, center, right
col1, col2, col3 = st.columns([3, 2, 2])
# Insert the image in the rightmost column
with col2:
    st.image("https://www.nea.gov.sg/images/default-source/about-us/nea-logo.png", width=400)