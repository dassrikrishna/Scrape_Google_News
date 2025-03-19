from datetime import datetime
from zoneinfo import ZoneInfo
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
