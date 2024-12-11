# Django Rest Framework + Remix SPA

## Directory tree

- backend
  - django rest framework files
- frontend
  - remix spa files
- docker
  - backend.dockerfile
    - for development backend
  - frontend.dockerfile
    - for development frontend

## How to run

```
docker-compose up --build
```

## How to access

- frontend: http://localhost:8080
- backend: http://localhost:8000/api/

## How to run manage.py

```
docker-compose exec backend uv run python manage.py ...
```
