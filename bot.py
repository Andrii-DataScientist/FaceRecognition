import telebot

# Read config from file
with open('config.ini', "r") as f:
    TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, freeloader! Send me your photo")

@bot.message_handler(commands=['test'])
def test(message):
	bot.reply_to(message, "test")

@bot.message_handler(func=lambda message: True)
def ask_photo(message):
	bot.send_message(message.chat.id, "Send me your photo, please.")

@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    bot.send_message(message.chat.id, f'file_path = {file_info.file_path}')

    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_photo(message.chat.id, downloaded_file, caption="Povtorka!")

bot.polling()