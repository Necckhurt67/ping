from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import time

# Замени на свой токен
TOKEN = "7619953134:AAGiEqE1e2fJcg_dURtjB4SKqI9EZetxdHo"

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Время начала обработки сообщения
    message_start_time = time.time()
    
    # API задержка (время обработки запроса)
    api_start = time.time()
    # Отправляем сообщение
    sent_message = await update.message.reply_text("🔄 Измеряю задержку...")
    api_latency = (time.time() - api_start) * 1000  # в миллисекундах
    
    # Задержка ответа на сообщение
    message_latency = (time.time() - message_start_time) * 1000
    
    # Редактируем сообщение с результатами
    await sent_message.edit_text(
        f"Pong! 🏓\n"
        f"API Latency: {api_latency:.2f}ms\n"
        f"Message Latency: {message_latency:.2f}ms"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n"
        "Напиши /ping чтобы проверить задержку"
    )

def main():
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ping", ping))
    
    # Запускаем бота
    print("🤖 Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()