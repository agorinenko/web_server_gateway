# Python Web Server Gateway

Реализация приложения и тестового сервера на python с использованием стандартов WSGI и ASGI

## WSGI

Вызов приложения с использованием стандарта wsgi

```
python -m wsgi
```

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