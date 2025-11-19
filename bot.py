import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

# ==========================================
# ⚠️ منطقة البيانات (أدخل بياناتك هنا)
# ==========================================
BOT_TOKEN = "8598900327:AAF3hHdoH8ZixGBiDIlaEq4Poa33jQKNSsg" # توكن البوت
API_ID = 7740070                                         
API_HASH = "7ffc4b7ec62beb0695ef5d44a58080bb"              

# 🚨 بيانات الاشتراك الإجباري
FORCED_SUB_CHANNEL = "@J11_11H" 
FORCED_SUB_LINK = "https://t.me/J11_11H"    

# ==========================================
# 🗂️ المصادر وقوائم الأذكار
# ==========================================

# 1. قائمة التسبيحات للعداد التفاعلي (متاح للجميع)
TASBEEHAT_INTERACTIVE = [
    "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ (100 مرة)",
    "الْحَمْدُ لِلَّهِ (100 مرة)",
    "اللَّهُ أَكْبَرُ (100 مرة)",
    "لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ (10 مرات)",
    "أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ وَأَتُوبُ إِلَيْهِ (100 مرة)",
    "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ (100 مرة)",
]

# 2. قائمة التسبيحات للإرسال الآلي (تذكير آلي)
AUTO_TASBEEHAT_LIST = [
    "✨ سُبْحَانَ اللَّهِ وَبِحَمْدِهِ ، سُبْحَانَ اللَّهِ الْعَظِيمِ",
    "🕌 لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ",
    "🤍 لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ",
    "🤲 أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ وَأَتُوبُ إِلَيْهِ",
]

# بيانات الإذاعة الصوتية
BASE_QURAN = "https://server7.mp3quran.net/basit/{}.mp3"
SURAH_NAMES = ["الفاتحة", "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام", "الأعراف", "الأنفال", "التوبة", "يونس", "هود", "يوسف", "الرعد", "إبراهيم", "الحجر", "النحل", "الإسراء", "الكهف", "مريم", "طه", "الأنبياء", "الحج", "المؤمنون", "النور", "الفرقان", "الشعراء", "النمل", "القصص", "العنكبوت", "الروم", "لقمان", "السجدة", "الأحزاب", "سبأ", "فاطر", "يس", "الصافات", "ص", "الزمر", "غافر", "فصلت", "الشورى", "الزخرف", "الدخان", "الجاثية", "الأحقاف", "محمد", "الفتح", "الحجرات", "ق", "الذاريات", "الطور", "النجم", "القمر", "الرحمن", "الواقعة", "الحديد", "المجادلة", "الحشر", "الممتحنة", "الصف", "الجمعة", "المنافقون", "التغابن", "الطلاق", "التحريم", "الملك", "القلم", "الحاقة", "المعارج", "نوح", "الجن", "المزمل", "المدثر", "القيامة", "الإنسان", "المرسلات", "النبأ", "النازعات", "عبس", "التكوير", "الانفطار", "المطففين", "الانشقاق", "البروج", "الطارق", "الأعلى", "الغاشية", "الفجر", "البلد", "الشمس", "الليل", "الضحى", "الشرح", "التين", "العلق", "القدر", "البينة", "الزلزلة", "العاديات", "القارعة", "التكاثر", "العصر", "الهمزة", "الفيل", "قريش", "الماعون", "الكوثر", "الكافرون", "النصر", "المسد", "الإخلاص", "الفلق", "الناس"]
NAHJ_DATA = {
    "n_1": ["خطبة المتقين (همام)", "https://dl.aviny.com/voice/sokhanrani/falsafi/sharh-khotbeh-hammam/01.mp3"], 
    "n_2": ["الشقشقية", "https://media.imamhussain.org/filestorage/files/audio/133.mp3"],
}
DUA_DATA = {
    "d_kumayl": ["دعاء كميل", "https://dl.aviny.com/voice/dua/kumail/kumail-maitham.mp3"],
    "d_sabah":  ["دعاء الصباح", "https://dl.aviny.com/voice/dua/sabah/sabah-maitham.mp3"],
}

