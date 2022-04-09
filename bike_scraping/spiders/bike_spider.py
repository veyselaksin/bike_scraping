import scrapy
from pathlib import Path

from scrapy.utils.project import get_project_settings
from bike_scraping.scripts.links import erdbikelinks


class ErdoganlarBike(scrapy.Spider):
    name = "erdoganlarbike"
    start_urls = erdbikelinks()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Host": "www.robitshop.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    def parse(self, response):
        for products in response.css("li.item"):
            yield{
                "name": products.css("h2.product-name").css("a").attrib["title"],
                "url": products.css("a.product-image").attrib["href"],
                "price": products.css("span.price::text").get().replace("\n", "").replace("\xa0", " ")   
            }

        next_page = response.css("a.next.i-next").attrib["href"]

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)