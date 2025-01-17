from flask import Flask, render_template
from flask import request, redirect, url_for
import re
import logging


app = Flask(__name__)



@app.route("/home")
def home():
   app.logger.info("Home route accessed") 
   return "Welcome to Hackers Poulette™!"


@app.route("/", methods=["GET"])
def index():
    app.logger.info("form accessed") 
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

   
    honeypot = request.form.get("honeypot")

    # If the honeypot field is filled, treat it as a spam submission
    if honeypot:
        flash("Spam detected! Your form submission has been ignored.")
        return redirect(url_for('home'))  # Redirect back to the form

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    country = request.form["country"]
    gender = request.form["gender"]
    message = request.form["message"]
    subjects = request.form.getlist("subject")

    # Add sanitization and validation here
    

    def sanitize_input(input_string):
        return re.sub(r'<.*?>', '', input_string)  # Remove HTML tags (XSS prevention)

    def validate_email(email):
        if "@" not in email or "." not in email:
            return False
        return True

   # honeypot = request.form.get("honeypot")
    #if honeypot:
     #  return "Spam detected"

    return render_template("thank_you.html", first_name=first_name, last_name=last_name)



if __name__ == "__main__":
    #serve(app, host='0.0.0.0', port=8080)
    app.run(debug=True)
