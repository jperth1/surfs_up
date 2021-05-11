# Import dependency
from flask import Flask
## Create new flast app instance
app = Flask(__name__)

# Create Flast Route
#1. Define the end point, "root"
@app.route('/')
# create the function hello_world
def hello_world():
    return 'Hello world'