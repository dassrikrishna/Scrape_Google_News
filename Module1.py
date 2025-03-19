# !pip install selenium
"""Scrape the home page of Google News"""

import os
from scrape import scrape
from selenium import webdriver

# Set up the WebDriver path
os.environ['PATH'] += r"C:\chromedriver"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# driver go through this link
driver.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
driver.implicitly_wait(30)

# Call the scraping function
scrape(driver)

# Close the driver
driver.quit()