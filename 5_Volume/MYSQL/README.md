# 5. Docker Volume with MySQL


## Objective


Practice Docker volumes by mounting a persistent storage volume to a MySQL container.


Docker volumes allow data to persist independently of the container lifecycle.


## Project Structure


```text
5_Volume/
└── MYSQL/
    ├── Dockerfile
    └── init.sql
```
## Architecture
```
              MySQL Container
                    │
                    │
                    ▼
              /var/lib/mysql
                    │
                    │ mounted volume
                    ▼
              mysql_data
             Docker Volume
```
## MySQL Database

The MySQL container uses:
```
Database: demo_db
```
The initialization script creates:
```
users
├── id
├── city
└── temperature
```
## Build the MySQL Image

Open the terminal inside:
```
5_Volume/MYSQL
```
Build the image:
```
docker build -t mysql-volume-app .
```
## Create and Run the Container with a Volume
```
docker run -d -p 3307:3306 --name mysql_volume_container -e MYSQL_ROOT_PASSWORD=demopassword -e MYSQL_DATABASE=demo_db -v mysql_data:/var/lib/mysql mysql-volume-app
```
## Explanation
```
docker run
```
Creates and starts a container.
```
-d
```
Runs the container in detached/background mode.
```
-p 3307:3306
```
Maps host port 3307 to MySQL's container port 3306.
```
--name mysql_volume_container
```
Assigns a name to the container.
```
-e MYSQL_ROOT_PASSWORD=demopassword
```
Sets the MySQL root password.
```
-e MYSQL_DATABASE=demo_db
```
Creates the demo_db database.
```
-v mysql_data:/var/lib/mysql
```
Mounts the Docker volume mysql_data to MySQL's data directory.
```
mysql-volume-app
```
Specifies the Docker image used to create the container.

## Check Running Containers
```
docker ps
```
## List Docker Volumes
```
docker volume ls
```
You should see:
```
mysql_data
```
## Inspect the Volume
```
docker volume inspect mysql_data
```
This displays information about the Docker volume.

## View Container Logs
```
docker logs mysql_volume_container
```
## Stop the Container
```
docker stop mysql_volume_container
```
## Start the Container Again
```
docker start mysql_volume_container
```

Because the MySQL data is stored in the Docker volume, the data can persist even when the container is stopped or removed.

## Remove the Container
```
docker rm mysql_volume_container
```
## Remove the Volume
```
docker volume rm mysql_data
```
Removing the volume permanently deletes the data stored in that volume.

## Concepts Practiced
- Docker volumes
- Persistent storage
- MySQL containers
- Volume mounting
- /var/lib/mysql
- Port mapping
- Environment variables
- Docker volume inspection
- Container lifecycle