# ==========================================
# 🛑 المتاغير العامة والمجدولة
# ==========================================
# متجر عالمي لتخزين مهام التذكير الآلي {chat_id: task_object}
SCHEDULED_TASKS = {} 

# ==========================================
# إعداد البوت
# ==========================================
app = Client("radio_bot_secured", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

# ==========================================
# ⏰ دالة مهمة الإرسال الآلي (Task Function)
# ==========================================
async def auto_tasbeeh_task(chat_id, interval_seconds):
    """ مهمة ترسل الأذكار آلياً إلى المجموعة """
    try:
        index = 0
        while True:
            await asyncio.sleep(interval_seconds)
            
            zikr = AUTO_TASBEEHAT_LIST[index % len(AUTO_TASBEEHAT_LIST)]
            
            await app.send_message(
                chat_id, 
                f"**🔔 تذكير آلي:**\n{zikr}",
                disable_notification=True
            )
            
            index += 1
            
    except asyncio.CancelledError:
        # يتم الوصول إلى هنا عند إيقاف المهمة بواسطة المشرف
        pass
    except Exception as e:
        print(f"Error in auto_tasbeeh_task for chat {chat_id}: {e}")

# ==========================================
# 👮‍♂️ دوال التحقق
# ==========================================
async def check_is_admin(chat_id, user_id):
    try:
        member = await app.get_chat_member(chat_id, user_id)
        return member.status in ["administrator", "owner"]
    except:
        return False

async def check_forced_subscription(user_id):
    try:
        member = await app.get_chat_member(FORCED_SUB_CHANNEL, user_id)
        return member.status not in ["kicked", "left"]
    except Exception as e:
        return False

def sub_required_markup():
    return InlineKeyboardMarkup([[InlineKeyboardButton("إشترك الآن في القناة 📢", url=FORCED_SUB_LINK)]])

# دالة مساعدة لتحويل الثواني إلى نص (للرد على المشرف)
def format_interval(seconds):
    if seconds >= 3600 and seconds % 3600 == 0:
        return f"{seconds // 3600} ساعة"
    elif seconds >= 60 and seconds % 60 == 0:
        return f"{seconds // 60} دقيقة"
    else:
        return f"{seconds} ثانية"

# ==========================================
# القوائم (Keyboards)
# ==========================================
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 القرآن الكريم", callback_data="menu_quran"), 
         InlineKeyboardButton("🤲 الأدعية والخطب", callback_data="menu_dua")],
        [InlineKeyboardButton("📿 ذكر وتسبيح (للجميع)", callback_data="menu_tasbeeh")], 
        [InlineKeyboardButton("⏰ **تذكير آلي** (مشرفين)", callback_data="menu_schedule")],
        [InlineKeyboardButton("🛑 إيقاف البث والخروج", callback_data="stop_stream")]
    ])

def tasbeeh_menu(index=0, count=0):
    total_items = len(TASBEEHAT_INTERACTIVE)
    count_button = InlineKeyboardButton(
        f"عدّاد النقرات: {count}", 
        callback_data=f"tasbeeh_count_{index}_{count+1}"
    )
    next_button = InlineKeyboardButton(
        f"التالي ({index + 1}/{total_items}) ➡️", 
        callback_data=f"tasbeeh_next_{index}"
    )
    return InlineKeyboardMarkup([
        [count_button],
        [next_button],
        [InlineKeyboardButton("إيقاف العداد ❌", callback_data="back_main")]
    ])

