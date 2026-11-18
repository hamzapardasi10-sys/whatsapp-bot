from datetime import datetime
from hijri_converter import Gregorian

# English Day ko Urdu mein convert karne ke liye dictionary
urdu_days = {
    "Monday": "پیر",
    "Tuesday": "منگل",
    "Wednesday": "بدھ",
    "Thursday": "جمعرات",
    "Friday": "جمعہ",
    "Saturday": "ہفتہ",
    "Sunday": "اتوار"
}

now = datetime.now()

gregorian_date = now.strftime("%d %B %Y")
english_day = now.strftime("%A")
urdu_day = urdu_days.get(english_day, english_day)

# Hijri Date
hijri = Gregorian(now.year, now.month, now.day).to_hijri()

# Message Template
message = f"""
💙💜💙💜💙💜💙💜💙💜
❄❄❄❄❄❄❄❄❄❄

🌹بسْــــــــــــــمِ ﷲِالرَّحْمن الرَّحِيم 🌹
🌸اَلسَّلَامُ عَلَیْکُم وَرَحْمَةُ اللهِ وَبَرَكَاتُه‌🌸

🇵🇰 *آج کا کیلنڈر* 🌤

🔖 {hijri.day} {hijri.month_name()} {hijri.year}ھ 💎
🔖 {gregorian_date}ء 💎

🌄 *بروز {urdu_day} ({english_day})* 🌄

🌿 *مجلس کے آداب!*

🔹 *رسول الله ﷺ نے فرمایا: کوئی شخص کسی دوسرے شخص کو اس کی جگہ سے نہ اٹھائے کہ پھر وہاں بیٹھ جائے بلکہ وسعت پیدا کرو۔*

📗«صحیح مسلم -5684»

❄❄❄❄❄❄❄❄❄❄
💜💙💜💙💜💙💜💙💜💙
"""

print(message)
