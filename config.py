import os
from pathlib import Path
import dotenv

dotenv.load_dotenv(".env")

SECRET_KEY = os.environ["SECRET_KEY"]
