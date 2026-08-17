# 3. Flask + MySQL Using Docker Networking


## Objective


Run a Flask application and MySQL database in separate Docker containers and allow them to communicate through a Docker network.


## Project Structure


```text
3_Docker_app_network/
│
├── Flask/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── MYSQL/
    ├── Dockerfile
    └── init.sql
```
## Architecture
```
                 Docker Network
        ┌────────────────────────────┐
        │                            │
        │     Flask Container        │
        │     flask_container        │
        │          │                 │
        │          │ PyMySQL         │
        │          ▼                 │
        │     MySQL Container        │
        │     mysql_container        │
        │          │                 │
        │          ▼                 │
        │        demo_db             │
        │          │                 │
        │          ▼                 │
        │         users              │
        │                            │
        └────────────────────────────┘
```
## Technologies
- Python
- Flask
- PyMySQL
- MySQL 8.0
- Docker
- Docker Networking
- SQL
## Step 1 — Create a Docker Network
```
docker network create flask-mysql-network
```
## Check the network:
```
docker network ls
```
## Step 2 — Build the MySQL Image

Move into the MySQL directory:
```
cd MYSQL
```
Build the image:
```
docker build -t mysql-practice .
```
## Step 3 — Run the MySQL Container
```
docker run -d --name mysql_container --network flask-mysql-network -e MYSQL_ROOT_PASSWORD=demopassword -e MYSQL_DATABASE=demo_db -p 3307:3306 mysql-practice
```
Check the container:
```
docker ps
```
View MySQL logs:
```
docker logs mysql_container
```
## Step 4 — Build the Flask Image

Move into the Flask directory:
```
cd ../Flask
```
Build the image:
```
docker build -t flask-network-app .
```
## Step 5 — Run the Flask Container
```
docker run -d --name flask_container --network flask-mysql-network -p 5000:5000 flask-network-app
```
Check both containers:
```
docker ps
```
## Step 6 — Inspect the Docker Network
```
docker network inspect flask-mysql-network
```
Both containers should be connected to the same network.

## Flask → MySQL Communication

The Flask application connects to MySQL using:
```
host='mysql_container'
```
The MySQL container name acts as the hostname within the Docker network.

The Flask application uses PyMySQL to connect to:
```
Database: demo_db
User: root
Host: mysql_container
```
## Database

The initialization SQL creates:
```
Database: demo_db
Table: users
```
The table contains:
```
id
city
temperature
```
## Test the Flask Application
Open:
```
http://localhost:5000
```
To insert sample data:
```
http://localhost:5000/insert_data
```
The `/insert_data` endpoint inserts:
```
City: New York
Temperature: 25.5
```
into the `users` table.

## Useful Commands
## Check containers
```
docker ps
```
## View Flask logs
```
docker logs flask_container
```
## View MySQL logs
```
docker logs mysql_container
```
## Stop containers
```
docker stop flask_container mysql_container
```
## Remove containers
```
docker rm flask_container mysql_container
```
## Remove the Docker network
```
docker network rm flask-mysql-network
```
## Concepts Practiced
- Docker networking
- Container-to-container communication
- Flask container
- MySQL container
- Docker image creation
- Port mapping
- PyMySQL
- Database initialization
- Container names as network hostnames