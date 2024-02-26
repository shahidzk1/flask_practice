# flask_practice
This repo contains the basics of Flask.
Python above 3.8 is required.
To run the server.py use
  ```
  flask --app server --debug run
  ```
in another terminal run
  ```
  curl -X GET -i -w '\n' localhost:5000
  ```
The -X argument specifies the GET command, and the -i argument displays the header from the response.

To Get the No content method
  ```
  curl -X GET -i -w '\n' localhost:5000/no_content
  ```
 To Get the explicit 
 
    ```
    curl -X GET -i -w '\n' localhost:5000/exp
    ```
  Fake data has been added, to get a person by first name
  
    ```
    curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"
    ```
  Delete a person
    ```
    curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
    ```

  Add a new person to the fake data
  
    ```
    curl -X POST -i -w '\n' \
    --url http://localhost:5000/person \
    --header 'Content-Type: application/json' \
    --data '{
          "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
          "first_name": "John",
          "last_name": "Horne",
          "graduation_year": 2001,
          "address": "1 hill drive",
          "city": "Atlanta",
          "zip": "30339",
          "country": "United States",
          "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
  }'
  ```

  For error handling

    ```
    curl -X POST -i -w '\n' http://localhost:5000/notvalid
    ```
