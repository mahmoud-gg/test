import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("APP_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKN", "").strip()
OWNERID = os.getenv("OWNER_ID", "").strip()

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not OWNERID:
    print("No OWNER_ID found. Exiting...")
    raise SystemExit


try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit


    
