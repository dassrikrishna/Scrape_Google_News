import os
import logging
from datetime import datetime
from zoneinfo import ZoneInfo
from selenium import webdriver
from encode_decode import encode_base64
from sql_setup import insert_news
from selenium.webdriver.common.by import By

# Configure logging
logging.basicConfig(
    filename="webscraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize WebDriver
def init_driver():
    os.environ["PATH"] += r"C:\chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

# Return 'Top Stories' link
def top_stories(driver):
    try:
        driver.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
        a_tags = driver.find_elements(By.TAG_NAME, "a")
        for a_tag in a_tags:
            if "Top stories" in a_tag.text:
                return a_tag.get_attribute("href")

        logging.warning("Top Stories link not found.")
        return None

    except Exception as e:
        logging.error(f"Error fetching Top Stories link: {e}")
        return None

# Scrape google news store in mysql
def scrape_store(driver):
    try:
        articles = driver.find_elements(By.TAG_NAME, "article")
        for article in articles:
            a_tags = article.find_elements(By.TAG_NAME, "a")

            for a_tag in a_tags:
                link_text, href = a_tag.text, a_tag.get_attribute("href")
                if not link_text or not href:
                    continue

                try:
                    time_element = article.find_element(By.TAG_NAME, "time")
                    thumbnail_element = article.find_element(By.TAG_NAME, "img")

                    if not time_element or not thumbnail_element:
                        continue

                    thumbnail_url = thumbnail_element.get_attribute("src")
                    article_date = time_element.get_attribute("datetime")
                    scrape_timestamp = datetime.now(ZoneInfo("Asia/Kolkata"))

                    if thumbnail_url and "api" in thumbnail_url:
                        logging.info(f"Scraped: {link_text}")

                        print("~" * 100)
                        print(f"Headline: {link_text}")
                        print(f"Headline URL: {href}")
                        print(f"Article Date: {article_date}")
                        print(f"Thumbnail URL: {thumbnail_url}")
                        print(f"Scrape Timestamp: {scrape_timestamp}")
                        
                        print("~" * 100)
                        # insert all data in my sql
                        insert_news(encode_base64(thumbnail_url), thumbnail_url, link_text, href, scrape_timestamp, article_date)

                except Exception as e:
                    logging.error(f"Error processing article: {e}")

    except Exception as e:
        logging.error(f"Error scraping articles: {e}")

def main():
    """Main execution for the scraper."""
    logging.info("Scraper execution started.")
    driver = init_driver()
    try:
        top_stories_link = top_stories(driver)
        if top_stories_link:
            driver.get(top_stories_link)
            scrape_store(driver)
        else:
            logging.warning("Top stories link not found.")
    finally:
        driver.quit()
    logging.info("Scraper execution completed.")

if __name__ == "__main__":
    main()
