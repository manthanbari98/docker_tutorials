# 1. First Docker Application


## Objective


Create a simple Python application and run it inside a Docker container.


## Project Files


```text
1_First_app/
├── app.py
└── Dockerfile
```
## Application

The Python application prints:
```
Hey Bro, this app will run in container!
```
## Dockerfile

The Dockerfile uses a lightweight Python image and defines the working directory, application files, and startup command.

## Build Docker Image

Open the terminal inside the 1_First_app folder and run:
```
docker build -t first-docker-app .
```
## Run Docker Container
```
docker run --name first-docker-container first-docker-app
```
## Check Containers
```
docker ps
```
To see stopped containers as well:
```
docker ps -a
```
## Remove Container
```
docker rm first-docker-container
```
## Remove Image
```
docker rmi first-docker-app
```
## Concepts Practiced
- Docker image
- Docker container
- Dockerfile
- Base image
- FROM
- WORKDIR
- COPY
- CMD
- Building an image
- Running a container