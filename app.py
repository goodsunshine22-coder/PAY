from flask import Flask, request, jsonify, send_from_directory
import random
import string
import time

app = Flask(__name__)

# Store codes temporarily
codes = {}

def make_code():
    return ''.join(random.choices(string.digits, k=6))

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/api/send_code", methods=["POST"])
def send_code():
    data = request.get_json()
    phone = data.get("phone", "").strip()

    if not phone:
        return jsonify({"success": False})

    code = make_code()
    codes[phone] = {
        "code": code,
        "time": time.time()
    }

    # Print clearly in terminal
    print("\n" + "="*40)
    print(f"PHONE NUMBER : {phone}")
    print(f"CODE         : {code}")
    print("="*40 + "\n")

    return jsonify({"success": True})

@app.route("/api/verify_code", methods=["POST"])
def verify_code():
    data = request.get_json()
    phone = data.get("phone", "").strip()
    code = data.get("code", "").strip()

    record = codes.get(phone)

    if not record or record["code"] != code:
        print(f"\nFAILED attempt → Phone: {phone} | Code tried: {code}\n")
        return jsonify({"success": False})

    # Success
    print("\n" + "="*40)
    print(f"VERIFIED SUCCESSFULLY")
    print(f"Phone: {phone}")
    print("="*40 + "\n")

    del codes[phone]
    return jsonify({"success": True})

if __name__ == "__main__":
    print("Server running at http://localhost:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