def schedule_menu(chat_id):
    # حالة التذكير الحالي
    status_text = "❌ غير مفعل"
    if chat_id in SCHEDULED_TASKS and not SCHEDULED_TASKS[chat_id].done():
        status_text = "✅ مفعل حالياً" 

    return InlineKeyboardMarkup([
        [InlineKeyboardButton("5 دقائق", callback_data="schedule_300"), 
         InlineKeyboardButton("10 دقائق", callback_data="schedule_600")],
        [InlineKeyboardButton("30 دقيقة", callback_data="schedule_1800"), 
         InlineKeyboardButton("ساعة واحدة", callback_data="schedule_3600")],
        [InlineKeyboardButton("4 ساعات", callback_data="schedule_14400"), 
         InlineKeyboardButton("🛑 إيقاف التذكير", callback_data="schedule_stop")],
        [InlineKeyboardButton(status_text, callback_data="no_op")], # لعرض الحالة فقط
        [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="back_main")]
    ])
    
# (بقية قوائم القرآن والأدعية كما هي)

# ==========================================
# 🚀 الأوامر والتفاعلات
# ==========================================

@app.on_message(filters.command("start") & filters.group)
async def start_handler(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # لا يوجد فحص للمشرف هنا، يتم عرض القائمة للجميع
    # ولكن سيتم منع غير المشرفين من استخدام أزرار التحكم لاحقاً
    
    await message.reply(
        "🎙 **نظام إذاعة القرآن والتسبيح**\n"
        "اختر الخدمة. (⚠️ التحكم بالإذاعة والمهام الآلية للمشرفين فقط).",
        reply_markup=main_menu()
    )

@app.on_callback_query()
async def cb_handler(client, cb: CallbackQuery):
    chat_id = cb.message.chat.id
    user_id = cb.from_user.id
    data = cb.data

    # 1. --- معالجة ميزات التسبيح المتاحة للجميع ---
    is_tasbeeh_action = data == "menu_tasbeeh" or data.startswith("tasbeeh_")
    
    if is_tasbeeh_action:
        # لا يوجد فحص للمشرفين هنا (لأنها متاحة للجميع)
        
        if data == "menu_tasbeeh":
            tasbeeh_index = 0
            await cb.edit_message_text(
                f"**📿 ذكر وتسبيح**\n\n{TASBEEHAT_INTERACTIVE[tasbeeh_index]}",
                reply_markup=tasbeeh_menu(tasbeeh_index, 0)
            )

        elif data.startswith("tasbeeh_count_"):
            try:
                _, index_str, count_str = data.split("_")
                index = int(index_str)
                count = int(count_str)
                if count > 10000: count = 1 # حد أقصى عملي
                await cb.edit_message_reply_markup(
                    reply_markup=tasbeeh_menu(index, count)
                )
            except:
                await cb.answer("خطأ في العداد.", show_alert=True)

        elif data.startswith("tasbeeh_next_"):
            try:
                _, _, index_str = data.split("_")
                current_index = int(index_str)
                next_index = (current_index + 1) % len(TASBEEHAT_INTERACTIVE) 
                await cb.edit_message_text(
                    f"**📿 ذكر وتسبيح**\n\n{TASBEEHAT_INTERACTIVE[next_index]}",
                    reply_markup=tasbeeh_menu(next_index, 0) 
                )
            except:
                await cb.answer("لا يوجد المزيد من الأذكار.", show_alert=True)
        return

    # 2. --- فحص المشرفين والاشتراك لبقية الأوامر (إذاعة، وجدولة) ---
    if not await check_is_admin(chat_id, user_id):
        return await cb.answer("🚫 هذا الزر (للإذاعة أو الجدولة) للمشرفين فقط!", show_alert=True)

    if not await check_forced_subscription(user_id):
        return await cb.edit_message_text(
            f"⛔ **عذراً، عزيزي المشرف.**\n"
            f"للاستمرار في استخدام البوت، يرجى الاشتراك في قناة البوت الرسمية أولاً.",
            reply_markup=sub_required_markup()
        )
        
    # 3. --- معالجة ميزات التذكير الآلي (الجدولة) ---
    if data == "menu_schedule":
        await cb.edit_message_text(
            "**⏰ إعداد التذكير الآلي**\n\nاختر الفترة الزمنية لإرسال التسبيحات:",
            reply_markup=schedule_menu(chat_id)
        )

    elif data.startswith("schedule_"):
        action = data.split("_")[1]
        
        # إيقاف المهمة الحالية (إذا كانت تعمل)
        if chat_id in SCHEDULED_TASKS:
            SCHEDULED_TASKS[chat_id].cancel()
            del SCHEDULED_TASKS[chat_id]

        if action == "stop":
            await cb.edit_message_text("🛑 **تم إيقاف التذكير الآلي بنجاح.**", reply_markup=main_menu())
        else:
            interval_seconds = int(action)
            
            # إنشاء وبدء المهمة الخلفية الجديدة
            task = asyncio.create_task(auto_tasbeeh_task(chat_id, interval_seconds))
            SCHEDULED_TASKS[chat_id] = task
            
            time_str = format_interval(interval_seconds)

            await cb.edit_message_text(
                f"🔔 **تم تفعيل التذكير الآلي!**\n\nسيتم إرسال التسبيحات كل **{time_str}**.",
                reply_markup=main_menu()
            )

    # 4. --- معالجة ميزات الإذاعة الصوتية (Voice Chat) ---
    elif data == "back_main":
        await cb.edit_message_text("👇 **القائمة الرئيسية:**", reply_markup=main_menu())
    elif data == "menu_quran":
        await cb.edit_message_text("📖 **اختر السورة:**", reply_markup=quran_menu(1))
    elif data == "menu_dua":
        await cb.edit_message_text("🤲 **اختر الدعاء أو الخطبة:**", reply_markup=list_menu({**NAHJ_DATA, **DUA_DATA}))
    elif data == "page_1":
        await cb.edit_message_text("📖 **القرآن - 1:**", reply_markup=quran_menu(1))
    elif data == "page_2":
        await cb.edit_message_text("📖 **القرآن - 2:**", reply_markup=quran_menu(2))
    
    elif data == "stop_stream":
        try:
            await call_py.leave_group_call(chat_id)
            await cb.edit_message_text("🛑 **تم إيقاف البث ومغادرة المكالمة.**", reply_markup=main_menu())
        except:
            await cb.answer("البوت غير متصل حالياً.", show_alert=True)

    elif data.startswith("play_"):
        url = ""
        title = ""
        if "play_q_" in data:
            num = data.split("_q_")[1]
            try:
                title = f"سورة {SURAH_NAMES[int(num)-1]}"
                url = BASE_QURAN.format(num)
            except:
                return await cb.answer("خطأ في تحديد السورة.", show_alert=True)
        elif "play_url_" in data:
            key = data.split("play_url_")[1]
            combined = {**NAHJ_DATA, **DUA_DATA}
            if key in combined:
                title = combined[key][0]
                url = combined[key][1]
        
        if url:
            try:
                stream = MediaStream(url)
                await call_py.join_group_call(chat_id, stream) 
                await cb.edit_message_text(
                    f"✅ **يتم البث الآن في المحادثة الصوتية:**\n🎙 {title}\n\n⚠️ (تأكد من أن المحادثة الصوتية قد تم إنشاؤها في المجموعة)", 
                    reply_markup=main_menu()
                )
            except Exception as e:
                await cb.message.reply(f"❌ **خطأ:** يرجى بدء المحادثة الصوتية (Voice Chat) في المجموعة أولاً ثم المحاولة مرة أخرى.")

# ==========================================
# التشغيل
# ==========================================
async def start_bot():
    print("Bot is ready. Mode: Groups, Admins-Only VC/Scheduling, Public Tasbeeh Counter.")
    await call_py.start()
    await pyrogram.idle()

if __name__ == "__main__":
    import pyrogram
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
