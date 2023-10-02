# Import the necessary libraries
from bs4 import BeautifulSoup
import requests

# Specify the URL of the website you want to scrape
url = "https://news.google.com/"

# Make an HTTP request to the website and retrieve the HTML or XML document
response = requests.get(url)

# Parse the document using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the headlines and links from the document
headlines = []
links = []

# Find the container element that contains all of the news headlines and links
container = soup.find("div", {"class": "xrnccd F6Welf R7GTQ keNKEd j7vNaf"})

# Check if the find method returned an element
if container:
    # Iterate over the child elements of the container
    for child in container.children:
        # Check if the child is a headline element
        if child.name == "article" and "DY5T1d" in child["class"]:
            # Find the headline element
            headline_element = child.find("a", {"class": "XlKvRb"})

            # Extract the headline and link from the element
            headline = headline_element["aria-label"]
            link = headline_element["href"]

            # Add the headline and link to the lists
            headlines.append(headline)
            links.append(link)

# Print the number of headlines found
print(f"{len(headlines)} headlines found")

# Print the headlines and links
for i in range(len(headlines)):
    print(headlines[i])
    print(links[i])

# Save the headlines and links to a file
with open("headlines.txt", "w") as f:
    for i in range(len(headlines)):
        f.write(headlines[i] + "\n")
        f.write(links[i] + "\n")
