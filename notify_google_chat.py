import requests
import os
import json


def send_google_chat_alert():
    webhook = os.getenv("GCHAT_WEBHOOK_URL")

    if not webhook:
        raise Exception("Google Chat webhook missing")

    payload = {
        "text": (
            "🚨 *LOGIN API FAILURE ALERT*\n\n"
            "❌ marketplace_vendor_login failed\n"
            "🌐 https://manavtest.yelobeta.xyz\n"
            "🕒 Check GitHub Actions logs"
        )
    }

    response = requests.post(
        webhook,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=10
    )

    print("Google Chat Status:", response.status_code)
    print("Google Chat Response:", response.text)


if __name__ == "__main__":
    send_google_chat_alert()
