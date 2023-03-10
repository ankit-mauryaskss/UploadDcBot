# MIT License

# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
Hi {} 

I am Powerful Url Uploader Bot. Multiple Source Support. To see /help more information.
 
"""

    HELP_TEXT = """

# Send me the Google Drive | ytdl | direct links.

# Select the desired option.

# Then be relaxed your file will be uploaded soon..
 
"""

# give credit to developer

    ABOUT_TEXT = """
<b>â»ï¸ My Name</b> : Url Uploader Bot

<b>ð Channel</b> : <a href="https://t.me/greymatter_bots">@GreyMatter's Bot</a>

<b>ðº Heroku</b> : <a href="https://heroku.com/">Heroku</a>

<b>ð Language :</b> <a href="https://www.python.org/">Python 3.10.5</a>

<b>ðµð² Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 2.0.30</a>

<b>ð² Owner :</b> <a href="https://t.me/GreyMatter_Owner">@GreyMatter_Owner</a>

"""

    PROGRESS = """
ð° Speed : {3}/s\n\n
ð Done : {1}\n\n
ð¥ Tá´á´á´Ê sÉªá´¢á´  : {2}\n\n
â³ TÉªá´á´ Êá´Òá´ : {4}\n\n
"""
    ID_TEXT = """
ð Your Telegram ID ð¢ð¬ :- <code>{}</code>
"""

    INFO_TEXT = """

 ð¤¹ First Name : <b>{}</b>

 ð´ââï¸ Second Name : <b>{}</b>

 ð§ð»âð Username : <b>@{}</b>

 ð Telegram Id : <code>{}</code>

 ð Profile Link : <b>{}</b>

 ð¡ Dc : <b>{}</b>

 ð Language : <b>{}</b>

 ð² Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('â Help', callback_data='help'),
            InlineKeyboardButton('ð¦ About', callback_data='about')
        ], [
            InlineKeyboardButton('ð Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ð  Home', callback_data='home'),
            InlineKeyboardButton('ð¦ About', callback_data='about')
        ], [
            InlineKeyboardButton('ð Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ð  Home', callback_data='home'),
            InlineKeyboardButton('â Help', callback_data='help')
        ], [
            InlineKeyboardButton('ð Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ð Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "Now Select the desired formats below."
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "Trying to Download â\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\nð¤ Uploading Please Wait "
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dá´á´¡É´Êá´á´á´á´á´ ÉªÉ´ {} sá´á´á´É´á´s.\n\nTÊá´É´á´s Fá´Ê UsÉªÉ´É¢ Má´\n\nUá´Êá´á´á´á´á´ ÉªÉ´ {} sá´á´á´É´á´s"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "â Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process Free users only 1 request per 4 hrs\n
Upgrade your /plans to Remove Time Gaps and For link Processing"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
