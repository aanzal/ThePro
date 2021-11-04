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
PICS = (environ.get('PICS', 'https://upload.wikimedia.org/wikipedia/commons/1/10/Zayn_Wiki_%28cropped%29.jpg https://stylesatlife.com/wp-content/uploads/2020/01/Zayn-Malik-Hairstyles-7.jpg https://wallpapercave.com/wp/wp7600834.jpg https://i.pinimg.com/originals/d8/03/15/d80315d6d07303167782a75177ea7c98.jpg https://images.hdqwalls.com/walls/thumb/zayn-malik-2019-new-wv.jpg https://w0.peakpx.com/wallpaper/789/565/HD-wallpaper-zayn-malik-cool-hair-hot-look.jpg https://i.pinimg.com/originals/22/36/31/22363100e03f3fa6b2d107e1b7ecac65.jpg https://image.winudf.com/v2/image1/Y29tLnNwYXJyb3cuemF5bm1hbGlrd2FsbHBhcGVyX3NjcmVlbl8wXzE1NjEyNjY4NTVfMDg0/screen-0.jpg?fakeurl=1&type=.jpg https://images.wallpapersden.com/image/wxl-zayn-malik-in-2017_58590.jpg https://www.wallpaperkiss.com/wimg/b/118-1186114_big.jpg https://c4.wallpaperflare.com/wallpaper/642/625/149/singers-zayn-malik-black-and-white-english-face-hd-wallpaper-preview.jpg https://www.kolpaper.com/wp-content/uploads/2021/01/Cool-Zayn-Malik-Wallpaper.jpg https://i.pinimg.com/736x/3b/87/27/3b8727b57790039ce52701552343c11c.jpg http://images6.fanpop.com/image/photos/41200000/Zayn-zayn-malik-41239750-640-800.jpg https://cdn.mwallpapers.com/photos/celebrities/music/zayn-malik-2019-new-android-iphone-desktop-hd-backgrounds-wallpapers-1080p-4khd-wallpapers-desktop-background-android-iphone-1080p-4k-gospo.jpg https://64.media.tumblr.com/b0ac56e8ae1d9441964c4fdaa47023e5/872bb8850bfc06f7-29/s640x960/2acc1787e393ee3ea4e5508b0d57c97b4f7acfcf.jpg')).split()

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
