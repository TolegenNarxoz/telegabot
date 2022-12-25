import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "23624904"))
    API_HASH = os.environ.get("API_HASH", "28af4f1ca61b3dea3070fcdc3a856adb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5830351956:AAHbzmc83cUk2UZP_mTSvtz_KIUy0m2JIWY")
    START_MSG = os.environ.get("START_MSG", "<b>Cәлем {},\nмен Youtube-тен музыка және видео жүктеуге арналған қарапайым ботмын</b>\n\n")
    START_IMG = os.environ.get("START_IMG", "https://realtyfact.com/wp-content/uploads/2022/10/MP4-from-Youtube.jpg")
    OWNER = os.environ.get("OWNER", "Balos12")
    OWNER2 = os.environ.get("OWNER2", 'tolegen_narxoz')
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
