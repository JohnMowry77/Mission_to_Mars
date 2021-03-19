from bs4 import BeautifulSoup
from splinter import Browser
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo
from pymongo import MongoClient
import pandas as pd

def scrape():
	executable_path={'executable_path': ChromeDriverManager().install()}
	browser=Browser('chrome', **executable_path, headless=False)

	mars_news= requests.get(mars_news_path)
	browser.visit(mars_news_path)
	sleep(0.5)
	mars_html=browser.html
	soup=BeautifulSoup(mars_html,'html.parser')

	news_title=soup.findAll("div", class_="content_title")
	for title in news_title[1]:
    children = list(title.children) 
    if children:
        first = children[0]
        print(getattr(first, "text")  
              if hasattr(first, "text")
                  else first)
        news_titles.append((getattr(first, "text")
              if hasattr(first, "text")
                  else first))
	news_title=news_titles[0]

	for teaser in mars_news_p[:1]: 
    teaser=list(teaser.children)
    if teaser:
        first=teaser[0]
        print(getattr(first, "text")
              if hasattr(first, "text")
                  else first)
        
        news_paragraph.append((getattr(first, "text")  
              if hasattr(first, "text")
                  else firs
                  t))
    news_paragraph[0]

    return browser

#visit the image_url
    image_url="https://www.jpl.nasa.gov/images?search=&category=Mars"
    
    browser.visit(image_url)
    time.sleep(0.5)
    browser.find_by_css('img.BaseImage').first.click()
    time.sleep(0.25)

    html=browser.html
    soup=BeautifulSoup(browser.html, 'html.parser')
    featured_image_url=soup.find('a', class_='BaseButton')['href']

    return browser

#visit the hemispehere url
    mars_hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)
    time.sleep(.5)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    mars_hem_photos=soup.find_all('div', class_='description')
    mars_hem_photos=soup.find_all('div', class_='description')
#mars_hem_photos
#base_url='https://astrogeology.usgs.gov'

#create empty list to append results

#title_hem=[]
#links=[]
	hemisphere_img_urls=[]
	count=0
#use splinter to find by css 
	class_description=browser.find_by_css("h3")

#iterate throught list: append title and href #append hem_img_urls

	for mars_hem in mars_hem_photos:
    	title=mars_hem.find('h3').text
    	link= mars_hem.find('a')
    	href=link['href']
# use splinter to find href, find_by_tag then click
    	browser.links.find_by_partial_href(href)
    	browser.find_by_tag('h3')[count].click()
    #watch screen
    	time.sleep(0.5)
    
    	count=count+1
    #rerun browser
    	html=browser.html
    	soup_2=BeautifulSoup(html, 'html.parser')
    	mars_img_url=browser.find_by_text('Original')['href']
    #mars_img_url=soup.find('li')['href']
    #print(mars_img_url)
    	hemisphere_dict={
    	"title": title,
    	"img_url": mars_img_url}
    	hemisphere_img_urls.append(hemisphere_dict)
    
    browser.back()
    




#visit space-facts url
	url='https://space-facts.com/mars/'






	