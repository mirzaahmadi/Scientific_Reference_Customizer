from bs4 import BeautifulSoup
import requests
import re

URL = input("URL: ") 
# "https://pubmed.ncbi.nlm.nih.gov/6576345/" #Birds, behavior, and anatomical evolution
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="article-details")

information_elements = results.find_all("div", class_="full-view")

for information_element in information_elements:
    journal_element = information_element.find("button", class_="journal-actions-trigger trigger").text.strip()
    volume_pgnumbers_year_element = information_element.find("span", class_="cit").text.strip()
    year_element, month_element, vol_pg_element = re.split(pattern = r"[ ;]", string = volume_pgnumbers_year_element)
    doi_element = information_element.find("span", class_="citation-doi").text.strip().replace("doi: ", "")
    title_element = information_element.find("h1", class_="heading-title").text.strip()
    authors_element = information_element.find("div", class_="authors-list").text.strip()
        
    print(journal_element)
    print(year_element)
    print(vol_pg_element)
    print(doi_element)
    print(title_element)
    print(authors_element)
    
    # print(f"{authors_element}. {title_element}. {journal_element}. {year_element}. {vol_pg_element} {doi_element}")






# journal_abbreviation = results.find_all("div", class_="journal-actions dropdown-block")

# print(journal_abbreviation)