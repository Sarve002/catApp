from flask import Flask  # first flask is package, second Flask is class.

app = Flask(__name__)  # app is a variable that takes the Flask class
app.config["SECRET_KEY"] = "very_strong_password"

from webApp import routes