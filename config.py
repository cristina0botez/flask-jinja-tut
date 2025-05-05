from os import environ, path
from json import loads

from dotenv import load_dotenv

# Load variables from .env
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    FLASK_APP = "wsgi.py"
    FLASK_DEBUG = loads(environ.get("FLASK_DEBUG"))
    SECRET_KEY = environ.get("SECRET_KEY")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    PRODUCT_DATA_FILEPATH = f"{BASE_DIR}/data/products.json"
