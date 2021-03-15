# Python Web Server Gateway

Реализация приложения на python с использованием стандартов WSGI и ASGI

## WSGI

Запуск тестового приложения на gunicorn.

```
docker-compose -f docker-compose.wsgi.yml up -d --build
```

Запрос

```
curl http://127.0.0.1:8000
```

Ответ

```json
{
  "text": "Hello world!"
}
```

## ASGI

Запуск тестового приложения на uvicorn.

```
docker-compose -f docker-compose.asgi.yml up -d --build
```

Запрос

```
curl http://127.0.0.1:8000
```

Ответ

```json
{
  "text": "Hello world!"
}
```