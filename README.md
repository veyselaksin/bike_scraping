# Bike Scraping

### About site
This site is a bicycle wholesaler site. People can buy bikes, bike parts or accessory for themselves.
Visit site: [erdoganlarbisiklet.com](https://www.erdoganlarbisiklet.com/)

**Note:** You should change your E-Mail address, enable drive and gsheet api on GCP (Google Cloud Platform).

### About project
This project developed in Python3.
I used scrapy framework for this project (you can access this [link](https://scrapy.org/)) and I crawl some information about pages. I'm storing data as dictionary into output/crawl_output.csv file. I prefer to store the data as a dictionary as I can easily watch it.

## Download and use
Firsting first;
install scrapy for your machine
```
pip install scrapy
```
Download my codes
```
git clone https://github.com/veyselaksin/bike_scraping.git
```
File location
```
cd bike_scraping/bike_scraping
```
Run project
```
scrapy crawl erdoganlarbike -O output/crawl_output.csv
```
See output after the scraping 🚡
```
cat output/crawl_output.csv
```
