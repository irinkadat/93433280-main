## exclusivenews scraping-parsing

## Author

- [@irinkadat](https://github.com/irinkadat)


## Description
Exclusivenews Scraping-Parsing is a Python script that allows you to extract news articles from the Exclusivenews.ge website using web scraping techniques. The script sends requests to the website and extracts information such as photo URLs, news categories, titles, and descriptions, and saves them to a CSV file.

The script is designed to run for a specified amount of time and scrape multiple pages of news articles. This means that it can extract a large amount of data over an extended period. This data can be useful for a variety of purposes, such as market research, trend analysis, or news aggregation.

The script uses the Requests module to send HTTP requests to the website and the BeautifulSoup module to parse the HTML responses. It also uses the Random module to wait for a random amount of time between requests to avoid overloading the website's server. The Time module is used to set the duration of the scraping process and to measure the time taken to scrape each page of articles.


## Used Resources
- exclusivenews [link](http://exclusivenews.ge/post/category/msoflio/page/1)
- Requests Module
- bs4 module
- random module
- time module

## Instalations
1. Install the requests library:
``` pip install requests ```
2. Install the BeautifulSoup library:
```pip install beautifulsoup4```

## Usage
1. Open a terminal window and navigate to the project directory.
2. Run the command:
```python project.py```
3. The script will output the scraped news articles and save them to a CSV file.

## Running Tests
1. Open a terminal window and navigate to the project directory.
2. Run the command:
```pytest test_project.py```

