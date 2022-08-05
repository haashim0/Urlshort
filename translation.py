from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_MESSAGE = '''👋𝗛𝗲𝗹𝗹𝗼, {}
𝗜 𝗖𝗮𝗻 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝗟𝗶𝗻𝗸 𝗧𝗼 𝗦𝗵𝗼𝗿𝘁𝗟𝗶𝗻𝗸. 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗔𝗻𝘆 𝗣𝗼𝘀𝘁 𝗪𝗶𝘁𝗵 𝗟𝗶𝗻𝗸𝘀 𝗔𝗻𝗱 𝗜 𝗪𝗶𝗹𝗹 𝗦𝗵𝗼𝗿𝘁𝗲𝗻 𝗔𝗹𝗹 𝗟𝗶𝗻𝗸𝘀 𝗜𝗻 𝗜𝘁 𝗖𝗼𝗻𝘃𝗲𝗿𝘁 𝘁𝗼 𝗗𝘂𝗟𝗶𝗻𝗸.

'''


HELP_MESSAGE = '''
Hey! My name is {firstname}. I am a Link Shortener Bot, here to make your Work Easy and Help you to Earn more

I have lots of handy features, such as 

- [Hyperlink](https://t.me/{username})
- Buttons convert support
- Header and Footer Text support
- Replace Username
- Banner Image

Helpful commands:

- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!

If you have any bugs or questions on how to use me, contact to {owner}.

Below are some features I provide'''


ABOUT_TEXT = """
**My Details:**

`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)
`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)
`👨‍💻 Developer:` [BotCreator99](t.me/BotCreator99)
`📢 Support:` {}
"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Home', callback_data='start_command')
    ]
])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('📨CopyrightLinks', callback_data='anc_command'),
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
- Shortener Website: {base_site}

- {base_site} API: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/shortener_api api`
            
Ex: `/shortener_api 6LZq851sXofffPHugiKQq`
            
Shortener API of your preferred shortener API.

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

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

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

