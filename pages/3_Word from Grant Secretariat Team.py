import streamlit as st

st.set_page_config(
    page_title="Hi there applicant",
    page_icon="👋",
)

st.write("# Hi there Grant Applicant! 👋")

st.markdown(
    """
    Understand applying for grant can be complex and challenging.
    With this app, we aim to empower applicants to navigate the application process independently, providing 24/7 support.
    We look forward to read incredible proposals you submit to help address our nation’s challenges.
    
    1. Please contact us through CTRL_Grant_Secretariat@nea.gov.sg  if you are unable to get the answer your are looking for. 
    2. Please contact Helpdesk@researchgrant.gov.sg if you require assistance with IGMS. Alternatively, refer to the training manual through https://www.researchgrant.gov.sg/Pages/TrainingGuides.aspx
    """)

with st.expander("How to use this app"):
    st.write('''
        1. Enter your prompt in text area
        2. Click the 'Submit' button
        3. The app will generate a text completion based on your prompt.
    ''')

with st.expander("Want to learn more?"):
    st.write('''
        - Check out [Funding Initiative (FI) under NEA](https://www.nea.gov.sg/programmes-grants/grants-and-awards/research-innovation-and-enterprise-funding-initiatives)
    - Jump into our [Closing the Resource Loop FI](https://www.nea.gov.sg/programmes-grants/grants-and-awards/research-innovation-and-enterprise-funding-initiatives/closing-the-resource-loop-funding-initiative)
    ''')

with st.expander("Will there be hallucination?"):
    st.write('''
        Even through we tried our best to test and coded in safe guards, there is still a low likelihood for hallucination.
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
    st.image("https://www.nea.gov.sg/images/default-source/about-us/nea-logo.png")