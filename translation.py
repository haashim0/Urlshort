from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_MESSAGE = '''👋𝗛𝗲𝗹𝗹𝗼, {}
𝗜 𝗖𝗮𝗻 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝗟𝗶𝗻𝗸 𝗧𝗼 𝗦𝗵𝗼𝗿𝘁𝗟𝗶𝗻𝗸. 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗔𝗻𝘆 𝗣𝗼𝘀𝘁 𝗪𝗶𝘁𝗵 𝗟𝗶𝗻𝗸𝘀 𝗔𝗻𝗱 𝗜 𝗪𝗶𝗹𝗹 𝗦𝗵𝗼𝗿𝘁𝗲𝗻 𝗔𝗹𝗹 𝗟𝗶𝗻𝗸𝘀 𝗜𝗻 𝗜𝘁 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝘁𝗼 𝗗𝘂𝗟𝗶𝗻𝗸.

'''


HELP_MESSAGE = '''
Help and bot not working so contact me :-@Gaurav4x @Y76D42

ℹ️ And how to use this bot and command so watch my video.
:-https://youtu.be/r5B-Mn4W2MA
'''


ABOUT_TEXT = """
📍My all bot settings in bot command and my most best command list.

/header - set header text and click on command check out more info.

/footer - set footer text and click on command check out more info.

/username - set username and click on command check out more info.

/banner_image - set banner img and click on command check out more info.

/me - your account information and on|off all settings.


ℹ️ And how to use this bot and command so watch my video.
:-https://youtu.be/r5B-Mn4W2MA
"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('🧰 Home', callback_data='start_command')
    ]
])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('🧰 Home', callback_data=f'start_command'),
        InlineKeyboardButton('🧿 Help Disk', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('🚫 Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('©️CopyrightLinks', callback_data='anc_command'),
        InlineKeyboardButton('🧿 Help Disk', callback_data='help_command'),
        
    ],
        [
        InlineKeyboardButton('⚙️ Settings', callback_data='about_command'),
        InlineKeyboardButton('❤️ Channel', url='https://t.me/DuLinkUpdate')
    ],
            [
        InlineKeyboardButton('♌️ Connect To Dulink', url='https://du-link.in/member/tools/api'),
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
❤️ Welcome to dulink and bot !!

- Api: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/shortener_api api.`
            
Ex: `/shortener_api 8f5987ac3a45a271b420aa5099d4792af53fa953`
            
ℹ️ And how to use this bot and command so watch my video.
:-https://youtu.be/r5B-Mn4W2MA"""

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

