import telebot 
from googletrans import *
#trans = Translator()
API_TOKEN= os.environ['PASS']

bot = telebot.TeleBot(API_TOKEN)
x= bot.get_me()
print("Bot launched successfully :: \n",x)
@bot.message_handler(commands=["start", "hello"])
def start_bot(msg):
    #my_translation = translator.translate()
    bot.send_message(msg.chat.id,"👋Hello {}😊☺️.\n Am language translator 🦿 bot.".format(msg.chat.first_name))
    bot.send_message(msg.chat.id,"Am here to translate any word for you in any language to English.")
    bot.send_message(msg.chat.id,"To use me just send me the word to translate😉.\nCreated by  @wambugu_kinyua.")
    
    
@bot.message_handler(commands=["info"])
def info_(msg):
    bot.reply_to(msg,"Am a translator bot.\nCreated by @wambugu_kinyua.")
    
@bot.message_handler(commands=["help"])
def help_user(msg):
    file = open("usage_photo.jpg", "rb")
    bot.reply_to(msg,"Usage :\n send me the text to translate as a chat message")
    bot.send_photo(msg.chat.id, file)  
    file.close()

@bot.message_handler(func=lambda m: True)
def translate_text(msg):
    try:
        translator = Translator()
        my_translation = translator.translate(msg.text)
        bot.send_message(msg.chat.id,"Detected language is {}".format(my_translation.src))
        bot.send_message(msg.chat.id,"Translated text :👇👇")
        bot.send_message(msg.chat.id,my_translation.text)
       # bot.send_message(msg.chat.id, "Thank you for using my services.😊\nCredits @wambugu_kinyua.")
    except:
        bot.send_message(msg.chat.id,"Didn't get that🙂...resend the text to translate.")

    
bot.polling()
