# 4. Docker Compose - Flask + MySQL


## Objective


Use Docker Compose to run and manage a multi-container application consisting of a Flask application and a MySQL database.


## Project Structure


```text
4_Docker_Compose/
│
├── Flask/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── MYSQL/
│   └── init.sql
│
└── docker-compose.yml
```
## Architecture
```
                  Docker Compose
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      Flask Container        MySQL Container
      flask_container        mysql_container
             │                     │
             └──── Docker Network ┘
                        │
                     demo_db
                        │
                      users
```
## Technologies
- Python
- Flask
- PyMySQL
- MySQL 8.0
- Docker
- Docker Compose
- SQL
## Services
## Flask Service

The Flask service:

- Builds the application from the `Flask` directory
- Runs on port `5000`
- Connects to the MySQL service
- Provides an endpoint to insert data
- MySQL Service

## The MySQL service:

- Uses the `mysql:8.0` image
- Creates the `demo_db` database
- Initializes the `users` table
- Exposes port `3306` inside the container
## Start the Application

Open the terminal inside the `4_Docker_Compose` directory and run:
```
docker compose up -d
```
This starts both the Flask and MySQL containers.

## Check Running Services
```
docker compose ps
```
You can also use:
```
docker ps
```
## View Logs

View logs for all services:
```
docker compose logs
```
View Flask logs:
```
docker compose logs flask_container
```
View MySQL logs:
```
docker compose logs mysql_container
```
## Access the Flask Application

Open:
```
http://localhost:5000
```
The Flask application should display:
```
Hello, World!
```
## Insert Data

Open:
```
http://localhost:5000/insert_data
```
The application inserts sample data into the MySQL users table:
```
City: New York
Temperature: 25.5
```
## Port Mapping

The Flask service uses:
```
5000:5000
```
The MySQL service uses:
```
3307:3306
```
This means:

Host              Container
--------------------------------
localhost:5000 →  Flask:5000
localhost:3307 →  MySQL:3306
## Health Check

The MySQL service includes a health check to determine whether the database is ready.

The Flask service uses:
```
depends_on:
  mysql_container:
    condition: service_healthy
```
This makes Flask wait until the MySQL service is reported as healthy.

## Volume

The MySQL initialization script is mounted using:
```
volumes:
  - ./MYSQL/init.sql:/docker-entrypoint-initdb.d/init.sql
```
This makes the local SQL initialization script available inside the MySQL container.

## Rebuild the Application

If you make changes to the Dockerfile or application:
```
docker compose up -d --build
```
## Stop the Services
```
docker compose stop
```
## Stop and Remove Containers
```
docker compose down
```
## View Docker Compose Configuration
```
docker compose config
```
## Concepts Practiced
- Docker Compose
- Multi-container applications
- Docker networking
- Flask containerization
- MySQL containerization
- Service dependencies
- Health checks
- Port mapping
- Volume mounting
- Database initialization
- Container logs