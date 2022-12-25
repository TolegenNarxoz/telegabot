from pyrogram import Client, filters

import yt_dlp
from youtube_search import YoutubeSearch
import requests

import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

APPER="Balos"
OWNER="Balos"
OWNER2="Tolegen"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))
@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(OWNER, url=f"https://telegram.dog/{Config.OWNER}"),
                    InlineKeyboardButton(OWNER2, url=f"https://telegram.dog/{Config.OWNER2}"),

                ]
          ]
        ),
        reply_to_message_id=message.message_id
    )
@Client.on_message(filters.command('about') & filters.private)
async def ss(client, message):
    messages='Маған кез-келген әннің атын /song command көмегімен жіберіңіз және \n Маған кез-келген видео атын /video command көмегімен жіберіңіз'
    await message.reply_text(messages)

@Client.on_message(filters.command('video'))
def ab(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('`Іздеп жатыр... Күте тұрыңыз...`')
    ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4'}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**👎 Ештеңе табылмады басқасын жазып көріңіз !**')
            return
    except Exception as e:
        m.edit(
            "** Видеоның атын  қасына жаз  /video командасы арқылы**"
        )
        print(str(e))
        return
    m.edit("`Бауырым... Жүктеп жатыр... күте тұрыңыз`")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            video_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 <b>Аты:</b> <a href="{link}">{title}</a>\n⌚ <b>Уақыты:</b> <code>{duration}</code>  \n </a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(video_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('**Сізде интернет жасамай тұр**')
        print(e)
    try:
        os.remove(video_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@Client.on_message(filters.command(['song']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('`Іздеп жатыр... Күте тұрыңыз...`')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]


            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
        except Exception as e:
            print(e)
            m.edit('**👎 Ештеңе табылмады басқасын жазып көріңіз  !**')
            return
    except Exception as e:
        m.edit(
            "**Әннің атын  қасына жаз  /song командасы арқылы!**"
        )
        print(str(e))
        return
    m.edit("`Бауырым... Жүктеп жатыр... күте тұр...`")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 <b>Аты:</b> <a href="{link}">{title}</a>\n⌚ <b>Уақыты:</b> <code>{duration}</code>\n</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur,  thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('**Сізде интернет жасамай тұр**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)