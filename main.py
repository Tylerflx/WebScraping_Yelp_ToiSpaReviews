# This is webscraping Toi Spa Review from Yelp Website
from bs4 import BeautifulSoup
import requests
from reviews import scrape_review

name = input('Enter the name you want to see reviews (or hit Enter for all): ')
#add choice all or enter technician name
url = f'https://www.yelp.com/biz/&q={name}' #had been removed real link
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

if __name__ == '__main__':
    lists = soup.find_all('div', class_='review__373c0__13kpL border-color--default__373c0__2oFDT')
    scrape_review(lists)
