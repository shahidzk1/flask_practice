from flask import Flask
# create Flask application by initializing the Flask class
app = Flask(__name__)
#create first route
@app.route("/")
#method for the main root URL
def index():
    #return html
    return "hello world"
    #return json
    #return "message": "Hello World"
