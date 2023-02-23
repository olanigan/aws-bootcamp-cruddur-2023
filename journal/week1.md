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