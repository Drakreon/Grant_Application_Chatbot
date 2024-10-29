import streamlit as st

st.set_page_config(
    page_title="Methodology",
    page_icon="📋",
)

st.write("# Methodology📋")

st.markdown(
    """
    This project follows a structured approach, starting with data extraction and vector database creation from grant call
    documents. To ensure safety and reliability, Crew AI agents are integrated for query filtering, rephrasing, data retrieval, and response generation.
    """)

# st.image("Image\Flowchart for AIbootcamp.drawio.png")
st.image(
    "https://raw.githubusercontent.com/Drakreon/Grant_Application_Chatbot/main/Image/Flowchart%20for%20AIbootcamp.drawio.png"
)

st.markdown(
    """ 
    Brought to you by the CTRL Grant Secretariat Team.
    """)

st.markdown("<div class='top-padding'></div>", unsafe_allow_html=True)

# Create three columns: left, center, right
col1, col2, col3 = st.columns([3, 2, 2])
# Insert the image in the rightmost column
with col2:
    st.image("https://www.nea.gov.sg/images/default-source/about-us/nea-logo.png", width=400)