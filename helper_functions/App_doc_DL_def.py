import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

##### RUN CODE [ONCE] T DOWNLOAD DOCUMENT FROM APPLICAION WEBSITE################

def RFPapplication_doc_dl(application_doc_url, folder_path):
    response = requests.get(application_doc_url)
    
    if response.status_code != 200:
        return
    
    os.makedirs(folder_path, exist_ok=True)
    
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", href=True)
    
    for link in links:
        href = link['href']
        if href.endswith(('.pdf', '.docx', '.xlsx', '.csv')):
            file_url = urljoin(application_doc_url, href)
            file_name = os.path.join(folder_path, href.split("/")[-1])

            if os.path.exists(file_name):
                continue

            with requests.get(file_url, stream=True) as doc_response:
                if doc_response.status_code == 200:
                    with open(file_name, 'wb') as file:
                        for chunk in doc_response.iter_content(chunk_size=8192):
                            file.write(chunk)

if __name__ == "__main__":
    application_doc_url = "https://www.nea.gov.sg/programmes-grants/grants-and-awards/research-innovation-and-enterprise-funding-initiatives/air-quality-monitoring-and-control-funding-initiative"
    folder_path = r"C:/Users/Sin Kuan Tan/OneDrive/Coding/Streamlit/Grant_Application_Chatbot/data"
    RFPapplication_doc_dl(application_doc_url, folder_path)
