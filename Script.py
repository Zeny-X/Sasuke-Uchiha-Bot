class script(object):
    
    START_TXT = """<b>ꜱᴀʟᴜᴛᴀᴛɪᴏɴꜱ, ꜰᴇʟʟᴏᴡ ɴɪɴᴊᴀ! {}, <i>{}</i> ✨
    
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ꜱᴀɴᴄᴛᴜᴍ ᴏꜰ ꜱᴀꜱᴜᴋᴇ ᴜᴄʜɪʜᴀ🔮. ꜱᴜᴍᴍᴏɴ ᴍᴇ ɪɴᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏꜰ 🔥 ᴀɴᴅ ᴡɪᴛɴᴇꜱꜱ ᴛʜᴇ ᴘʀᴏᴡᴇꜱꜱ ᴛʜᴀᴛ ʟɪᴇꜱ ᴡɪᴛʜɪɴ🗡. ɪ, ᴛʜᴇ ꜱʜᴀʀᴇʀ ᴏꜰ ᴀɴɪᴍᴇ ᴇᴘɪꜱᴏᴅᴇꜱ, ꜱᴛᴀɴᴅ ʀᴇᴀᴅʏ. ᴇᴍʙᴀʀᴋ ᴏɴ ʏᴏᴜʀ ᴊᴏᴜʀɴᴇʏ ɴᴏᴡ🪄, ᴀꜱ ᴛʜᴇ ꜰʟᴀᴍᴇꜱ ᴏꜰ ᴇxᴄɪᴛᴇᴍᴇɴᴛ ᴀɴᴅ ʟɪɢʜᴛɴɪɴɢ ᴏꜰ ᴀᴅᴠᴇɴᴛᴜʀᴇ ᴀᴡᴀɪᴛ! 🔥⚡</b>"""

    MY_ABOUT_TXT = """★ Server: <a href=https://render.com>Render</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>
★ Language: <a href=https://www.python.org>Python</a>
★ Library: <a href=https://pyrogram.org>Pyrogram</a>"""

    MY_OWNER_TXT = """★ Name: ɪᴛᴀᴄʜɪ ᴜᴄʜɪʜᴀ
★ Username: @Itachiofthekonoha
★ ID: <code>1935368808</code>
★ Country: ɪɴᴅɪᴀ 🇮🇳"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Storage: <code>{}</code> / <code>{}</code>
🚀 Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#New_Group_Robo

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """🌟 ꜱʜᴀᴅᴏᴡ-ꜱᴇᴇᴋᴇʀ {},

ɪ'ᴠᴇ ꜱᴇᴀʀᴄʜᴇᴅ, ʙᴜᴛ ᴛʜᴇ <b>{}</b> ᴇʟᴜᴅᴇꜱ ᴍʏ ɢʀᴀꜱᴘ! 🥲

👉 ᴠᴇɴᴛᴜʀᴇ ɪɴᴛᴏ ᴛʜᴇ ʀᴇᴀʟᴍꜱ ᴏꜰ ɢᴏᴏɢʟᴇ, ᴄᴏɴꜰɪʀᴍɪɴɢ ᴛʜᴇ ᴀᴄᴄᴜʀᴀᴄʏ ᴏꜰ ʏᴏᴜʀ ɪɴᴄᴀɴᴛᴀᴛɪᴏɴ.!
👉 ʀᴇꜰɪɴᴇ ʏᴏᴜʀ ᴛᴇᴄʜɴɪQᴜᴇ ʙʏ ʀᴇᴠɪᴇᴡɪɴɢ ᴛʜᴇ ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ.
👉 ᴛʜᴇ ꜰɪʟᴇ ᴍᴀʏ ɴᴏᴛ ʜᴀᴠᴇ ᴇɴɢʀᴀᴠᴇᴅ ɪᴛꜱ ᴘʀᴇꜱᴇɴᴄᴇ ɪɴ ᴍʏ ꜱᴄʀᴏʟʟꜱ.
👉 ɪᴛ ᴍɪɢʜᴛ ꜱᴛɪʟʟ ʙᴇ ᴄᴏɴᴄᴇᴀʟᴇᴅ ɪɴ ᴛʜᴇ ꜱʜᴀᴅᴏᴡꜱ, ᴀᴡᴀɪᴛɪɴɢ ʀᴇʟᴇᴀꜱᴇ."""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://telegram.me/how_to_download_channel/14>mdisklink.link</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<i>{file_name}</i>

🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫"""

    WELCOME_TEXT = """🔮ꜱɪʟʜᴏᴜᴇᴛᴛᴇ {mention} ✨, ᴠᴇɴᴛᴜʀᴇ ɪɴᴛᴏ ᴛʜᴇ ʀᴇᴀʟᴍ ᴏꜰ {title} Begin Your Anime Odyssey With Me! 🔥⚡"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 🌟</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>🪄ᴍᴀꜱᴛᴇʀ ᴛʜᴇ ᴀᴅᴍɪɴ ꜱᴋɪʟʟꜱ🪄
/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels</b>"""
    
    USER_COMMAND_TXT = """<b>🗡ᴇᴍʙᴀʀᴋ ᴏɴ ʏᴏᴜʀ ɴɪɴᴊᴀ ᴘᴀᴛʜ ᴡɪᴛʜ ᴛʜᴇꜱᴇ ꜱʜɪɴᴏʙɪ ꜱᴄʀᴏʟʟꜱ🗡

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/openai - Find solution to any question with ChatGPT</b>"""

    SOURCE_TXT = """<b>-🔗𝗦𝗛𝗔𝗥𝗜𝗡𝗚𝗔𝗡 𝗖𝗢𝗗𝗘 -

- ☯ᴡɪᴛɴᴇꜱꜱ ᴛʜᴇ ʜɪᴅᴅᴇɴ ᴀʀᴛꜱ ɪɴ ᴛʜɪꜱ ᴏᴘᴇɴ-ꜱᴏᴜʀᴄᴇ ᴍᴀꜱᴛᴇʀʏ.

- ꜱᴏᴜʀᴄᴇ - <a href=https://github.com/HansakaAnuhas-TG/AutoFilterBot-Beta>ʜᴇʀᴇ</a>

🪄𝗦𝗛𝗜𝗡𝗢𝗕𝗜 𝗖𝗥𝗘𝗔𝗧𝗢𝗥𝗦 -
<a href=https://telegram.me/Hansaka_Anuhas>ʜᴀɴsᴀᴋᴀ</a>
<a href=https://telegram.me/Technicalaks123>ᴀᴋs</a></b>"""
