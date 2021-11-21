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
                "<code>/connect groupid</code>\n\n",
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
            await message.reply_text("<b>പറ്റിക്കാൻ നോക്കല്ലേ രാമാ...ആദ്യം ADMIN ആയിട്ട് വാ!</b>", quote=True)
            return
    except Exception as e:
        print(e)
        await message.reply_text(
            "<b>ID തെറ്റാണ് ബ്രോ.\nഅല്ലെങ്കിൽ ഗ്രൂപ്പിൽ ഞാൻ ഉണ്ടോ എന്ന് നോക്ക്\nSomething Fishy!!</b>",
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
                    f"ആഹാ. **{title}** ൽ CONNECT ആയല്ലോ.",
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
                    "Already <b>CONNECTED</b>!",
                    quote=True
                )
        else:
            await message.reply_text("Add me as an ADMIN in group", quote=True)
    except Exception as e:
        print(e)
        await message.reply_text('Some ERROR occured! TRY AGAIN later.', quote=True)
        return


@Client.on_message((filters.private | filters.group) & filters.command('disconnectit'))
async def deleteconnection(client,message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are ANONYMOUS ADMIN. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == "private":
        await message.reply_text("Run /connections to VIEW or DISCONNECT from groups!", quote=True)

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
            await message.reply_text("This chat isn't CONNECTED to me!\nDo /connect to CONNECT.", quote=True)


@Client.on_message(filters.private & filters.command(["myconnections"]))
async def connections(client,message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "CONNECT SOME GROUP FIRST!",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            act = " - ACTIVE" if active else ""
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
            "Your connected group details ;\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
