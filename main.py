import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your credentials (be careful exposing this publicly!)
BOT_TOKEN = "7983002268:AAFXTyhMfomoujNmVZGIqx-jGqdwl31v1FY"
ADMIN_ID = 6996741395

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id == ADMIN_ID:
        await update.message.reply_text("Hello Admin! I'm TaskMaster AI.")
    else:
        await update.message.reply_text("Hello! I'm TaskMaster AI.")

# Run the Telegram bot
def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# Dummy Flask web server to keep Render alive
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running!"

# Start both Flask and the bot
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    web_app.run(host="0.0.0.0", port=5000)
