from project import extract_elements
from project import get_url
from project import sanitize_authors

URL = "https://pubmed.ncbi.nlm.nih.gov/25041215/"
# Doing this above is called a constant


def main():
    test_get_url()
    test_extract_elements()
    test_sanitize_authors()
    
def test_get_url():
    assert len(get_url(URL)) > 0
    
def test_extract_elements():
    html = get_url(URL)
    assert len(extract_elements(html)) == 6

def test_sanitize_authors():
    assert len(sanitize_authors("Bob Jones, Billy Bob")) > 0
    assert len(sanitize_authors("Bob Jones, Billy Bob, Dog, Whitney Johnson")) > 0
    assert len(sanitize_authors("")) == 0
    assert len(sanitize_authors("1, 2, 3, 4, 5, 6")) > 0
    assert len(sanitize_authors("Bob Jones Billy Bob")) > 0
    
   
if __name__ == "__main__":
    main()