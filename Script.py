class script(object):
    START_TXT = """<b>Heyy {}.
I'm an High-Tech Telegram Filter Bot :)
Bot was Actually Made for <a href=https://t.me/CinemaGround>Cinema Ground</a>

Add me to your Groups & Enjoy!
Tap <code>Help</code> If you have any Doubt about how to use me in your Groups!</b>"""
    HELP_TXT = """𝐇𝐄𝐋𝐏 : <b>How to use me?</b>

- Add me to your Group, Promote me as an Admin. 
- Subscribe our <a href='https://t.me/CineGround'>Channel</a> , to get access of movies / Series!

That's it! <b>Bot is now Ready!</b>

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    ABOUT_TXT = """🤖 𝐁𝐎𝐓 : <a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡</a>

👨‍💻 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 : <a href=https://t.me/axnzal>𝗛𝗨𝗠𝗔𝗡</a>

📚 𝐋𝐈𝐁𝐑𝐀𝐑𝐘 : <a href=https://github.com/pyrogram/pyrogram>𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠</a>

📝 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄 : <a href=https://www.python.org/>𝗣𝗬𝗧𝗛𝗢𝗡</a>

📡 𝐁𝐎𝐓 𝐒𝐄𝐑𝐕𝐄𝐑 : <a href=http://heroku.com/>𝗛𝗘𝗥𝗢𝗞𝗨</a>

📂 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 : <a href=https://www.mongodb.com/>𝗠𝗢𝗡𝗚𝗢 𝗗𝗕</a>

👣 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : <a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    SOURCE_TXT = """𝐇𝐄𝐋𝐏 : <b>Source Code</b>

- Zayn Bot is a Private Source Project.

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    MANUELFILTER_TXT = """𝐇𝐄𝐋𝐏 : <b>Filters</b>

- Filter is the feature were users can set automated Replies for a particular keyword and Zayn will respond whenever a keyword is found in the message.


𝐍𝐎𝐓𝐄 :

○ <b>Zayn Bot</b> should have Admin.
○ Only <b>Admins</b> can Add filters in the Connected chat.
○ Alert buttons have a limit of <b>64 characters.</b>


𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

○ /filter - <code>Adds a filter in the Connected Chat.</code>
○ /viewfilters - <code>Lists all the filters of the Connected Chat.</code>
○ /delf - <code>Deletes a Specific Filter in the Connected Chat.</code>
○ /delallf - <code>Deletes the whole Filters in the Connected Chat ( For Chat Owner Only ).</code>

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    BUTTON_TXT = """𝐇𝐄𝐋𝐏 : <b>Buttons</b>

- Zayn Supports Both URL and ALERT Inline Buttons.


𝐍𝐎𝐓𝐄 :

○ <b>Zayn Bot</b> supports buttons with any telegram media type.
○ Telegram will not Allows you to send Buttons Without any <b>Content</b>, So Content is Mandatory.
○ Buttons should be properly parsed as <b>Markdown format.</b>


𝐁𝐔𝐓𝐓𝐎𝐍𝐒 𝐔𝐒𝐀𝐆𝐄 :

○ <b>URL Buttons :</b>
<code>[Button Text](buttonurl:https://t.me/XaynBot)</code>

○ <b>Alert Buttons :</b>
<code>[Button Text](buttonalert:This is an Alert message)</code>

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    AUTOFILTER_TXT = """𝐇𝐄𝐋𝐏 : <b>Auto Filter</b>

○ Make me the <b>Admin</b> of your channel if it's private.
○ Make sure that your Channel does not contains <b>Camrips, Porn or Fake </b>files.
○ <b>Forward</b> the last message to me with quotes. I'll Add all the files in that channel to my <b>Data Base.</b>

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    CONNECTION_TXT = """<b>𝐇𝐄𝐋𝐏 : <b>Connections</b>

- Used to connect Bot to PM for managing filters.
- It helps to avoid spamming in groups.


𝐍𝐎𝐓𝐄 :

○ Only admins can Add a connection.
○ Send <code>/connectit</code> in your Group for connecting me to your PM. ( Only After making me Admin )


𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

○ /connectit  - <code>Connect a Particular chat to your PM.</code>
○ /disconnectit  - <code>Disconnect from a Particular Chat.</code>
○ /myconnections - <code>List of all your Connections.</code></b>

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    EXTRAMOD_TXT = """𝐇𝐄𝐋𝐏 : <b>Extra Modules</b>

- These are the Extra Features of Zayn


𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

○ /id - <code>Gets ID of a Specifed User.</code>
○ /info  - <code>Gets Information About a Specifed User.</code>
○ /imdb | /search - <code>Get the Movie Information From Various Sources.</code>

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>
"""
    ADMIN_TXT = """<b>Oh Yeah, Wait for It!</b>"""
    STATUS_TXT = """» 𝗧𝗢𝗧𝗔𝗟 𝗙𝗜𝗟𝗘𝗦 : <code>{}</code>
» 𝗧𝗢𝗧𝗔𝗟 𝗨𝗦𝗘𝗥𝗦 : <code>{}</code>
» 𝗧𝗢𝗧𝗔𝗟 𝗖𝗛𝗔𝗧𝗦 : <code>{}</code>
» 𝗨𝗦𝗘𝗗 𝗦𝗧𝗢𝗥𝗔𝗚𝗘 : <code>{}</code>
» 𝗙𝗥𝗘𝗘 𝗦𝗧𝗢𝗥𝗔𝗚𝗘 : <code>{}</code>

<a href=https://t.me/XaynUpdates>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>"""
    LOG_TEXT_G = """#NewGroup
Group - {}(<code>{}</code>)
Total Members - <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
