from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)


browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
page = browser.html


soup = BeautifulSoup(page, 'html.parser')

x = soup.find_all('div', class_='item')


def get_img_url(url_to_visit):
    browser.visit(url_to_visit)
    a = BeautifulSoup(browser.html, 'html.parser').find_all('a', target='_blank')
    for i in a:
        if i.text=='Sample':
            return i.get('href')

hemisphere_urls = []
for i in soup.find_all('div', class_='item'):
    to_visit = 'https://astrogeology.usgs.gov' + i.find('a',class_='itemLink product-item').get('href')
    desc = i.find('h3').text
    url = get_img_url(to_visit)
    hemisphere_urls.append({'img_url':url, 'title':desc})


browser.quit()
hemisphere_urls



