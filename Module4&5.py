import os
from selenium import webdriver
from scrape import scrape_store
from selenium.webdriver.common.by import By
from sql_setup import close_connection

os.environ['PATH'] += r"C:\chromedriver"
driver = webdriver.Chrome()

driver.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
driver.implicitly_wait(30)

a_tags = driver.find_elements(By.TAG_NAME, "a")
for a_tag in a_tags:
    if "Top stories" in a_tag.text:
        top_stories_link = a_tag.get_attribute("href")
        
#print("Top Stories link :", top_stories_link)

driver.get(top_stories_link)
scrape_store(driver)

driver.quit()

close_connection()