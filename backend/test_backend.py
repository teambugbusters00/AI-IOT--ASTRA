import requests
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    try:
        r = requests.get(f"{BASE_URL}/")
        if r.status_code == 200 and r.json() == {"status": "Backend running"}:
            print("✅ Root endpoint working")
        else:
            print(f"❌ Root endpoint failed: {r.status_code} {r.text}")
    except Exception as e:
        print(f"❌ Root endpoint exception: {e}")

def test_signup():
    payload = {"name": "Test User", "email": "test@example.com", "password": "password123"}
    try:
        r = requests.post(f"{BASE_URL}/signup", json=payload)
        if r.status_code == 200:
             print("✅ Signup working")
        elif r.status_code == 400 and r.json()["detail"] == "User already exists":
             print("✅ Signup working (User existed)")
        else:
             print(f"❌ Signup failed: {r.status_code} {r.text}")
    except Exception as e:
        print(f"❌ Signup failed: {e}")

def test_login():
    payload = {"email": "test@example.com", "password": "password123"}
    try:
        r = requests.post(f"{BASE_URL}/login", json=payload)
        print(f"Login Response: {r.status_code} {r.text}")
        if r.status_code == 200:
             print("✅ Login working")
        else:
            print(f"❌ Login failed: {r.status_code} {r.text}")
    except Exception as e:
        print(f"❌ Login failed: {e}")

def test_dashboard():
    try:
        r = requests.get(f"{BASE_URL}/dashboard")
        if r.status_code == 200:
            data = r.json()
            if "projects" in data and "status" in data:
                print("✅ Dashboard connection working")
            else:
                print(f"❌ Dashboard data invalid: {data}")
        else:
             print(f"❌ Dashboard failed: {r.status_code} {r.text}")
    except Exception as e:
        print(f"❌ Dashboard failed: {e}")

def test_device():
    try:
        r = requests.get(f"{BASE_URL}/device/status")
        if r.status_code == 200:
            data = r.json()
            if "temperature" in data and "led" in data:
                print("✅ Device simulation working")
            else:
                print("❌ Device data invalid")
        else:
             print(f"❌ Device simulation failed: {r.status_code} {r.text}")
    except Exception as e:
        print(f"❌ Device simulation failed: {e}")

if __name__ == "__main__":
    test_root()
    test_signup()
    test_login()
    test_dashboard()
    test_device()
    print("\n🎉 ALL SYSTEMS GO!")
