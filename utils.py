import logging
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from info import AUTH_CHANNEL, LONG_IMDB_DESCRIPTION
from imdb import Cinemagoer
import asyncio
from pyrogram.types import Message, InlineKeyboardButton, ChatJoinRequest
from pyrogram import enums
import os
import pytz
import time
from datetime import datetime
from typing import List, Any, Union, Optional, AsyncGenerator
from database.users_chats_db import db
from shortzy import Shortzy

imdb = Cinemagoer() 

# temp db for banned 
class temp(object):
    START_TIME = 0
    BANNED_USERS = []
    BANNED_CHATS = []
    ME = None
    CANCEL = False
    U_NAME = None
    B_NAME = None
    SETTINGS = {}
    FILES = {}
    USERS_CANCEL = False
    GROUPS_CANCEL = False
    BOT = None

async def is_subscribed(bot, query, channel=AUTH_CHANNEL):
    btn = []
    for id in channel:
        chat = await bot.get_chat(id)
        try:
            await bot.get_chat_member(id, query.from_user.id)
        except UserNotParticipant:
            btn.append(
                [InlineKeyboardButton(f'Join {chat.title}', url=chat.invite_link)]
            )
        except Exception as e:
            logger.exception(e)
    return btn

async def get_poster(query, bulk=False, id=False, file=None):
    if not id:
        query = (query.strip()).lower()
        title = query
        year = re.findall(r'[1-2]\d{3}$', query, re.IGNORECASE)
        if year:
            year = list_to_str(year[:1])
            title = (query.replace(year, "")).strip()
        elif file is not None:
            year = re.findall(r'[1-2]\d{3}', file, re.IGNORECASE)
            if year:
                year = list_to_str(year[:1]) 
        else:
            year = None
        movieid = imdb.search_movie(title.lower(), results=10)
        if not movieid:
            return None
        if year:
            filtered=list(filter(lambda k: str(k.get('year')) == str(year), movieid))
            if not filtered:
                filtered = movieid
        else:
            filtered = movieid
        movieid=list(filter(lambda k: k.get('kind') in ['movie', 'tv series'], filtered))
        if not movieid:
            movieid = filtered
        if bulk:
            return movieid
        movieid = movieid[0].movieID
    else:
        movieid = query
    movie = imdb.get_movie(movieid)
    if movie.get("original air date"):
        date = movie["original air date"]
    elif movie.get("year"):
        date = movie.get("year")
    else:
        date = "N/A"
    plot = ""
    if not LONG_IMDB_DESCRIPTION:
        plot = movie.get('plot')
        if plot and len(plot) > 0:
            plot = plot[0]
    else:
        plot = movie.get('plot outline')
    if plot and len(plot) > 800:
        plot = plot[0:800] + "..."

    return {
        'title': movie.get('title'),
        'votes': movie.get('votes'),
        "aka": list_to_str(movie.get("akas")),
        "seasons": movie.get("number of seasons"),
        "box_office": movie.get('box office'),
        'localized_title': movie.get('localized title'),
        'kind': movie.get("kind"),
        "imdb_id": f"tt{movie.get('imdbID')}",
        "cast": list_to_str(movie.get("cast")),
        "runtime": list_to_str(movie.get("runtimes")),
        "countries": list_to_str(movie.get("countries")),
        "certificates": list_to_str(movie.get("certificates")),
        "languages": list_to_str(movie.get("languages")),
        "director": list_to_str(movie.get("director")),
        "writer":list_to_str(movie.get("writer")),
        "producer":list_to_str(movie.get("producer")),
        "composer":list_to_str(movie.get("composer")) ,
        "cinematographer":list_to_str(movie.get("cinematographer")),
        "music_team": list_to_str(movie.get("music department")),
        "distributors": list_to_str(movie.get("distributors")),
        'release_date': date,
        'year': movie.get('year'),
        'genres': list_to_str(movie.get("genres")),
        'poster': movie.get('full-size cover url'),
        'plot': plot,
        'rating': str(movie.get("rating")),
        'url':f'https://www.imdb.com/title/tt{movieid}'
    }


async def iter_messages(client, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[AsyncGenerator["types.Message", None]]:
    """Iterate through a chat sequentially.
    This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
    you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
    single call.
    Parameters:
        chat_id (``int`` | ``str``):
            Unique identifier (int) or username (str) of the target chat.
            For your personal cloud (Saved Messages) you can simply use "me" or "self".
            For a contact that exists in your Telegram address book you can use his phone number (str).
                
        limit (``int``):
            Identifier of the last message to be returned.
                
        offset (``int``, *optional*):
            Identifier of the first message to be returned.
            Defaults to 0.
    Returns:
        ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
    Example:
        .. code-block:: python
            for message in app.iter_messages("pyrogram", 1, 15000):
                print(message.text)
    """
    current = offset
    while True:
        new_diff = min(200, limit - current)
        if new_diff <= 0:
            return
        messages = await client.get_messages(chat_id, list(range(current, current+new_diff+1)))
        for message in messages:
            yield message
            current += 1


async def is_check_admin(bot, chat_id, user_id):
    try:
        member = await bot.get_chat_member(chat_id, user_id)
        return member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]
    except:
        return False


async def get_verify_status(user_id):
    verify = await db.get_verify_status(user_id)
    return verify

async def update_verify_status(user_id, verify_token="", is_verified=False, verified_time=0, link=""):
    current = await get_verify_status(user_id)
    current['verify_token'] = verify_token
    current['is_verified'] = is_verified
    current['verified_time'] = verified_time
    current['link'] = link
    await db.update_verify_status(user_id, current)
    
    
async def broadcast_messages(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return "Success"
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await broadcast_messages(user_id, message)
    except Exception as e:
        await db.delete_user(int(user_id))
        return "Error"

async def groups_broadcast_messages(chat_id, message):
    try:
        k = await message.copy(chat_id=chat_id)
        try:
            await k.pin()
        except:
            pass
        return "Success"
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await groups_broadcast_messages(chat_id, message)
    except Exception as e:
        await db.delete_chat(chat_id)
        return "Error"

async def get_settings(group_id):
    settings = temp.SETTINGS.get(group_id)
    if not settings:
        settings = await db.get_settings(group_id)
        temp.SETTINGS.update({group_id: settings})
    return settings
    
async def save_group_settings(group_id, key, value):
    current = await get_settings(group_id)
    current.update({key: value})
    temp.SETTINGS.update({group_id: current})
    await db.update_settings(group_id, current)

def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def list_to_str(k):
    if not k:
        return "N/A"
    elif len(k) == 1:
        return str(k[0])
    else:
        return ' '.join(f'{elem}, ' for elem in k)
    
async def get_shortlink(url, api, link):
    shortzy = Shortzy(api_key=api, base_site=url)
    link = await shortzy.convert(link)
    return link

def get_readable_time(seconds):
    periods = [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    result = ''
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            result += f'{int(period_value)}{period_name}'
    return result

def get_wish():
    tz = pytz.timezone('Asia/Colombo')
    time = datetime.now(tz)
    now = time.strftime("%H")
    if now < "12":
        status = "ꜱʜᴀᴅᴏᴡ'ꜱ ᴅᴀᴡɴ 🌄"
    elif now < "18":
        status = "ᴅᴀʏ'ꜱ ᴅᴇꜱᴄᴇɴᴛ 🌇"
    else:
        status = "ᴇᴠᴇɴɪɴɢ ᴡʜɪꜱᴘᴇʀꜱ 🌆"
    return status

def get_media_from_message(message: "Message") -> Any:
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media

def get_hash(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_unique_id", "")[:6]
