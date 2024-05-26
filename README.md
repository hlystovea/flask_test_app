# To-do app

## Контракт

1. Создание задачи:
- Метод: POST
- URL: /tasks
- Параметры запроса: JSON-объект с полями title (строка) и description (строка, опционально).
- Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

2. Получение списка задач:
- Метод: GET
- URL: /tasks
- Ответ: JSON-список задач, где каждая задача представляет собой JSON-объект с полями id, title, description, created_at, updated_at.

3. Получение информации о задаче:
- Метод: GET
- URL: /tasks/<id>
- Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

4. Обновление задачи:
- Метод: PUT
- URL: /tasks/<id>
- Параметры запроса: JSON-объект с полями title (строка, опционально) и description (строка, опционально).
- Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

5. Удаление задачи:
- Метод: DELETE
- URL: /tasks/<id>
- Ответ: Сообщение об успешном удалении.


## Инструменты
- Python 3.12
- Flask 3.0
- Docker
- Nginx
- MySQL


## Установка (Linux)
У вас должен быть установлен [Docker Compose](https://docs.docker.com/compose/)

1. Клонирование репозитория

```git clone https://github.com/hlystovea/flask_test_app.git```  

2. Переход в директорию flask_test_app

```cd flask_test_app```

3. Создание файла с переменными окружения

```cp env.example .env```

4. Заполнение файла .env своими переменными

```nano .env```

5. Запуск проекта

```sudo docker compose up -d```

6. Запуск миграций

```sudo docker compose exec backend flask db upgrade```

7. Приложение будет доступно по адресу
 
```http://127.0.0.1```
