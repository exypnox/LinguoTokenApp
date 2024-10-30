import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Вставьте ваш токен здесь
TOKEN = '7614715798:AAHSxTlsKqrf3c6A9HcWTu5pD0UdpGi8Jy0'

nest_asyncio.apply()  # Примените nest_asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Открыть Mini App", url='https://t.me/LinguoTokenBot/LinguoToken')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Нажмите на кнопку ниже, чтобы открыть Mini App:', reply_markup=reply_markup)

async def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
