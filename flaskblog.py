# DO THIS ON MAC FOR VIRTUAL ENV SET UP
# code copied from flask website/ from flask, importing Flask class
from flask import Flask
# app variable setting to an instance of Flask class
app = Flask(__name__)

# app route decorator/decorators are used to add additional functionality to existing functions
#home page
@app.route("/")
def hello():
    return "Hello, World!"