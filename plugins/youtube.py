from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import get_bot_information
from database import set_db_wait
from utils import commands
from urllib.parse import urlparse
import os
import asyncio
import yt_dlp
from youtube_search import YoutubeSearch
from requests import get


# yt-dlp options - fixed format + android client to bypass JS runtime & 429
ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio[ext=mp3]/bestaudio/best',
    'outtmpl': '/tmp/%(id)s.%(ext)s',
    'writethumbnail': True,
    'quiet': True,
    'no_warnings': True,
    'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/100.0.4896.127 Mobile Safari/537.36',
    },
    'sleep_interval': 2,
    'max_sleep_interval': 5,
    'retries': 3,
}

ydl_opts_video = {
    'format': 'best[ext=mp4][filesize<50M]/best[filesize<50M]/best',
    'outtmpl': '/tmp/%(id)s.%(ext)s',
    'writethumbnail': True,
    'quiet': True,
    'no_warnings': True,
    'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/100.0.4896.127 Mobile Safari/537.36',
    },
    'sleep_interval': 2,
    'retries': 3,
}


@Client.on_callback_query(filters.regex(r"^youtube (\d+)$"))
async def youtube_main(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("نتائج اليوتوب 🔍", callback_data="ntagyout " + str(m.from_user.id))] +
        [InlineKeyboardButton("تحميل من الرابط 🔗", callback_data="downyout " + str(m.from_user.id))],
        [InlineKeyboardButton("بحث صوت 🎵", callback_data="searchyout " + str(m.from_user.id))] +
        [InlineKeyboardButton("بحث فديو 🎬", callback_data="searchyoutvideo " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الى مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بك في قائمة اليوتيوب\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex(r"^ntagyout (\d+)$"))
async def ntagyout(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر", show_alert=True)
        return
    set_db_wait("ntagyoutube", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ ماذا تريد انا ابحث لك...\n√")


@Client.on_callback_query(filters.regex(r"^downyout (\d+)$"))
async def downyout(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر", show_alert=True)
        return
    set_db_wait("downyout", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ ارسل لى الرابط الان وساقوم بتحميله لك...\n√")


@Client.on_callback_query(filters.regex(r"^searchyout (\d+)$"))
async def searchyout(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر", show_alert=True)
        return
    set_db_wait("searchyout", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ ارسل لى اسم الاغنيه وساجلبها لك...\n√")


@Client.on_callback_query(filters.regex(r"^searchyoutvideo (\d+)$"))
async def searchyoutvideo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر", show_alert=True)
        return
    set_db_wait("searchyoutvideo", m.from_user.id, m.message.chat.id)
    await m.message.edit_text("◍ ارسل لى اسم الفديو وساجلبه لك...\n√")


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    parts = basename.split(".")
    return parts[-1] if len(parts) > 1 else "jpg"


def _find_file(base, extensions):
    for ext in extensions:
        candidate = base + '.' + ext
        if os.path.exists(candidate):
            return candidate
    return None


def download_audio_sync(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        base = '/tmp/' + info['id']
        audio_file = _find_file(base, ['m4a', 'mp3', 'opus', 'ogg', 'webm', 'weba'])
        if not audio_file:
            audio_file = ydl.prepare_filename(info)
        thumb_file = _find_file(base, ['jpg', 'jpeg', 'png', 'webp'])
        return audio_file, thumb_file, info


def download_video_sync(url):
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
        info = ydl.extract_info(url, download=True)
        base = '/tmp/' + info['id']
        video_file = _find_file(base, ['mp4', 'mkv', 'webm'])
        if not video_file:
            video_file = ydl.prepare_filename(info)
        thumb_file = _find_file(base, ['jpg', 'jpeg', 'png', 'webp'])
        return video_file, thumb_file, info


def _err_msg(e):
    err = str(e)
    if "429" in err or "Too Many Requests" in err:
        return "◍ يوتيوب يرفض الطلب الان بسبب كثرة الطلبات، حاول بعد دقيقتين\n√"
    if "requested format" in err:
        return "◍ هذه الاغنيه مساحتها كبيره جداا\n√"
    if "Video unavailable" in err or "Private video" in err:
        return "◍ الفيديو غير متاح\n√"
    return f"◍ خطأ: {err[:300]}\n√"


async def downfromlink(message: Message):
    m = await message.reply_text("◍ جارى تحميل الصوت...\n√", disable_web_page_preview=True)
    audio_file = thumb_file = None
    try:
        loop = asyncio.get_event_loop()
        audio_file, thumb_file, info = await loop.run_in_executor(None, download_audio_sync, message.text.strip())
        if not audio_file or not os.path.exists(audio_file):
            await m.edit("◍ فشل التحميل، حاول مرة اخرى\n√")
            return
        title = info.get('title', 'Unknown')
        performer = info.get('uploader', 'Unknown')
        duration = int(float(info.get('duration', 0)))
        await m.edit("◍ انتظر جارى الرفع....\n√")
        await message.reply_audio(audio_file, caption=title, duration=duration,
                                  performer=performer, title=title, thumb=thumb_file,
                                  reply_to_message_id=message.message_id)
        await m.delete()
    except Exception as e:
        await m.edit(_err_msg(e))
    finally:
        for f in [audio_file, thumb_file]:
            if f and os.path.exists(f):
                try: os.remove(f)
                except: pass


async def ntagyoutube(message: Message):
    try:
        m = await message.reply_text("◍ جاري البحث....")
        results = YoutubeSearch(message.text, max_results=6).to_dict()
        if not results:
            await m.edit("◍ لا توجد نتائج\n√")
            return
        text = ""
        for i, r in enumerate(results[:6]):
            text += f"🔢 {i+1}. {r['title']}\n"
            text += f"⏱ {r['duration']} | 👁 {r['views']} | 📺 {r['channel']}\n"
            text += f"🔗 https://youtube.com{r['url_suffix']}\n\n"
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(f"◍ خطأ: {str(e)[:200]}")


async def youttsearch(message: Message):
    a = None
    audio_file = thumb_file = None
    try:
        a = await message.reply_text("◍ جاري البحث....")
        results = YoutubeSearch(message.text, max_results=1).to_dict()
        if not results:
            await a.edit("◍ لا توجد نتائج\n√")
            return
        r = results[0]
        link = f"https://youtube.com{r['url_suffix']}"
        await a.edit(f"◍ وجدت: {r['title']}\n◍ جارى التحميل...\n√", disable_web_page_preview=True)
        loop = asyncio.get_event_loop()
        audio_file, thumb_file, info = await loop.run_in_executor(None, download_audio_sync, link)
        if not audio_file or not os.path.exists(audio_file):
            await a.edit("◍ فشل التحميل\n√")
            return
        title = info.get('title', r['title'])
        performer = info.get('uploader', r.get('channel', 'Unknown'))
        duration = int(float(info.get('duration', 0)))
        await a.edit("◍ انتظر جارى الرفع....\n√", disable_web_page_preview=True)
        await message.reply_audio(audio_file, caption=title, reply_to_message_id=message.message_id,
                                  duration=duration, performer=performer, title=title, thumb=thumb_file)
        await a.delete()
    except Exception as e:
        if a:
            await a.edit(_err_msg(e))
        else:
            await message.reply_text(_err_msg(e))
    finally:
        for f in [audio_file, thumb_file]:
            if f and os.path.exists(f):
                try: os.remove(f)
                except: pass


async def youttsearch_video(message: Message):
    a = None
    video_file = thumb_file = None
    try:
        a = await message.reply_text("◍ جاري البحث....")
        results = YoutubeSearch(message.text, max_results=1).to_dict()
        if not results:
            await a.edit("◍ لا توجد نتائج\n√")
            return
        r = results[0]
        link = f"https://youtube.com{r['url_suffix']}"
        await a.edit(f"◍ وجدت: {r['title']}\n◍ جارى التحميل...\n√", disable_web_page_preview=True)
        loop = asyncio.get_event_loop()
        video_file, thumb_file, info = await loop.run_in_executor(None, download_video_sync, link)
        if not video_file or not os.path.exists(video_file):
            await a.edit("◍ فشل التحميل\n√")
            return
        title = info.get('title', r['title'])
        duration = int(float(info.get('duration', 0)))
        await a.edit("◍ انتظر جارى الرفع....\n√", disable_web_page_preview=True)
        await message.reply_video(video_file, caption=title, reply_to_message_id=message.message_id,
                                  duration=duration, thumb=thumb_file)
        await a.delete()
    except Exception as e:
        if a:
            await a.edit(_err_msg(e))
        else:
            await message.reply_text(_err_msg(e))
    finally:
        for f in [video_file, thumb_file]:
            if f and os.path.exists(f):
                try: os.remove(f)
                except: pass


async def urbandict(_, message: Message):
    if len(message.command) < 2:
        await message.reply_text('يرجى كتابة كلمة بعد الامر.')
        return
    text = message.text.split(None, 1)[1]
    try:
        results = get(f"http://api.urbandictionary.com/v0/define?term={text}").json()
        reply_text = f'Definition: {results["list"][0]["definition"]}'
        reply_text += f'\n\nExample: {results["list"][0]["example"]}'
    except IndexError:
        reply_text = "لا توجد نتائج!"
    reply = reply_text.replace("[", "").replace("]", "")
    await message.reply_text(reply[:4096])


commands.add_command("music", "general")
commands.add_command("ud", "general")
commands.add_command("yt", "general")
commands.add_command("ys", "general")
commands.add_command("telegraph", "general")
