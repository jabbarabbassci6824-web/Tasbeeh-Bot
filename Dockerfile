# استخدام صورة بايثون أساسية كنقطة انطلاق
FROM python:3.11-slim

# تثبيت المتطلبات الضرورية للنظام (الأهم هو ffmpeg)
RUN apt-get update && apt-get install -y ffmpeg

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملف البوت الرئيسي
COPY radio.py /app

# أمر تشغيل البوت عند بدء الحاوية
CMD ["python3", "radio.py"]
