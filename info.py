import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/1ac036573c742678aa556.jpg https://telegra.ph/file/621a74d1af8cfbdff4790.jpg https://telegra.ph/file/5a4a925800855eb33d829.jpg https://telegra.ph/file/8f3e2a5bc00f37225851b.jpg https://telegra.ph/file/ebf62d98952299dcb9ce4.jpg https://telegra.ph/file/4326b5a0d29112e24499d.jpg https://telegra.ph/file/0b0856641cf3961ed81d5.jpg https://telegra.ph/file/9b78e86598c7d8eeb3717.jpg https://telegra.ph/file/4ad4f80160791e5d63697.jpg https://telegra.ph/file/60db926665f264f6428c0.jpg https://telegra.ph/file/1d5ba6a98abad0b319bb8.jpg https://telegra.ph/file/6d6b017925f16a405bf73.jpg https://telegra.ph/file/8ae9361c6e2ee935037bc.jpg https://telegra.ph/file/00345533e093721c4e05f.jpg https://telegra.ph/file/fe01ab373a1f7a2acbc95.jpg https://telegra.ph/file/3ef9472ab689f0f71e8c0.jpg https://telegra.ph/file/2b338841a311036b814c3.jpg https://telegra.ph/file/dc202376b1eced7cd03b7.jpg https://telegra.ph/file/e9ea5453e14aab47ec0ac.jpg https://telegra.ph/file/ac1def5a939f3700e8034.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', 0).split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'CinemaGround')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Requested Film : {query}</b> \n\n🏷📺 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10\n\n<b>@CinemaGround</b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
