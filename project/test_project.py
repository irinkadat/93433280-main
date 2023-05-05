import csv
import requests
from bs4 import BeautifulSoup
from project import get_soup, get_news, write_news_to_csv


def test_get_soup():
    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    soup = get_soup(url)
    assert isinstance(soup, BeautifulSoup)


def test_get_news():
    html = '<section class="small-12 medium-8 columns equal"><article></article><article></article></section>'
    soup = BeautifulSoup(html, 'html.parser')
    news = get_news(soup)
    assert len(news) == 2


def test_write_news_to_csv(tmp_path):
    news = [
        {'Category': 'Sports', 'Title': 'New record set in marathon', 'Text': '...', 'Image URL': 'https://example.com/image1.jpg'},
        {'Category': 'Politics', 'Title': 'Election results announced', 'Text': '...', 'Image URL': 'https://example.com/image2.jpg'}
    ]
    filepath = tmp_path / 'test.csv'
    with open(filepath, 'w', encoding='UTF-8_sig', newline='') as f:
        fieldnames = ['Category', 'Title', 'Text', 'Image URL']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for article in news:
            writer.writerow(article)
    with open(filepath, newline='', encoding='utf-8-sig') as f:
        assert f.readline().strip() == 'Category,Title,Text,Image URL'
        assert f.readline().strip() == 'Sports,New record set in marathon,...,https://example.com/image1.jpg'
        assert f.readline().strip() == 'Politics,Election results announced,...,https://example.com/image2.jpg'
