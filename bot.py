import logging
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# فعال کردن لاگینگ برای بهتر دیدن خطاها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# تابع برای پاسخ دادن به پیام‌ها
async def handle_message(update: Update, context: CallbackContext):
    if update.channel_post:  # بررسی اینکه پیام در کانال هست
        text = update.channel_post.text
        if "😂" in text:  # اگر در پیام خنده (emoji) باشد
            # ارسال پیام به کانال برای اعلام "نخند!"
            await context.bot.send_message(chat_id=update.channel_post.chat_id, text="کیرخر")

# تابع main برای راه‌اندازی ربات
async def main():
    # توکن ربات خود را وارد کنید
    application = Application.builder().token("7770284224:AAF9lMjPggkSmn3lukOHRSSNR5fG9SRK4cI").build()

    # اضافه کردن هنده برای دریافت پیام‌ها در کانال
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # شروع کار با ربات
    await application.run_polling()

# اجرای ربات
if __name__ == "__main__":
    # به جای asyncio.run از await استفاده می‌کنیم
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())  # یا مستقیماً از await استفاده کنید