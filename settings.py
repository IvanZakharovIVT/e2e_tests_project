import os

from dotenv import load_dotenv


load_dotenv()

TRACKER_USERNAME = os.getenv("TRACKER_USERNAME")
TRACKER_PASSWORD = os.getenv("TRACKER_PASSWORD")

TRACKER_URL = os.getenv("TRACKER_URL", "http://track.nordclan/")
