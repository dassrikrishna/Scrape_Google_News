# !pip install selenium
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver path
os.environ['PATH'] += r"C:\chromedriver"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

driver.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
driver.implicitly_wait(30)

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

# Call the scraping function
scrape(driver)

# Close the driver
driver.quit()