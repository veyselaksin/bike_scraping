#!/bin/bash

timer(){
for((i=3; i>0; i--))
    do
        sleep 1
        echo -n "$i "
    done
}

worker(){
	echo "Web Scraping"
	timer
	source venv/bin/activate
	scrapy crawl erdoganlarbike
	timer
	echo "File uploading..."
	python3 bike_scraping/scripts/gsheet.py
	deactivate
}

worker

