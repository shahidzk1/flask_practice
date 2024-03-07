from flask import Flask, make_response, request
# create Flask application by initializing the Flask class
app = Flask(__name__)
#create first route. @app.route(“/“) is a Python decorator provided by Flask to assign URLs in the app to functions.
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
    """return 'Hello World' message with a status code of 200
    Returns:
        string: Hello World
        status code: 200
    """
    res = make_response({"message":"Hello"})
    res.status_code = 200
    return resp

#######insert csv data

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]
    
@app.route("/name_search")
def name_search():
    """find a person in the database

    Returns:
        json: person if found, with status of 200
        404: if not found
        422: if argument q is missing
    """
    query = request.args.get("q")

    if not query:
        return {"message": "Invalid input parameter, insert q"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person

    return ({"message": "Person not found"}, 404)

@app.route("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person
    return {"message": "person not found in data"}, 404

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            #####save the csv file again
            return {"message":"id of person deleted"}, 200
    return {"message": "person not found"}, 404


@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{new_person['id']}"}, 200

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404
