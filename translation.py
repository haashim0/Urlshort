from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_MESSAGE = '''ððð²ð¹ð¹ð¼, {}
ð ðð®ð» ðð¼ð»ðð²ð¿ð ðð¶ð»ð¸ ð§ð¼ ð¦ðµð¼ð¿ððð¶ð»ð¸. ð¦ð²ð»ð± ð ð² ðð»ð ð£ð¼ðð ðªð¶ððµ ðð¶ð»ð¸ð ðð»ð± ð ðªð¶ð¹ð¹ ð¦ðµð¼ð¿ðð²ð» ðð¹ð¹ ðð¶ð»ð¸ð ðð» ðð ðð¼ð»ðð²ð¿ð ðð¼ ðððð¶ð»ð¸.

â¹ï¸ ðð»ð± ðµð¼ð ðð¼ ððð² ððµð¶ð ð¯ð¼ð ð®ð»ð± ð°ð¼ðºðºð®ð»ð± ðð¼ ðð®ðð°ðµ ðºð ðð¶ð±ð²ð¼.
:-https://youtu.be/lpzEll82EQc

'''


HELP_MESSAGE = '''
ð¤ Help and bot not working so contact me :-@Gaurav4x @Y76D42

â¹ï¸ And how to use this bot and command so watch my video.
:-https://youtu.be/lpzEll82EQc

'''


ABOUT_TEXT = """
ðMy all bot settings in bot command and my most best command list.

/header - set header text and click on command check out more info.

/footer - set footer text and click on command check out more info.

/username - set username and click on command check out more info.

/banner_image - set banner img and click on command check out more info.

/me - your account information and on|off all settings.

â¹ï¸ And how to use this bot and command so watch my video.
:-https://youtu.be/lpzEll82EQc
"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('ð§° Home', callback_data='start_command')
    ]
])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('ð§° Home', callback_data=f'start_command'),
        InlineKeyboardButton('ð§¿ Help Disk', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('ð« Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('ð¢ Notification', callback_data='anc_command'),
        InlineKeyboardButton('ð§¿ Help Disk', callback_data='help_command'),
        
    ],
        [
        InlineKeyboardButton('âï¸ Settings', callback_data='about_command'),
        InlineKeyboardButton('â¤ï¸ Channel', url='https://t.me/DuLinkUpdate')
    ],
            [
        InlineKeyboardButton('âï¸ Connect To Dulink', url='https://du-link.in/member/tools/api'),
    ],


])


BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'start_command')
    ],

])

USER_ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Home', callback_data='start_command')
    ]
])

USER_ABOUT_MESSAGE = """
â¤ï¸ Welcome to dulink and bot !!

- Api :- {shortener_api}

- Username :- @{username}

- Header Text :- 
{header_text}

- Footer Text :- 
{footer_text}

- Banner Image :- {banner_image}

ð click on this buttons and on|off features.
"""


SHORTENER_API_MESSAGE = """ â¹ï¸ send /start command and click on "Connect To Dulink"
   """

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username`

For just removing the username from the post: 
`/username none`

This username will be automatically replaced with other usernames in the post

To remove current username, `/username remove`"""

BANNER_IMAGE = """Current Banner Image URL: {banner_image}

Usage: `/banner_image image_url`

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://wallpapercave.com/wp/wp6674867.jpg`"""

