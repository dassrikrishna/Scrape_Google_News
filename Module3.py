"""Extract the thumbnail and the headline of every story from Top Stories page."""

import os
from scrape import headline_thumbnail
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\chromedriver"
driver = webdriver.Chrome()

driver.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
driver.implicitly_wait(30)

a_tags = driver.find_elements(By.TAG_NAME, "a")
for a_tag in a_tags:
    if "Top stories" in a_tag.text:
        top_stories_link = a_tag.get_attribute("href")
        
#print("Top Stories link :", top_stories_link)

# driver go through this link 
driver.get(top_stories_link)

# use scrape  from Module1 to scrape "Top Stories link"
headline_thumbnail(driver)

driver.quit()