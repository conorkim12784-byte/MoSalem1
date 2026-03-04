============================
 خطوات تشغيل البوت
============================

1. ثبت المتطلبات:
   pip install -r requirements.txt

2. افتح ملف info.json وحط التوكن بتاعك:
   {"Token": "TOKEN_BTAK_HENA", "idSudo": 1923931101}
   
   - Token: احصل عليه من @BotFather على تيليجرام
   - idSudo: الـ ID بتاعك (1923931101) ✅ جاهز

3. شغل البوت:
   python bot.py

============================
 هيكل المجلدات المطلوب
============================

bot_folder/
├── bot.py
├── config.py
├── database.py
├── dbh.py
├── utils.py
├── localization.py
├── consts.py
├── backup_file.py
├── info.json          ← حطه بنفسك بالتوكن
├── requirements.txt
├── version.txt
├── plugins/           ← كل ملفات الـ .py التانية
│   ├── admin.py
│   ├── general.py
│   ├── start.py
│   └── ... (باقي الملفات)
└── locales/
    ├── ar-SA/         ← ملفات JSON العربية
    └── en-US/         ← ملفات JSON الإنجليزية

============================
