import streamlit as st

st.set_page_config(
    page_title="About Us",
    page_icon="👋",
)

st.write("# About Us 👋")

st.markdown(
    """
    Welcome to our innovative project aimed at supporting grant applicants through an AI-powered chatbot. We are a dynamic duo committed to delivering excellence ☯ behind the scenes, ready to assist with any queries regarding grant applications.

✨Our mission: :blue-background[**streamline the grant application process and enhance the applicant experience.**] ✨ 
""")

with st.expander("⚠️Current Challenge"):
    st.write('''
Responding to grant applicants' queries consumes about **10% of our work time** during grant call periods. We see an opportunity to leverage 🤖**Large Language Models (LLMs)** to develop an intelligent chatbot, designed to provide **consistent, accurate, and immediate** responses to queries.

The chatbot will learn, adapt, and improve over time, ensuring every interaction is better than the last. Future expansions may include support for all NEA-managed grant calls.
''')

with st.expander("📋 Project Scope"):
    st.write('''
        Project focuses on building a custom chatbot using Retrieval-Augmented Generation (RAG) technology with Crew AI Agents to answer a variety of questions about grant calls and application processes. Here’s a breakdown of the key development areas:

        📑 **Step 1: Data Extraction and Forming of Vector Database from Grant Call Documents**:
                          
        - Extracting and combining text from grant call documents   
        - Text splitting and conversion to Vector Database
            
            
        ⚙️ **Step 2: Evaluation and Selection of LLM**:
                          
        - Fine-tuning parameters of vector database such as chunk size to improve accuracy and efficiency           
        - Using RAGAS to select the best retrieval combination (refer to more details in assessment section)
                          
        🔐 **Step 3: LLM Safety and Accuracy Assurance**:
                          
        - Integrating Crew AI agents for safe and reliable information retrieval. The four Crew AI are   
            (a) **Query filter** - Differentiate malicious query from query related to grant applicaiton   
            (b) **Query Rephraser** - Assess of the query is clear and provide edits ONLY when needed   
            (c) **Query Retriever** - Retrieve the data from the vector database   
            (d) **Response Generator** - Generate civil servant format of response based on reference provided           
        - Prevent malicious content generation, ensure information accuracy and generate responses are replied in civil servant tone
             
        🛠️ **Step 4: Quality Assurance and Testing**:
                          
        - Testing chatbot responses across various query types           
        - Validating performance on complex and nuanced questions (refer to more details in assessment section)          
        - Enhancing relevance by incorporating historical FAQs           
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
    For this Proof of Concept (POC), we are using data from a recently closed plastic grant call.

    **Key Data Sources:**
    - 📄**Grant-specific documents**: Consist of 12 documents covering the grant call topics, application process, eligibility criteria, proposal template, and evaluation matrix, etc.
    - ❓**Frequently Asked Questions (FAQs)**: This is a document where we compiled the questions that were asked and answers provided. It was used during the evaluation of the chatbot to select the retrieval method (during RAGAS ).
    The document would be eventually incorporated into the chatbot at our final step as a data source to improve response quality
             
    In a production environment, we have tested codes which can scrape NEA Grant call webpages for real-time updates of documents. For now, the POC uses locally stored grant documents to ensure reliable processing.''')

with st.expander("🔍 Evaluation of LLM"):
    st.write('''
    :red-background[**Evaluation 1: Evaluation of splitting and chunking methods**]
             
    We evaluated three splitting and chunking methods using RAGAS metrics based on five past queries and answers:
    - Recursive + Naïve retrieval
    - Semantic + Naïve retrieval
    - Recursive + Parent and Child + Naïve retrieval
             
    Although the Semantic + Naïve Retrieval combination achieved the highest scores in Answer Relevancy (0.9416) and Correctness (0.4699), it generated the most hallucinations, raising concerns about reliability. This is a critical concern, as hallucinations can lead to misinformation and reduce the reliability of the system.
     
    **We chose the Recursive + Naïve Retrieval method for the following reasons:**
    - Reduced hallucinations: Compared to the Semantic method, the Recursive combination produces fewer hallucinations, ensuring better answer integrity.
    - Balanced approach : While not the top scorer, it offers solid results with a Relevancy score of 0.7376. It also provides decent results across all metrics
    
    This chosen combination aligns with our goal of providng accurate and reliable information by balancing performance in relevancy with minimal hallucination risk.                   
    ''')
    st.image(
    "https://raw.githubusercontent.com/Drakreon/Grant_Application_Chatbot/main/Image/RAGAS%20evaluation.png",
    width=650)


    st.write('''
    :red-background[**Evaluation 2: Human Evaluation of Output from Chatbot**]
    
    XXXXX
    ''')

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