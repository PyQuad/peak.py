import os
from dotenv import load_dotenv

load_dotenv()

if not (DB_URI := os.getenv("DB_URI", default=None)):
    print("DB URI not set!")
    exit(1)

TORTOISE_ORM = {
    "connections": {"default": DB_URI},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}