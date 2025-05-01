from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Your credentials
BOT_TOKEN = "7983002268:AAFXTyhMfomoujNmVZGIqx-jGqdwl31v1FY"
ADMIN_IDS = [6996741395]
BAD_WORDS = ["badword1", "badword2", "idiot", "stupid"]

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm TaskMaster AI — ready to assist your group!")

# Welcome new members
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(f"Welcome, {user.first_name}!")

# Block bad words
async def filter_bad_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    if any(bad_word in message_text for bad_word in BAD_WORDS):
        await update.message.delete()
        await update.message.reply_text("⚠️ Please avoid using inappropriate language.")

# Admin command example
async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id in ADMIN_IDS:
        await update.message.reply_text("✅ Admin command executed.")
    else:
        await update.message.reply_text("❌ This command is only for admins.")

# App setup
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin_command))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), filter_bad_words))

print("Bot is running...")
app.run_polling()
