from bs4 import BeautifulSoup
from splinter import Browser
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo
from pymongo import MongoClient
mongo_conn=pymongo.MongoClient('mongodb://localhost:27017')
mars_db_one = mongo_conn["mars_db_one"]
mars_info = mars_db_one["mars"]
import pandas as pd


# mars_dict={}

def init_browser():
    # Chromedriver path
    executable_path={'executable_path': ChromeDriverManager().install()}
    #init_browser function must return the browser to pass through to other functions
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    from bs4 import BeautifulSoup
    from splinter import Browser
    import time
    import pandas as pd

    mars_dict={}
    # allows you to re-use browser
    browser= init_browser()

    
    mars_news_path='https://mars.nasa.gov/news/'
    #print("I am running")
    browser.visit(mars_news_path)
    time.sleep(0.5)
    mars_html=browser.html
    # Use soup to get the mars title & teaser for the first article
    soup=BeautifulSoup(mars_html,'html.parser')
    
    news_title=soup.findAll("div", class_="content_title")
    news_title=news_title[1].text
    mars_news_p=soup.find_all("div", class_="article_teaser_body")
    mars_news_p=mars_news_p[0].text

    #append news_title & mars_news_p to mars_dict dictionary using 'news_title' & 'news_p' as keys
    mars_dict['news_title']=news_title
    mars_dict['news_p']=mars_news_p
    #print(mars_news_p)

    # #visit the  mars image_url
    image_url="https://www.jpl.nasa.gov/images?search=&category=Mars"
    
    browser.visit(image_url)
    time.sleep(0.5)
    browser.find_by_css('img.BaseImage').click()
    time.sleep(0.25)

    html=browser.html
    soup=BeautifulSoup(browser.html, 'html.parser')
    featured_image_url=soup.find_all("img", class_="BaseImage")
    #returns a list, grab by index integer
    featured_image_url=(featured_image_url[0]['src'])
    #print(featured_image_url)

    #append mars_image to mars_dict, use 'image_tag'as key
    mars_dict['image_tag']=featured_image_url

    #Scrape Mars facts table from website
    url='https://space-facts.com/mars/'
    #use pandas to create a table
    tables = pd.read_html(url)
    mars_facts=tables[0]
    #rename columns & set index to first column
    mars_facts=mars_facts.rename(columns=({0: "Metric", 1: "Measurement"}))
    mars_facts=mars_facts.set_index('Metric')
    #export table to html string
    mars_facts=mars_facts.to_html()
    #print(mars_facts)

    #append mars_facts to mars_dict, use "mars_facts" as key

    mars_dict['mars_facts']=mars_facts

    # visit the hemispehere url 
    mars_hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)
    time.sleep(.5)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    mars_hem_photos=soup.find_all('div', class_='description')
    #create empty list to append results
    hemisphere_img_urls=[]
    count=0
    #use splinter to find by css 
    class_description=browser.find_by_css("h3")
    #iterate throught list: append title and href #append hem_img_urls
    for mars_hem in mars_hem_photos:
        title=mars_hem.find('h3').text
        link= mars_hem.find('a')
        href=link['href']
        #use splinter to find href, find_by_tag then click
        browser.links.find_by_partial_href(href)
        browser.find_by_tag('h3')[count].click()
        #watch screen
        time.sleep(0.5)

        count=count+1
        html=browser.html
        soup_2=BeautifulSoup(html, 'html.parser')
        mars_img_url=browser.find_by_text('Original')['href']
        hemisphere_dict={"title": title, "img_url": mars_img_url}
        hemisphere_img_urls.append(hemisphere_dict)
        #append hemisphere img urls to mars_dict, use 'hemispheres' as the key
        mars_dict['hemispheres']=hemisphere_img_urls

    #Close the browser after scraping
    browser.quit()

    #return mars_dict which has the scraped values
    return mars_dict
    # print(mars_dict)

#     return mars_dict
#     mars_db_one.mars_info.insert_one(mars_dict)


if __name__ == "__main__":
    scrape()





	