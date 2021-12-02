#! python3
# parseIt.py - Let's parse some html with Beautiful Soup 4

import bs4
import requests

exampleFile = open('parseIt.html')
soupFile = bs4.BeautifulSoup(exampleFile, features="html.parser")
print("Here\'s the type of object we're opening: \n", type(exampleFile), "\n------------------------")
print("Converting the file to a BS4 object: \n", type(soupFile), "\n------------------------")

elements = soupFile.select('#author')
print("Let\'s select the \'author\' css ID. Returns a list: \n", elements, "\n")
print("We can select the element\'s innerHTML (text) minus the tags: \n", elements[0].getText(), "\n---------------------")
elementsString = str(elements[0])
print("The elements as a string: \n", elementsString, "\n-------------------------")
elemAttrs = elements[0].attrs
print("Display the elements attributes as a dictionary: \n", elemAttrs, "\n-------------------------")


print("Select all the \'p\' tags and pring them: \n--------------------------------------------------------------")
pElements = soupFile.select('p')
for i in pElements:
    print(i.getText(), "\n")