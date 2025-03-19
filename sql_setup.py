#pip install mysql
#pip install mysql-connector-python

import mysql.connector
import getpass

# Establish connection
conn = mysql.connector.connect(
    host = "localhost",                                                     # MySQL server host (e.g., 'localhost' or IP)
    user = "root",                                                          # MySQL username (e.g., 'root')
    password = getpass.getpass("Enter your password: "),                    # My MySQL password
    database ="scrape",
    port = 3306                                                             # MY database name
)
print("Connected to MySQL successfully!")

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS google_news (
    thumbnail_data LONGBLOB NOT NULL,
    thumbnail_url TEXT NOT NULL,
    headline VARCHAR(255) NOT NULL UNIQUE,
    headline_url TEXT NOT NULL,
    scrape_timestamp DATETIME NOT NULL,
    article_date TEXT NOT NULL
);
''')
# "headline VARCHAR(255) NOT NULL UNIQUE"
# This handel the de-duplication constraint,(as mention in Q.5) based on headline,but that’s not the best.
conn.commit()

def insert_news(thumbnail_data, thumbnail_url, headline, headline_url, scrape_timestamp, article_date):    
    try:
        cursor.execute('''
            INSERT IGNORE INTO google_news
            (thumbnail_data, thumbnail_url, headline, headline_url, scrape_timestamp, article_date) 
            VALUES (%s, %s, %s, %s, %s, %s);
        ''', (thumbnail_data, thumbnail_url, headline, headline_url, scrape_timestamp, article_date))
        conn.commit()

    except mysql.connector.Error as err:
        print("Error", err)

# close connection
def close_connection():
    cursor.close()
    conn.close()