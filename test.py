from bs4 import BeautifulSoup
import requests
import re

URL = input("URL: ").strip()
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="article-details")
information_elements = results.find_all("div", class_="full-view")
extract_elements(information_elements)

    

for information_element in i_f:
    journal_element = information_element.find("button", class_="journal-actions-trigger trigger").text.strip()
    volume_pgnumbers_year_element = information_element.find("span", class_="cit").text.strip()
    year_element, month_element, vol_pg_element = re.split(pattern = r"[ ;]", string = volume_pgnumbers_year_element)
    doi_element = information_element.find("span", class_="citation-doi").text.strip().replace("doi: ", "")
    title_element = information_element.find("h1", class_="heading-title").text.strip()
    authors_element = information_element.find("div", class_="authors-list").text.strip()
sanitize_author_list(authors_element)
order_components(authors_element, title_element, journal_element, year_element, vol_pg_element, doi_element)

def sanitize_author_list(a_e):
    if "1" indef get_url(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="article-details")
    information_elements = results.find_all("div", class_="full-view")
    extract_elements(information_elements)
    
    
def extract_elements(i_f):
    for information_element in i_f:
        journal_element = information_element.find("button", class_="journal-actions-trigger trigger").text.strip()
        volume_pgnumbers_year_element = information_element.find("span", class_="cit").text.strip()
        year_element, month_element, vol_pg_element = re.split(pattern = r"[ ;]", string = volume_pgnumbers_year_element)
        doi_element = information_element.find("span", class_="citation-doi").text.strip().replace("doi: ", "")
        title_element = information_element.find("h1", class_="heading-title").text.strip()
        authors_element = information_element.find("div", class_="authors-list").text.strip()
    sanitize_author_list(authors_element)
    order_components(authors_element, title_element, journal_element, year_element, vol_pg_element, doi_element)

def sanitize_author_list(a_e):
    if "1" in