# Docker Tutorials & Practice Projects


Hands-on Docker practice projects covering containerization, Dockerfiles, Flask, MySQL, Docker networking, Docker Compose, and Docker volumes.


These projects were created to understand Docker fundamentals and progressively move from a simple Python container to multi-container applications.


---


## 📚 Projects


| # | Project | Main Concepts |
|---|---|---|
| 1 | First Docker App | Dockerfile, Image, Container |
| 2 | Flask App | Flask, Dependencies, Port Mapping |
| 3 | Flask + MySQL Network | Docker Networking, Container Communication |
| 4 | Docker Compose | Multi-container Application, Health Check, Volumes |
| 5 | Docker Volume | Persistent Storage, MySQL Volume |


---


# 1️⃣ First Docker Application


### Objective


Create a simple Python application and run it inside a Docker container.


### Concepts


- Dockerfile
- Docker image
- Docker container
- Base image
- `WORKDIR`
- `COPY`
- `CMD`


### Flow


```text
Python Application
       ↓
   Dockerfile
       ↓
   Docker Image
       ↓
 Docker Container
```
## Run
```
docker build -t first-docker-app ./1_First_app

docker run --name first-docker-container first-docker-app
```
View Scenario 1 →

## 2️⃣ Flask Application in Docker
### Objective

Containerize a Flask web application and run it inside Docker.

## Technologies
- Python
- Flask
- Docker
- Concepts
- Flask containerization
- requirements.txt
- Installing dependencies
- Docker image
- Port mapping
- Container logs
## Architecture
```
Flask Application
       ↓
   Dockerfile
       ↓
   Docker Image
       ↓
 Flask Container
       ↓
localhost:5000
```
## Run
```
cd 2_Flask_app


docker build -t flask-docker-app .


docker run -d -p 5000:5000 --name flask-container flask-docker-app
```
Application:
```
http://localhost:5000
```
View Scenario 2 →

## 3️⃣ Flask + MySQL Using Docker Networking
### Objective

Run Flask and MySQL in separate containers and allow them to communicate through a Docker network.

Architecture
```
                    Docker Network
        ┌─────────────────────────────┐
        │                             │
        │     Flask Container         │
        │     flask_container         │
        │            │                │
        │            │ PyMySQL        │
        │            ▼                │
        │     MySQL Container         │
        │     mysql_container         │
        │            │                │
        │            ▼                │
        │         demo_db             │
        │            │                │
        │            ▼                │
        │           users             │
        │                             │
        └─────────────────────────────┘
```
## Important Concept

The Flask application connects to MySQL using the container name:
```
host='mysql_container'
```
The container name works as the hostname inside the Docker network.

## Technologies
- Python
- Flask
- PyMySQL
- MySQL
- Docker Networking
- SQL
## Run

Create the network:
```
docker network create flask-mysql-network
```
Build and run the MySQL container, then build and run the Flask container using the same network.

The detailed commands are available in the project README.

View Scenario 3 →

## 4️⃣ Docker Compose - Flask + MySQL
### Objective

Use Docker Compose to manage a multi-container Flask and MySQL application.

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
## Docker Compose Features

This project demonstrates:

- Multiple services
- Flask + MySQL
- Docker networking
- Port mapping
- Health checks
- Service dependencies
- Volume mounting
- Database initialization
## Start the Application

From the `4_Docker_Compose` directory:
```
docker compose up -d
```
Check services:
```
docker compose ps
```
Access Flask:
```
http://localhost:5000
```
## Health Check

The Flask service depends on MySQL being healthy:
```
depends_on:
  mysql_container:
    condition: service_healthy
```
View Scenario 4 →

## 5️⃣ Docker Volume with MySQL
### Objective

Practice Docker volumes for persistent MySQL storage.

## Architecture
```
              MySQL Container
                    │
                    ▼
              /var/lib/mysql
                    │
                    ▼
              mysql_data
             Docker Volume
```
## Important Concept

The volume:
```
mysql_data
```
is mounted to:
```
/var/lib/mysql
```
This allows MySQL data to persist independently from the container lifecycle.

## Example
```
docker run -d \
  -p 3307:3306 \
  --name mysql_volume_container \
  -e MYSQL_ROOT_PASSWORD=demopassword \
  -e MYSQL_DATABASE=demo_db \
  -v mysql_data:/var/lib/mysql \
  mysql-volume-app
```
List volumes:
```
docker volume ls
```
Inspect the volume:
```
docker volume inspect mysql_data
```
View Scenario 5 →

## 🛠️ Technologies Used
- Docker
- Docker Compose
- Python
- Flask
- PyMySQL
- MySQL
- SQL
## 📈 Learning Progression

The projects demonstrate a gradual progression of Docker concepts:
```
1. Python Application
        ↓
2. Dockerfile
        ↓
3. Docker Image
        ↓
4. Docker Container
        ↓
5. Flask Application
        ↓
6. Flask + MySQL
        ↓
7. Docker Networking
        ↓
8. Docker Compose
        ↓
9. Health Checks & Service Dependencies
        ↓
10. Docker Volumes & Persistent Storage
```
## 🎯 Key Docker Concepts Practiced
- Images
- Containers
- Dockerfiles
- Base images
- FROM
- WORKDIR
- COPY
- RUN
- CMD
- EXPOSE
- Port mapping
- Environment variables
- Docker networks
- Container-to-container communication
- Docker Compose
- Services
- Health checks
- depends_on
- Volumes
- Persistent storage
- MySQL initialization
- Container logs