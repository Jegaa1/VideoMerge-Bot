# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID", "1923471")
    API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5824947866:AAEt_buKW6b2KpCmn-ZTKuG9qRuln_g9V9k")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 10))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Erichdaniken:Erichdaniken@cluster0.vhu3d.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 880087645))

    START_TEXT = """
Hi Sir, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @JAsuran2p0
"""
    CAPTION = ""
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
