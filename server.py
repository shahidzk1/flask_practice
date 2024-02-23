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

# URL of /no_content
@app.route("/no_content")
def no_content():
    """return 'no content found' with a status of 204
    Returns:
        string: no content found with 204 status code
    """
    return ({"message":"No content found"}, 204)


