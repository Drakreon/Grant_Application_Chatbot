import streamlit as st

st.set_page_config(
    page_title="Methodology",
    page_icon="📋",
)

st.write("# Methodology📋")

st.markdown(
    """
This project adopts a structured workflow, starting with data extraction and the creation of a vector database from grant call
documents. To ensure safety and reliability, Crew AI agents are integrated to handle query filtering, rephrasing, data retrieval,
and response generation.

The **left flowchart** illustrates the core chatbot process 🤖, beginning with the user’s query. The query undergoes an initial
filter to block malicious content, followed by refinement through a rephrasing agent. The refined query is then used by the
retriever agent to search the vector database for relevant information. The response generator crafts a final reply using either
the rephrased query or the retrieved data, which is ultimately presented to the user.

The **right flowchart** provides an overview of the backend processes 💾, including embedded model operations and data retrieval.
It outlines how data, such as information from previous grant calls, is scraped, processed, and stored as vector
representations in the database. When a query is received, Crew AI agent retrieve matching vectors and forward them
to the response generator, which, as shown in the left flowchart, produces the final output.
""")

# st.image("Image\Flowchart for AIbootcamp.drawio.png")
st.image(
    "https://raw.githubusercontent.com/Drakreon/Grant_Application_Chatbot/main/Image/Flowchart%20for%20AIbootcamp.drawio_2.png"
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