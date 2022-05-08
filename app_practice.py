#Import Dependency
from flask import Flask

#Create a Flask App Instance
app = Flask(__name__)

#Create Flask Routes 
@app.route('/')
def hello_world():
    return 'Hello world'
