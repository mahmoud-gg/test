from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("APP_ID"))
API_HASH = getenv("APP_HASH")

BOT_TOKEN = getenv("BOT_TOKN")
OWNERID = int(getenv("OWNER_ID"))
