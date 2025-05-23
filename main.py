import requests, selectorlib, time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

connection = sqlite3.connect("date_temps")

def scrape(url):
    response = requests.get(url)
    source_code = response.text
    return source_code


def extract(source):
    content = selectorlib.Extractor.from_yaml_file("extract.yaml")
    extracted_data = content.extract(source)["temperature"]
    return extracted_data


def store(time, data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO scrape VALUES (?, ?)", (time, data))
    connection.commit()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    extracted_time = time.strftime('%Y-%b-%d-%H-%M-%S')
    store(extracted_time, extracted)