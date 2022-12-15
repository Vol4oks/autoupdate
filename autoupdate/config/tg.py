import os
from dotenv import load_dotenv

load_dotenv()
WORK_BOT = os.getenv("WORK_BOT")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMINS = str(os.getenv("ADMINS"))

