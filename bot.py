import os
import requests

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
RECIPIENT_PHONE = "923XXXXXXXXX"  # یہاں اپنا واٹس ایپ نمبر لکھیں

def send_whatsapp_message():
    url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_PHONE,
        "type": "text",
        "text": {
            "body": "🌅 روزانہ کی اسلامی معلومات اور کیلنڈر اپڈیٹ:\n\nآج کا دن اللہ کے ذکر اور اچھے کاموں کے ساتھ شروع کریں! 🤲"
        },
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("پیغام کامیابی سے بھیج دیا گیا ہے!")
    else:
        print(f"خرابی پیش آئی: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_whatsapp_message()
