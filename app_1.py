# import dependencies
from flask import Flask
# Create new flask app instance
app = Flask(__name__)
# Create flask starting point route
@app.route("/")
# Create a function
def your_mom():
    return "your mom is so fat"
