from telegram.ext import *
import responsre as R
import telebot
from dotenv import load_dotenv
import os
import requests

photo = "https://te.legra.ph/file/cf00ecd72b3ee934bd87e.jpg"
# photo2 = "https://te.legra.ph/file/036781df069b478254e37.jpg"

updater = Updater("6151806723:AAEOkTGYlhQNPjrUHZAZBUSnIv-qDnTv-LI", use_context=True)


load_dotenv()
token = os.getenv('5621512579:AAGhhvBcDNiQ_wfdQwEyVVUzaQMNPL1vDR8')

bot = telebot.TeleBot(token)

# Let's define stuff
def get_url():
    contents = requests.get('https://api.waifu.pics/sfw/waifu').json()
    image_url = contents['url']
    return image_url

def get_nekourl():
    contents = requests.get('https://api.waifu.pics/sfw/neko').json()
    image_url = contents['url']
    return image_url

def get_avatarurl():
    contents = requests.get('https://nekos.life/api/v2/img/avatar').json()
    image_url = contents['url']
    return image_url


def get_shinobuurl():
    contents = requests.get('https://api.waifu.pics/sfw/shinobu').json()
    image_url = contents['url']
    return image_url

def get_meguminurl():
    contents = requests.get('https://api.waifu.pics/sfw/megumin').json()
    image_url = contents['url']
    return image_url

def get_kissurl():
    contents = requests.get('https://api.waifu.pics/nsfw/trap').json()
    image_url = contents['url']
    return image_url

def get_lickurl():
    contents = requests.get('https://api.waifu.pics/nsfw/blowjob').json()
    image_url = contents['url']
    return image_url

def get_nwaifuurl():
    contents = requests.get('https://api.waifu.pics/nsfw/waifu').json()
    image_url = contents['url']
    return image_url

def get_lewdurl():
    contents = requests.get('https://nekos.life/api/v2/img/lewd').json()
    image_url = contents['url']
    return image_url

def get_holourl():
    contents = requests.get('https://nekos.life/api/v2/img/hololewd').json()
    image_url = contents['url']
    return image_url

def get_titsurl():
    contents = requests.get('https://nekos.life/api/v2/img/tits').json()
    image_url = contents['url']
    return image_url

def get_boobsurl():
    contents = requests.get('https://nekos.life/api/v2/img/boobs').json()
    image_url = contents['url']
    return image_url

def get_solourl():
    contents = requests.get('https://nekos.life/api/v2/img/solo').json()
    image_url = contents['url']
    return image_url

def get_erourl():
    contents = requests.get('https://nekos.life/api/v2/img/ero').json()
    image_url = contents['url']
    return image_url

def get_hentaiurl():
    contents = requests.get('https://nekos.life/api/v2/img/hentai').json()
    image_url = contents['url']
    return image_url

def get_eronurl():
    contents = requests.get('https://nekos.life/api/v2/img/eron').json()
    image_url = contents['url']
    return image_url


def get_bjurl():
    contents = requests.get('https://nekos.life/api/v2/img/bj').json()
    image_url = contents['url']
    return image_url

def get_erokiturl():
    contents = requests.get('https://nekos.life/api/v2/img/eroK').json()
    image_url = contents['url']
    return image_url

def get_pussyurl():
    contents = requests.get('https://nekos.life/api/v2/img/pussy').json()
    image_url = contents['url']
    return image_url

def get_kitesuneurl():
    contents = requests.get('https://nekos.life/api/v2/img/lewdk').json()
    image_url = contents['url']
    return image_url

def get_holoerourl():
    contents = requests.get('https://nekos.life/api/v2/img/holoero').json()
    image_url = contents['url']
    return image_url


@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hey there, I'm Tele-chan 💖
     I can fetch hottest anime and hentai images & send them to you
     Send /help to check the commands out. '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['ping'])
def greet(message):
    msg = ''' I'm alive :3 '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['repo'])
def greet(message):
    msg = ''' Repository Link -> https://github.com/KazeDevID/Tele-chan/ '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['source'])
def greet(message):
    msg = ''' Source Code -> https://github.com/KazeDevID
              Author -> @KenalSayaaa '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['help'])
def help(message):
    msg = ''' Here are the commands :

    SFW Commands :
    /waifu
    /neko
    /shinobu
    /megumin
    /avatar

    NSFW Commands :
    /trap
    /blowjob
    /lewd
    /tits
    /boobs
    /solo
    /ero
    /hentai
    /bj
    /kitesune
    /eroKitesune
    /pussy
    /holo
    /holoEro
    /eroNeko

    Other Commands :
    /ping
    /repo
    /source
    '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['waifu'])
@bot.message_handler(regexp=r'waifu')
def waifu(message):
    url = get_url()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['neko'])
@bot.message_handler(regexp=r'neko')
def neko(message):
    url = get_nekourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['eroNeko'])
@bot.message_handler(regexp=r'eroNeko')
def eroneko(message):
    url = get_eronekourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['avatar'])
@bot.message_handler(regexp=r'avatar')
def avatar(message):
    url = get_avatarurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['kitesune'])
@bot.message_handler(regexp=r'kitesune')
def kitesune(message):
    url = get_kitesuneurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['eroKitesune'])
@bot.message_handler(regexp=r'eroKitesune')
def eroKitesune(message):
    url = get_erokiturl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['holo'])
