from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/test")
def test():
    return "Flask is working"

@app.route("/")
def home():
    return render_template("payment.html")

@app.route("/process-payment", methods = ["POST"])
def process_payment():
    email = request.form.get("email")
    cardholder = request.form.get("cardholder")
    cardnumber = request.form.get("card_number")
    expiry = request.form.get("expiry")
    pin = request.form.get("cvv")

    print("Email:", email)
    print("Cardholder:", cardholder)
    print("Card Number:", cardnumber)
    print("Expiry: ", expiry)
    print("Pin: ",pin)
    
    

    return "Form submitted successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
    


