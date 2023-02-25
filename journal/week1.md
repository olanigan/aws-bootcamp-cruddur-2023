# Week 1 — App Containerization


## Docker commands used to build backend image and run container

```
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
docker run --rm -p 4567:4567 -it  -e FRONTEND_URL -e BACKEND_URL backend-flask 
docker build -t backend-flask ./backend-flask
```


## Docker commands used to build front-end image and run container
docker build -t frontend-react-js ./frontend-react-js
docker run -p 3000:3000 -d frontend-react-js
```


## Docker commands used for compose

```
docker compose up
docker-compose up
```

Troubleshooting:
Successfully ran the frontend and backend containers individually without an hitch.

However, the posts was not getting populated initially on running Docker compose. To resolve this, I stopped and deleted the existing containers and images and use Docker Compose to re-build the images and run the containers.


## Postgres

Postgres was added and the following command was used for verification:
```
psql -Upostgres --host localhost
```