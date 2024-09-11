import requests
from bs4 import BeautifulSoup
import mysql.connector
import logging

# Configure logging
logging.basicConfig(filename='scraping.log', level=logging.INFO)

try:
    # Database connection
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="novels_db"
    )
    cursor = db.cursor()

    def scrape_novels():
        url = 'https://www.lightnovelpub.com/novels'
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        for novel in soup.find_all(class_='novel-item'):
            try:
                title = novel.find('h3').text.strip()
                description = novel.find('p').text.strip()
                cover_image_url = novel.find('img')['src']
                
                cursor.execute(
                    "INSERT INTO novels (title, description, cover_image_url) VALUES (%s, %s, %s)",
                    (title, description, cover_image_url)
                )
                db.commit()
            except Exception as e:
                logging.error(f"Error processing novel: {e}")

    # Scrape the data
    scrape_novels()

except Exception as e:
    logging.error(f"Error in scraping script: {e}")

finally:
    cursor.close()
    db.close()