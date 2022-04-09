from pathlib import Path
from .textreader import textreader
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

BASE_DIR= settings.get("BASE_DIR")
ERD_BIKE_LIST = Path.joinpath(BASE_DIR, "assets/erdoganlarbikelist.txt")

def erdbikelinks():
    bike_item = textreader(file=ERD_BIKE_LIST)
    return bike_item
    