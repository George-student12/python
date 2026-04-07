import os
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")
ADMIN_ID = os.getenv("ADMIN_ID")
BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {TOKEN}'
  }
