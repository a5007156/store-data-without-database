# Receive HTTP requests and store data without using a database
Check the [nodejs version](https://github.com/Tecosse/store-data-without-db-nodejs-/).

## HOW TO USE
    sudo apt install git
    git clone https://github.com/Tecosse/store-data-without-database/
    cd ./store-data-without-database/
    python3 ./server.py
> The command python3 server.py will start the server on port 8080.

> To send a GET request to the server, you can use curl.

    curl http://localhost:8080/

> This will return an empty JSON array, because the server doesn't have any data yet.

> To send a POST request to the server, you can use curl like this:

    curl -d '{"name": "Tecosse", "description": "Loves python!"}' http://localhost:8080/

> This will send a JSON object containing a name and a description to the server. The server will add this data to its list and return an empty JSON object as the response.

> If you send another GET request to the server, you will see that it now contains the data you sent in the POST request:

    curl http://localhost:8080/

`[{"name": "Tecosse", "description": "Loves python!"}]`
