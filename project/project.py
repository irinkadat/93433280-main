import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

def main():
    """Scrapes news data from a URL and writes it to a CSV file"""
    url = 'http://exclusivenews.ge/post/category/msoflio'
    with open('news.csv', 'w', encoding='UTF-8_sig', newline='\n') as f:
        file = csv.writer(f)
        file.writerow(['Category', 'Title', 'text', 'Image URL'])
        for ind in range(1, 6):
            url_with_page = url + '/page/' + str(ind)
            soup = get_soup(url_with_page)
            news = get_news(soup)
            write_news_to_csv(news, file)
            sleep(randint(15, 20))


def get_soup(url):
    """Fetches the HTML content of a URL and returns a BeautifulSoup object"""
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def get_news(soup):
    """Returns a list of news articles from a BeautifulSoup object"""
    section = soup.find('section', class_='small-12 medium-8 columns equal')
    return section.find_all('article')


def write_news_to_csv(news, file):
    """Writes news data to a CSV file"""
    for each in news:
        category = each.aside.a.text
        title = each.header.h5.a.text
        text = each.p.text
        image_url = each.img.attrs.get('src')
        file.writerow([category, title, text, image_url])



if __name__ == '__main__':
    main()
