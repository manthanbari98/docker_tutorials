# 2. Flask Application in Docker


## Objective


Containerize and run a Flask web application using Docker.


## Project Files


```text
2_Flask_app/
├── app.py
├── Dockerfile
└── requirements.txt
```
## Technologies
- Python
- Flask
- Docker
## Application Routes

The Flask application contains the following routes:

| Route      | Purpose                   |
| ---------- | ------------------------- |
| `/`        | Displays the main page    |
| `/about`   | Displays the About page   |
| `/contact` | Displays the Contact page |

## Dockerfile

The Dockerfile:

- Uses Python as the base image
- Creates a working directory
- Copies requirements.txt
- Installs Python dependencies
- Copies the application code
- Exposes port 5000
- Starts the Flask application
## Build the Docker Image

Open the terminal inside the `2_Flask_app` folder:
```
docker build -t flask-docker-app .
```
## Run the Container
```
docker run -d -p 5000:5000 --name flask-container flask-docker-app
```
The application runs on:
```
http://localhost:5000
```
## Test the Application

Open:
```
http://localhost:5000
```
You can also test:
```
http://localhost:5000/about
```
and:
```
http://localhost:5000/contact
```
## Check Running Containers
```
docker ps
```
## View Container Logs
```
docker logs flask-container
```
## Stop the Container
```
docker stop flask-container
```
## Start the Container Again
```
docker start flask-container
```
## Remove the Container
```
docker rm flask-container
```
## Remove the Image
```
docker rmi flask-docker-app
```
## Concepts Practiced
- Flask application containerization
- Dockerfile
- Docker image
- Docker container
- requirements.txt
- Installing Python dependencies
- Port mapping
- Container logs
- Starting and stopping containers