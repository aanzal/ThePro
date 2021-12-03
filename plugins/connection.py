from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.connections_mdb import add_connection, all_connections, if_active, delete_connection
from info import ADMINS

@Client.on_message((filters.private | filters.group) & filters.command('connectit'))
async def addconnection(client,message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are ANONYMOUS admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == "private":
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>Enter in correct format!</b>\n\n"
                "<code>/connectit groupid</code>\n\n",
                quote=True
            )
            return

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            await message.reply_text("<b>Try not to fool me!\nFirst be an Admin in this Group!</b>", quote=True)
            return
    except Exception as e:
        print(e)
        await message.reply_text(
            "<b>Error</b>\n\n× Maybe the ID you have given is Wrong!\n**<i>OR</i>**\n× Check i'm in this group. If not, Add me by Clicking <a href='http://t.me/XaynBot?startgroup=true'>Here</a> & Make me admin!",
            quote=True,
        )

        return
    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == "administrator":
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Successfully Connected to **{title}**\n\n❣️ From 𝗭𝗮𝘆𝗻",
                    quote=True,
                    parse_mode="md"
                )
                if chat_type in ["group", "supergroup"]:
                    await client.send_message(
                        userid,
                        f"Connected to **{title}** !",
                        parse_mode="md"
                    )
            else:
                await message.reply_text(
                    "Already <b>Connected</b>!",
                    quote=True
                )
        else:
            await message.reply_text("Add me as an ADMIN in this group", quote=True)
    except Exception as e:
        print(e)
        await message.reply_text('Some ERROR occured! TRY AGAIN later.', quote=True)
        return


@Client.on_message((filters.private | filters.group) & filters.command('disconnectit'))
async def deleteconnection(client,message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are ANONYMOUS ADMIN. Use /connectit {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == "private":
        await message.reply_text("Run /myconnections to VIEW or DISCONNECT from groups!", quote=True)

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("Successfully DISCONNECTED from this chat", quote=True)
        else:
            await message.reply_text("This chat isn't CONNECTED to me!\nDo /connectit to CONNECT.", quote=True)


@Client.on_message(filters.private & filters.command(["myconnections"]))
async def connections(client,message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "<b>Connect Some Group First!</b>",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            act = " - Active" if active else ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "**Your connected group details :**\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
