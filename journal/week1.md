# Week 1 — App Containerization


## Docker commands used to build backend image and run container

```
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
docker run --rm -p 4567:4567 -it  -e FRONTEND_URL -e BACKEND_URL backend-flask 
docker build -t backend-flask ./backend-flask
```