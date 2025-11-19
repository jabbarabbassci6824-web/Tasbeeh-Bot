from keep_alive import keep_alive
keep_alive()
import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import BadRequest

# --- إعدادات البوت ---
TOKEN = "8598900327:AAF3hHdoH8ZixGBiDIlaEq4Poa33jQKNSsg"  # ضع توكين البوت هنا
REQUIRED_CHANNEL = "@J11_11H"  # ضع معرف قناتك هنا (يجب أن يبدأ بـ @)

# قائمة التسبيحات
TASBEEH_LIST = [
    "سبحان الله وبحمده، سبحان الله العظيم",
    "لا إله إلا الله محمد رسول الله",
    "أستغفر الله العظيم وأتوب إليه",
    "اللهم صل وسلم على نبينا محمد",
    "لا حول ولا قوة إلا بالله",
    "سبحان الله، والحمد لله، ولا إله إلا الله، والله أكبر",
    "رضيت بالله رباً، وبالإسلام ديناً، وبمحمد صلى الله عليه وسلم نبياً",
    "اللهم إنك عفو تحب العفو فاعف عنا"
]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- دالة التحقق من الاشتراك ---
async def check_subscription(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    try:
        # جلب حالة العضو في القناة
        member = await context.bot.get_chat_member(chat_id=REQUIRED_CHANNEL, user_id=user_id)
        # الحالات المقبولة: عضو، منشئ القناة، أو مشرف
        if member.status in ["member", "creator", "administrator"]:
            return True
    except BadRequest:
        # يحدث هذا الخطأ إذا لم يكن البوت مشرفاً في القناة أو القناة غير موجودة
        print(f"Error: Bot is not admin in {REQUIRED_CHANNEL} or channel not found.")
        return False
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

    return False

# --- الوظائف ---

async def send_tasbeeh(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    random_tasbeeh = random.choice(TASBEEH_LIST)
    try:
        await context.bot.send_message(chat_id=job.chat_id, text=random_tasbeeh)
    except Exception:
        job.schedule_removal() # إيقاف التذكير إذا قام البوت بمغادرة المجموعة

async def start_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_message.chat_id

    # --- خطوة التحقق من الاشتراك ---
    is_subscribed = await check_subscription(user_id, context)

    if not is_subscribed:
        # إنشاء زر شفاف (Inline Button) يحتوي رابط القناة
        # نقوم بحذف علامة @ من الرابط ليعمل بشكل صحيح كـ URL
        channel_link = f"https://t.me/{REQUIRED_CHANNEL.replace('@', '')}"
        keyboard = [
            [InlineKeyboardButton("📢 اشترك في القناة أولاً", url=channel_link)],
            # زر للتحقق مرة أخرى (اختياري ولكن مفيد)
            # ملاحظة: زر التحقق يحتاج CallbackQueryHandler، للتبسيط سنكتفي برسالة توجيهية
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"🚫 **عذراً عزيزي**\n\nلا يمكنك تفعيل البوت إلا بعد الاشتراك في قناة البوت الرسمية.\nيرجى الاشتراك ثم إعادة إرسال /start",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        return
    # -----------------------------

    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    if current_jobs:
        await update.message.reply_text("✅ التذكير مفعل بالفعل في هذه المجموعة!")
        return

    # تشغيل التذكير كل 60 ثانية
    context.job_queue.run_repeating(send_tasbeeh, interval=60, first=10, chat_id=chat_id, name=str(chat_id))

    await update.message.reply_text(f"✅ شكراً لاشتراكك!\nتم تفعيل التذكيرات، سيتم إرسال تسبيح كل دقيقة.")

async def stop_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))

    if not current_jobs:
        await update.message.reply_text("التذكير غير مفعل حالياً.")
        return

    for job in current_jobs:
        job.schedule_removal()

    await update.message.reply_text("تم إيقاف التذكيرات بنجاح.")

# --- التشغيل الرئيسي ---
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_timer))
    application.add_handler(CommandHandler("stop", stop_timer))

    print("Bot with Force Subscribe is running...")
    application.run_polling()

if __name__ == "__main__":
    main()