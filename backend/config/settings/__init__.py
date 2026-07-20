import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

print("BASE_DIR:", BASE_DIR)

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(BASE_DIR / ".env")  # read .env file

isDev = env("DEBUG")

if isDev:
    from .development import *
else:
    from .production import *