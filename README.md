# Scientific Reference Creator
#### Video Demo:  <https://www.youtube.com/watch?v=LpdjGh14MgE>
#### Description:
This program creates a customized scientific reference for any PubMed journal article. It works by having the user input a PubMed URL into the program, 
prompting the user to input the desired order of each of the reference components, and finally, the program outputs their customized and formatted reference.

Scientific references typically contain six different components: names of authors, article title, journal name, the year the article was published, volume/page numbers, and a DOI (Digital object identifier). A common template for a scientific reference is as follows:
    > Author1, Author2, Author3. Title of article. journal name. Year published. Volume/Page-numbers. DOI.

However, the above template is only one example of a scientific reference. The order of components can be interchanged, as different journals have different reference formats, and different courses in high school or post-secondary institutions may have different guidelines for how they want scientific references to be formatted.

Whether you are using the information from journal articles for research or other academic purposes, the number of sources you use can grow quite large, oftentimes exceeding 20+ citations. Writing out all of these references yourself can be a tedious and lengthy process, and because you are handling numerous author names, article titles, years, journal names etc., it is easy to make mistakes. Thus, this program allows a user to simply input the URL of any PubMed (Online search engine for biomedical and life sciences literature, containing more than 35 million journal article citations and abstracts) article and the order in which they want their reference to be formatted, and a fully formatted scientific reference will be produced. This project was completed using the following functions: main, get_url, extract_elements, sanitize_authors, and order_components, and the following libraries: Requests, Regular expression operations, and BeautifulSoup.

#### main:
- The main function is at the top of my program. It functions by first asking the user for a Pubmed URL and then calling each of the other functions accordingly.

#### get_url:
- Using the Requests library, I was able to retrieve data from the user's specific PubMed URL. Then, using the library BeautifulSoup for web scraping, I was able to index into the Document Object Model (DOM) of the webpage. I indexed into the appropriate IDs and classes within the webpages DOM which contains all of the components I need to format a reference.

#### extract_elements:
- This function allowed me to index specifically into the appropriate sections of the DOM that contained each of my six required components: author names, title of article, journal name, year published, volume/page numbers and DOI. I looped through the portion of the DOM which contained the desired information and extracted each of the components. I also formatted each of them by stripping whitespace and/or removing unwanted characters and then returned each of the six components in a string.

### sanitize_authors:
- In many PubMed journal articles, each of the authors' names was followed by an affiliation number subscripted over their name. This affiliation number was not part of the reference, so, this function worked to remove the number and any whitespace between author names, so that there was only a comma between each of them.

#### order_components:
- Now that the program has all the components needed to format a scientific reference, we need to ask the user for the order in which they would like their reference components to be displayed, and then output the reference. This function first provides brief instructions on how the user can order their reference using numbers 1 through 6 (with each number corresponding to a certain reference component), and then asks the users for their input. The user's input links back to a dictionary within this function that uses the numbers 1-6 as keys that are paired to the values of the six reference components specific to the inputted journal article URL. Finally, the customized order of the user's scientific reference is returned and then printed in the terminal via the main function.

In this project folder, there are three files. One of which is this README file, then there is the file project.py which contains the program code, and finally, there is a file called test_project.py which uses unit tests to test each of the functions in the program.
