from .base import *
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

print("BASE_DIR:", BASE_DIR)

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(BASE_DIR / ".env")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["https://csi.khajavali.dev", "csi.khajavali.dev", "www.csi.khajavali.dev"])

print("Production settings loaded. DEBUG is set to False. ALLOWED_HOSTS:", ALLOWED_HOSTS)