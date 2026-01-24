import requests
import os

URL = "https://beta-api.yelo.red/marketplace_vendor_login"

HEADERS = {
    "base_version": "1.0.0",
    "device_type": "WEB",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Referer": "https://manavtest.yelobeta.xyz/en/",
    "User-Agent": "Mozilla/5.0"
}


def test_marketplace_vendor_login():
    payload = {
        "email": os.getenv("LOGIN_EMAIL"),
        "password": os.getenv("LOGIN_PASSWORD"),
        "marketplace_reference_id": os.getenv("MARKETPLACE_REF_ID"),
        "device_token": None,
        "app_type": "WEB",
        "domain_name": "ManavTest.yelobeta.xyz",
        "dual_user_key": 0,
        "language": "en"
    }

    # Validate env variables
    if not payload["email"] or not payload["password"] or not payload["marketplace_reference_id"]:
        raise Exception("Environment variables missing")

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        timeout=15
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    assert response.status_code == 200, "API status code failed"

    response_json = response.json()
    assert response_json.get("status") is True, "Login failed"

