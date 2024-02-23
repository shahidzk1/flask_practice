from flask import Flask,  make_response
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

#In the index method Flask automatically sends an HTTP 200 OK successful response when one sent back a message
#However, one can also set the return status explicitly
# URL of /no_content
@app.route("/no_content")
def no_content():
    """return 'no content found' with a status of 204
    Returns:
        string: no content found with 204 status code
    """
    return ({"message":"No content found"}, 204)

#Send custom HTTP code back with the make_response() method
@app.route("/exp")
def index_explicit():
    resp = make_response({"message":"Hello"})
    resp.status_code = 200
    return resp

