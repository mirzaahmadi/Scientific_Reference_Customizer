from bs4 import BeautifulSoup
import requests

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# It creates a parse tree for parsed pages that can be used to extract data from HTML

results = soup.find(id="ResultsContainer")
# creating a beautiful soup object (soup) that takes page content as its input

""" 
FINDALL SYNTAX
###find_all(name, attrs, recursive, string, limit, **kwargs)
the name in this method signature above refers to a tag in HTML, such as h2 (contained within <h2> when inspecting element)
the string in this method signature allows you to search for specific strings in the text portion instead of tags
"""





job_elements = results.find_all("div", class_="card-content")
# Calling find_all on a beautiful soup object returns an iterable containing all the html for all the job listings
# which are under the class "card-content" (card as in job card)

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # print(title_element.text.strip())
    # print(company_element.text.strip())
    # print(location_element.text.strip())
# For each line of code in job_elements, which returns an iterable for everthing in the job cards, 
# i can use the find() function to find specifics of what Im looking for, mainly 
# titles of jobs, the comapnies offering these jobs, and the locations of these jobs. 

# the .text at the end only extracts the text elements of HTML


""" 
So, the above code just gets the end product of all the job titles, company names and locatiosn for each job. However,
we still need to only look for software developer jobs. 
"""





#_________________________________________


# python_jobs = results.find_all("h2", string="Python")
# print(python_jobs)

# this approach (^^) will return an empty list, because making the string just named
#'Python' does not take into account any whitespace(), capitalization, punctuation etc.




python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
""" 
This above approach works though
^^^
Now youre passing an anonymous function to the string= argument. 
The lambda function looks at the text of each <h2> element, 
converts it to lowercase, and checks whether the substring 
"python" is found anywhere. You can check whether you managed 
to identify all the Python jobs with this approach:
""" 
# print(python_jobs)
# for job_element in python_jobs:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     # print(title_element.text.strip())
#     # print(company_element.text.strip())
#     # print(location_element.text.strip())
#     # print()
    
""" 
However, this returns an error. that is becuase I am searching for elements
that ONLY have python in it - nothin else. But none of the job titles
only say python, thus, I get an attribute error.

The text I am looking for is nested in sibling elements of the 
<h2> elements your filter returned. Beautiful Soup can help you
to select sibling, child, and parent elements of each 
Beautiful Soup object.
"""

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
# So now, we want to look at the complete card content JUST FOR every
# python related job. This code above allows us to do just this, 
# as it loops through all ten of of the python jobs, and returns back the 
# the card-content which is three generations up in the html code - 
# thus, that is why it is .parent.parent.parent (three times)



# NOW WE CAN LOOP THROUGH python_job_elements which contains
# the title, company and location tags 

# for job_element in python_job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
    
    # Finally, now we have to get the URLs of the actual apply links
    # One may thunk we could use the following code: 
    
# for job_element in python_job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     links = job_element.find_all("a") # a is the tag for the links
#     for link in links:
#         print(link.text.strip())
#     print()
    # However, the above text doesnt actually print the URL, because of the 
    # .text function, it only prints the text in the part associated with the "a" tag
    # which is "Apply"  and "Learn"
    
    
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    link_url = job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")
    print()
    
    # Finally, this last code gives you the url
    # for link_url = :
    # It finds all the job elements that start with "a" tag, which are the two URLs. You only care about the second URL though,
    # So we index into only the second URL, and then we refernece the actual URL itself and extracting it using the 
    # square-bracket notation and addressing the href attribute (["href"]).
    
    #______________________________________________________________
    
    
    
#The code without comments is below:
    
    
""" 
from bs4 import BeautifulSoup
import requests

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")
    
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
    
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
    
    
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    link_url = job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")
    print()
"""