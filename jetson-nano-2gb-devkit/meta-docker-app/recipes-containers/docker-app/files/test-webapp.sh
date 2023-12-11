#! /bin/sh

# Delete existing container
echo "Deleting exiting postgres and webapp containers ..."
docker-compose down

# Run new docker containers for postgres and webapp
echo "Running the docker containers for postgres and webapp ..."
docker-compose up -d

# Wait for container to start
echo "Waiting for containers to start ..."
sleep 20

# Tests
echo "Testing route /"
curl http://localhost:5500

echo "Testing route /create_table"
curl -X POST http://localhost:5500/create_table

echo "Testing route /insert_data"
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:5500/insert_data

echo "Testing route /tables"
curl http://localhost:5500/tables

echo "Testing route /all_data"
curl http://localhost:5500/all_data

# Cleanup
echo "Deleting test containers ..."
docker-compose down
