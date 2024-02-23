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
