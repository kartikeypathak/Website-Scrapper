from nturl2path import url2pathname
from turtle import title
import requests
from bs4 import BeautifulSoup
url = "https://www.datacommons.org/"

# Get the HTML

r = requests.get(url)
htmlContent = r.content
#print(htmlContent)


# Parse HTML

soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#HTML Tree Traversal

title = soup.title
#print(type(title))

#Get all the paragraphs from the page

paras = soup.find_all('p')
#print(paras)

# We can use it for comment

#markup = "<p><!-- this is a comment --></p>"
#soup2 = BeautifulSoup(markup)
#print(type(soup2.p.string))
#exit()


# Find All the elements with class lead

#print(soup.find('p')['class'])
#print(soup.find('p', class_="lead"))


# Get the text from the tags

#print(soup.find('p').get_text())
#print(soup.get_text())

# Get all the links on the page

anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href') != "#"):
        linkText = url +link.get('href')
        all_links.add(link)
        #print(linkText)


dc_main_nav = soup.find(id='dc-main-nav')

#for element in dc_main_nav.stripped_strings:
#    print(element)

for item in dc_main_nav.parents:
    print(item.name)