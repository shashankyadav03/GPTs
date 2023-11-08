#import all the required libraries
import requests
from bs4 import BeautifulSoup


#Function to scrape web and get data based on user input
def scrape_webdog(user_input):
    #print welcome message
    print("Welcome to the web scraper!")
    #Get the url of the website
    url = "https://www.google.com/search?q=" + user_input + "&tbm=isch"
    #Get the html of the website
    html = requests.get(url)
    #Parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    #Get the images
    images = soup.findAll('img')
    #Get the first image
    first_image = images[0]
    #Get the source of the image
    image_source = first_image['src']
    #Return the image source
    return image_source

#Function to get user input
def get_user_input():
    #Get user input
    user_input = input("Enter your search query: ")
    #Return user input
    return user_input 


#main function 
if __name__ == "__main__":
    #print welcome message
    print("Welcome to the web scraper!")
    #Get user input
    user_input = get_user_input()
    #Scrape the web and get data based on user input
    data = scrape_web(user_input)
    #Print the data
    print(data)