@bot.message_handler(regexp=r'holo')
def eroHolo(message):
    url = get_holourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['holoEro'])
@bot.message_handler(regexp=r'holoEro')
def holoEro(message):
    url = get_holoerourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['shinobu'])
@bot.message_handler(regexp=r'shinobu')
def shinobu(message):
    url = get_shinobuurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['megumin'])
@bot.message_handler(regexp=r'megumin')
def megumin(message):
    url = get_meguminurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['bj'])
@bot.message_handler(regexp=r'bj')
def bj(message):
    url = get_bjurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['pussy'])
@bot.message_handler(regexp=r'pussy')
def pussy(message):
    url = get_pussyurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['trap'])
@bot.message_handler(regexp=r'trap')
def kiss(message):
    url = get_kissurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['blowjob'])
@bot.message_handler(regexp=r'blowjob')
def lick(message):
    url = get_lickurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['lewd'])
@bot.message_handler(regexp=r'lewd')
def lewd(message):
    url = get_lewdurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['tits'])
@bot.message_handler(regexp=r'tits')
def lewdb(message):
    url = get_titsurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['solo'])
@bot.message_handler(regexp=r'solo')
def lewdc(message):
    url = get_solourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['boobs'])
@bot.message_handler(regexp=r'boobs')
def lewdd(message):
    url = get_boobsurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['ero'])
@bot.message_handler(regexp=r'ero')
def ero(message):
    url = get_erourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['hentai'])
@bot.message_handler(regexp=r'hentai')
def hentai(message):
    url = get_hentaiurl()
    bot.send_photo(message.chat.id, url)


def main():
    bot.polling()

if __name__ == '__main__':
    main()

def start(update, context):
	update.message.reply_text(
		f"{photo} \n𝒉𝒊𝒊𝒊 𝒊 𝒂𝒎 𝒍𝒂𝒓𝒂... 𝒂𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝒐𝒓 @aadillllll . \n𝒓𝒆𝒎𝒆𝒎𝒃𝒆𝒓 𝒐𝒏𝒆 𝒕𝒉𝒊𝒏𝒈 𝒎𝒚 𝒎𝒂𝒔𝒕𝒆𝒓 𝒂𝒍𝒘𝒂𝒚𝒔 𝒃𝒆 𝒐𝒑.... 𝒔𝒐 𝒅𝒐𝒏'𝒕 𝒎𝒆𝒔𝒔 𝒖𝒑 𝒘𝒊𝒕𝒉 𝒉𝒊𝒎. 𝒃𝒖𝒕 𝒍𝒂𝒅𝒊𝒆𝒔 𝒚𝒐𝒖 𝒂𝒓𝒆 𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒉𝒆𝒓 𝒅𝒎  𝒐𝒓 𝒊𝒏𝒔𝒕𝒂. 𝒂𝒍𝒔𝒐 𝒚𝒐𝒖 𝒌𝒏𝒐𝒘 𝒂𝒃𝒐𝒖𝒕 𝒉𝒆𝒓. 𝒋𝒖𝒔𝒕 𝒕𝒚𝒑𝒆 /info 𝒂𝒏𝒅 𝒃𝒐𝒐𝒎 𝒚𝒐𝒖 𝒌𝒏𝒐𝒘 𝒂𝒍𝒍 𝒂𝒃𝒐𝒖𝒕 𝒉𝒆𝒓.ֆ 💛💭ۦ")

def info(update, context):
	update.message.reply_text(""" https://te.legra.ph/file/036781df069b478254e37.jpg \n HERE are the some commands that you know  
	Available Commands :-
	/crush - To get the information about my master
	/insta - To get the instagram profile URL
	/gmail - To get gmail URL
	/github - To get the github URL""")


def crush_about(update, context):
	update.message.reply_text(
		"Hiiii my name is Aadil Shiekh. I have many thing to telll i know you here for my personal information. So, let's begin\n\
		my age is just 17 years.\nheight of 6 feet and the thing you don't know is my weight which is just 62 kg\
		I lived in New Delhi - JAMNAPAAR. \nI am a class 12th science(PCMB) student with a decent above average student profile. \nI best in Physics and Maths as well. But Chemistry is such a loosing face for me. \nBut if you want to be better text me.\nAnd then my professtional profile, I am a Developer with the master in Python CSS HTML and JAVA SCRIPT.\nI have Deploy Many of Telegram bots. And currently working with a secret projec let it be down.\nif you wanna to know more just dm me")


def instagram_url(update, context):
	update.message.reply_text("INSTAGRAM Link =>\
	https://www.instagram.com/aadillllll._/")


def gmail_url(update, context):
	update.message.reply_text(
		"GMAIL URL => \
		darkanger008@gmail.com")


def github_url(update, context):
	update.message.reply_text(
		"GITHUB URL => https://github.com/Darkranger00/")


def gaali(update, context):
	update.message.reply_text(
		"bsdk ka apna kaam kar")

dict1 = {i:f"give a big hand to adil" for i in range(10)}

def repeat(update, context):
	update.message.reply_text(dict1)

def handle_message(update, context):
	text = str(update.message.text).lower()
	responses = R.sample_response(text)

	update.message.reply_text(responses)

#def unknown_text(update: Update, context: CallbackContext):
#	update.message.reply_text(
#		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('insta', instagram_url))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('crush', crush_about))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('repeat', repeat))
# updater.dispatcher.add_handler(MessageHandler(
#	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
