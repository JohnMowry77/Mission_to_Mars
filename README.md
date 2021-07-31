
# Mission to Mars

![mars_finish_one](https://user-images.githubusercontent.com/72773479/127752113-99082f46-78d4-4d66-b850-b2638eca561d.png)

![mars_finish_three](https://user-images.githubusercontent.com/72773479/127752114-975f1935-78d7-4e90-8856-a3e959b8dc15.png)
![mars_finish_two](https://user-images.githubusercontent.com/72773479/127752115-25a8f1fc-7ddc-4487-9aa7-066733f9a5f2.png)

This project involed building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.* Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data. Used Pymongo for CRUD applications for the database. The data is overwritten each time the `/scrape` url is visited and new data is obtained. Used Bootstrap to structure the HTML template.

The following outlines what the process is from start to finish:

### Start here:

1. Create a new repository for this project called `web-scraping-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. Inside your local git repository, create a directory for the web scraping challenge. Use a folder name to correspond to the challenge: **Missions_to_Mars**.

4. Add your notebook files to this folder as well as your flask app.

5. Push the above changes to GitHub or GitLab.

## Step 1 - Scraping

The process involved scrapping various html pages using Jupyter Notebook (JN), BeautifulSoup, Pandas, and Requests/Splinter. 
* Created a JN file called `mission_to_mars.ipynb` and used this to complete all of the scraping and analysis tasks. The following outlines what html pages are scraped. 

### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Make sure to find the image url to the full size `.jpg` image.

* Make sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import `scrape_mars.py` script and call `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements.

![Capture](Images/final_app_part1.png)
![Capture](Images/final_app_part2.png)

![mars_color](https://user-images.githubusercontent.com/72773479/127752153-00a16629-55ab-4fb0-b1c8-9b1fc4b01e1c.jpeg)
![mars_life_2](https://user-images.githubusercontent.com/72773479/127752154-6e2792e4-626a-45e2-9263-4fce8d6b1891.jpeg)
![Mars_life](https://user-images.githubusercontent.com/72773479/127752155-c0745e4c-dae3-449a-bfa6-670624e00c5f.jpg)
![Mars](https://user-images.githubusercontent.com/72773479/127752156-662646c2-c6d3-484d-8e20-24990e90b4b4.jpg)
![mission_to_mars](https://user-images.githubusercontent.com/72773479/127752157-05bea641-1438-4209-bf3c-e8f6a5ea9f49.png)


- - -

### Finish
* The end result will be an html page with an updated featured mars image, facts about mars, and four photos of mars hemishperes (Cerberus, Syrtis Major, Schiaparelli, Valles Marineris).