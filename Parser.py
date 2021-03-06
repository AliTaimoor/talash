from bs4 import BeautifulSoup
import regex
import re

def parser(path):

    path = path.replace("\\", "\\\\")

    headings = []
    
    #If a file is stored on local machine, use this
    with open(path, "rb") as file:
        page = BeautifulSoup(file.read(), "lxml")

    #To get all the headings
    for heading in page.find_all(regex.compile('^h[1-6]$')):    # "'^h[1-6]$'" is the levels of headings ie. h1 indicates heading, h2 subheading, etc...
        headings.append(heading.text.strip())

    return page.title, headings[2:-4], page.get_text()

def pageTitleHead (docId, title, head, dictionary):

    dictionary[docId] = [[title, head[:-4]]]

def urlIndex(docId, url, dictionary):
    dictionary[docId] = [url]
