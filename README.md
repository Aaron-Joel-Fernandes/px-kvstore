# px-kvstore

Author: Aaron Fernandes 

## Description

A minimal in-memory key-value store with CRUD support via HTTP interface. Built with Python using only the standard library.

## Features

- In-memory key-value storage
- HTTP API for create, read, update, delete
- Dockerized
- Unit tests included

## API Endpoints

| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| POST   | `/store/<key>`   | Create key-value  |
| GET    | `/store/<key>`   | Read value        |
| PUT    | `/store/<key>`   | Update value      |
| DELETE | `/store/<key>`   | Delete key        |

Payload for POST/PUT:
```json
{ "value": "your_value" } 
```
## Running Locally
python server.py

curl -X POST localhost:8080/store/mykey -d '{"value":"test"}' -H "Content-Type: application/json"

## Running with Docker
docker build -t px-kvstore .
docker run -p 8081:8081 px-kvstore

## Running Test
python test_kvstore.py


## Future Enhancements

- Persistent storage (e.g., file or DB)
- Authentication/authorization
- Metrics and logging
- Graceful shutdown and error handling
