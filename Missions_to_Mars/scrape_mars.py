# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
 
    url = "https://mars.nasa.gov/news/"

    html = browser.html
    soup = bs(html, "html.parser")

    data = soup.find("li", class_="slide")
    title = data.find("div", class_="content_title").a.text
    paragraph = data.find("div", class_="article_teaser_body").text
    

    # Part 2 Mars Images
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url2) 


    html = browser.html

    
    soup = bs(html, "html.parser")

   
    image = soup.find("li", class_="slide").a["data-fancybox-href"]

    
    featured_image_url = "https://www.jpl.nasa.gov" + image
    
    # part 3 Mars Weather
    tweet = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(tweet)

   
    soup = bs(response.text, "html.parser")

    # get the weather tweet with beautiful soup
    weather = soup.find("div", class_="js-tweet-text-container").p.get_text(strip=True)
    
    weather2 = mars_weather.split("pic",1)[0]


    # part 3 Mars facts
    facts = "https://space-facts.com/mars/"

    table = pd.read_html(facts)

    mars_facts_df = table[0]

    mars_facts_df.columns=["parameter", "value"]

    facts_df.set_index("parameter", inplace=True)
    # dataframe to an html 
    facts_html = facts_df.to_html()

    # part 4 Mars hemisphere
    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(h_url)

    html = browser.html

 
    soup = bs(html, "html.parser")

    hemi_data = soup.find_all("div", class_="item")
    
    img_urls = []

    # loop 
    for a in data:
    
        title = a.find("h3").text

        img_url = a.a["href"]
    
        url = "https://astrogeology.usgs.gov" + img_url
    
        response = requests.get(url)

        soup = bs(response.text,"html.parser")
    
        new_url = soup.find("img", class_="wide-image")["src"]
    
        total_url = "https://astrogeology.usgs.gov" + new_url
        
        img_urls.append({"title": title, "img_url": total_url})
        
    # mars data dictionary
    mars_data = {
        "title": title,
        "paragraph" : paragraph,
        "featured_image_url": featured_image_url,
        "mars_weather": weather,
        "facts_table": facts_html,
        "img_urls": img_urls
    }
    browser.quit()

    return mars_data