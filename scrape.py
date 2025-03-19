from datetime import datetime
from zoneinfo import ZoneInfo
from encode_decode import encode_base64
from sql_setup import insert_news
from selenium.webdriver.common.by import By

# Function to scrape news headlines, links, and time
def scrape(driver):
    articles = driver.find_elements(By.TAG_NAME, "article")
    for article in articles:
        a_tags = article.find_elements(By.TAG_NAME, "a")
        for a_tag in a_tags:
            link_text = a_tag.text
            href = a_tag.get_attribute("href")
            if link_text and href:
                time = article.find_element(By.TAG_NAME, "time")
                if time:
                    print("Headline:", link_text)
                    print("LINK:", href)
                    print("Time:", time.text)
                    print("~" * 100)

# Extract the thumbnail and the headline
def headline_thumbnail(driver):
    articles = driver.find_elements(By.TAG_NAME, "article")
    
    for article in articles:
        a_tags = article.find_elements(By.TAG_NAME, "a")
        
        for a_tag in a_tags:
            link_text = a_tag.text
            href = a_tag.get_attribute("href")
            
            if link_text and href:
                thumbnail = article.find_element(By.TAG_NAME, "img")
                
                if thumbnail:
                    thumbnail_url = thumbnail.get_attribute("src")
                    
                    if thumbnail_url and "api" in thumbnail_url:
                        print("Headline:", link_text)
                        print("Headline URL:", href)
                        print("Thumbnail URL:", thumbnail_url)
                        print("~" * 100)

# scrape Headline, url, article date, thumbnail link, data, timestamp and store in my sql
def scrape_store(driver):
    articles = driver.find_elements(By.TAG_NAME, "article")
    
    for article in articles:
        a_tags = article.find_elements(By.TAG_NAME, "a")
        
        for a_tag in a_tags:
            link_text = a_tag.text
            href = a_tag.get_attribute("href")
            
            if link_text and href:
                time = article.find_element(By.TAG_NAME, "time")
                thumbnail = article.find_element(By.TAG_NAME, "img")
                
                if thumbnail and time:
                    thumbnail_url = thumbnail.get_attribute("src")
                    scrape_timestamp = datetime.now(ZoneInfo("Asia/Kolkata")) #.strftime("%Y-%m-%d %H:%M:%S")
                    
                    if thumbnail_url and "api" in thumbnail_url:
                        print("Headline:", link_text)
                        print("Headline URL:", href)
                        print("Article Date:", time.get_attribute("datetime"))
                        print("Thumbnail URL:", thumbnail_url)
                        print("Thumbnail Base64 Data:", encode_base64(thumbnail_url)[:50],"...")
                        print("Scrape Timestamp:", scrape_timestamp)
                        print("~" * 100)
                        
                        insert_news(encode_base64(thumbnail_url), thumbnail_url, link_text, href, scrape_timestamp, time.get_attribute("datetime"))
            