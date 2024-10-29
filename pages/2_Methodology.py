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

st.image("Image\Flowchart for AIbootcamp.drawio.png")