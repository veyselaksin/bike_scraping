from __future__ import print_function

from pathlib import Path
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import json
from datetime import datetime
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

BASE_DIR = settings.get("BASE_DIR")
CONFIG = Path.joinpath(BASE_DIR, "assets/config.json")
CRAWL_OUTPUT = Path.joinpath(BASE_DIR, "output/crawl_output.csv")

with open(CONFIG) as config_file:
    config = json.load(config_file)

SCOPES = config["gsheet"]["scopes"] 
SERVICE_ACCOUNT_FILE = Path.joinpath(BASE_DIR, "assets/service_account.json")

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def gsheet_service():
    return build("sheets", "v4", credentials= credentials)

def drive_service():
    return build("drive", "v3", credentials= credentials)


def create_folder():
    """
    Creates a folder and upload a file to it
    """
    dservice = drive_service()

    folder_meta = {
        'name': "Scrapy",
        'mimeType': 'application/vnd.google-apps.folder'
    }

    permission_user = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': config["gsheet"]["email"] 
    }

    file = dservice.files().create(body=folder_meta, fields="id").execute()
    folder_id = file.get("id")
    dservice.permissions().create(fileId=folder_id, body=permission_user, fields="id").execute()
    print("Folder: {}".format(folder_id))


def upload_file():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    try:
        title = f"Erdoğanlar Bisiklet - {datetime.now().strftime('%Y/%M/%d')}"
        dservice = drive_service()

        file_meta = {
            'name': title,
            'parents': [config["gsheet"]["folder_id"]]
        }
        
        media = MediaFileUpload(CRAWL_OUTPUT, resumable=False)
        file = dservice.files().create(body=file_meta, media_body=media, fields="id").execute()
        print("File: {}".format(file.get("id")))


    except HttpError as err:
        print(err)


upload_file()
# create_folder()