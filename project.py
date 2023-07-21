from bs4 import BeautifulSoup
import requests
import re

def main():
    while True:
        # Ask user for PubMed URL
        URL = input("PubMed URL: ").strip()
        print()
        # Ensure URL is from PubMed
        matches = re.search(r"^(https://)?pubmed\.ncbi\.nlm\.nih\.gov/[0-9]*/$", URL)
        if matches:
            break
        else:
            # Loop back to input until valid URL given
            print("Invalid URL, please try again")
            pass
    information_from_url = get_url(URL)
    one, two, three, four, five, six = extract_elements(information_from_url)
    print(order_components(one, two, three, four, five, six))

def get_url(URL):
    #Link back to URL given by user
    page = requests.get(URL)
    if page.status_code != 200:
        return []
    # Create soup object where parsing ability is present
    soup = BeautifulSoup(page.content, "html.parser")
    # Narrow down HTML using specific Id and classes which contain what I want to parse through
    results = soup.find(id="article-details")
    information_elements = results.find_all("div", class_="full-view")
    print(len(information_elements))
    return information_elements

def extract_elements(i_f):
    # Loop through all information_elements to get all I am looking for
    for information_element in i_f:
        # Extract journal name from article
        journal_element = information_element.find("button", class_="journal-actions-trigger trigger").text.strip()
        # Extract year, volume, page numbers from article
        volume_pgnumbers_year_element = information_element.find("span", class_="cit").text.strip()
        # Volume/page/year elements are formatted differently depending on depending on article, following code accounts for multiple variations
        year_month_date_vol_pg = re.search(r"^[0-9]+ ([A-Z]?[a-z]+) [0-9]+;.+$", volume_pgnumbers_year_element)
        year_vol_pg = re.search(r"^[0-9]+;.+$", volume_pgnumbers_year_element)
        year_month_vol_pg = re.search(r"^[0-9]+ ([A-Z]?[a-z])+;.+$", volume_pgnumbers_year_element)
        year_monthrange_vol_pg = re.search(r"^[0-9]+ ([A-Z]?[a-z]+)\-([A-Z]?[a-z]+);.+$", volume_pgnumbers_year_element)
        if year_month_date_vol_pg:
            year_element, month_element, date_element, vol_pg_element = re.split(pattern = r"[ ;]", string = volume_pgnumbers_year_element)
        elif year_vol_pg:
            year_element, vol_pg_element = re.split(pattern = r"[ ;]", string = volume_pgnumbers_year_element)
        elif year_month_vol_pg:
            year_element, month_element, vol_pg_element = re.split(pattern = r"[ ;]", string = volume_pgnumbers_year_element)
        elif year_monthrange_vol_pg:
            year_element, monthrange_element, vol_pg_element = re.split(pattern = r"[ ;]", string = volume_pgnumbers_year_element)
        # Extract and format doi from article
        doi_element = information_element.find("span", class_="citation-doi").text.strip().replace("doi: ", "")
        doi_element_reversed = (doi_element[::-1]).replace(".", "", 1)
        sanitized_doi_element = (doi_element_reversed[::-1])
        #Extract title from article
        title_element = information_element.find("h1", class_="heading-title").text.strip()
        # Extract authors' names from article
        authors_element = information_element.find("div", class_="authors-list").text.strip()
        # Sanitize authors' element
        if "1" in authors_element:
            sanitized_authors = sanitize_authors(authors_element)
            return sanitized_authors, title_element, journal_element, year_element, vol_pg_element, sanitized_doi_element
        else:
            return authors_element, title_element, journal_element, year_element, vol_pg_element, sanitized_doi_element

def sanitize_authors(authors_element):
    res = ''
    authors_without_numbers = re.sub(r"[0-9]+", repl = "", string = authors_element)
    lst = authors_without_numbers.split(',')
    for author in lst:
        res += author.strip() + ', '
    return res[:-2]

def order_components(a, t, j, y, v, d):
    # Create dictionary with all elements to index into
    dict = {
        "1": a,
        "2": t,
        "3": j,
        "4": y,
        "5": v.replace(".", ""),
        "6": d
    }
    # Provide instructions to user on how to format their reference
    print("Please list the following components in the order of your choice using their corresponding numbers:")
    print("1. Authors")
    print("2. Title")
    print("3. Journal")
    print("4. Year")
    print("5. Volume/Page")
    print("6. Doi")
    print("example: 1, 2, 3, 4, 5, 6")
    print()

    while True:
        # Obtain user input on their desired reference format
        order = input("Order: ").strip().lower()
        # Split user input into six different elements
        components = order.split(", ")
        # Ensuring user inputs exactly 6 elements, otherwise loop continues until requirement met
        if len(components) > 6:
            print("Too many components, please try again")
            pass
        elif len(components) < 6:
            print("Too few components, please try again")
            pass
        else:
            try:
                first, second, third, fourth, fifth, sixth = components
                print()
                print("Reference:")
                # User input is used to index back into dictionary to obtain corresponding order of reference components
                return dict[first] + ". " + dict[second] + ". " + dict[third] + ". " + dict[fourth] + ". " + dict[fifth] + ". " + dict[sixth] + "."
            except KeyError:
                # Error checking in case one or more of user_input doesnt match Keys in dictionary
                print("Hmm, looks like one or more of your components don't exist. Please try again!")

if __name__ == "__main__":
    main()