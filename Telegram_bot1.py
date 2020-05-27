from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telebot import apihelper

apihelper.proxy = {'http':'https://23.31.218.226:80'}
TG_Token = "1288851011:AAFCLoUGTn4NO49CtEGgbjKIz4lq9FvmyYs"

def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = "незнакомец"
	text = update.effective_message.text
	reply_text = f"Привет, {name}!\n\n{text}"

	bot.send_message(
		chat_id = update.effective_message.chat_id,
		text = reply_text,
	)

def main():
	bot = Bot(
		token=TG_Token,
	)
	updater = Updater(TG_Token, use_context=True)
	handler = MessageHandler(Filters.all, message_handler)
	updater.dispatcher.add_handler

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	main()