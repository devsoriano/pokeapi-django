
# 🎮 PokeAPI Django REST Framework 🌟

![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.14-green?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-✓-0db7ed?style=flat-square&logo=docker)

Welcome to the **PokeAPI** project! 🌈 This app brings the exciting world of Pokémon into your hands by leveraging Django REST Framework and Celery to build a scalable and interactive RESTful API.

---

## 🌟 Features

- 🐾 **Pokemon Management**: CRUD operations for Pokémons and their abilities.
- 🌀 **Fetch Them All**: Automatically fetch the first 150 Pokémon directly from PokeAPI with just a POST request.
- 📄 **Pagination**: Browse Pokémons in pages (20 per page).
- 📊 **Dockerized**: Easily deployable with Docker.

---

## 📜 Table of Contents

- [🚀 Installation](#-installation)
- [🛠️ How to Use](#️-how-to-use)
- [📂 Project Structure](#-project-structure)
- [👨‍💻 Testing](#-testing)

---

## 🚀 Installation

1. Clone the repo and navigate into the project folder:

   ```bash
   git clone https://github.com/devsoriano/pokeapi-django.git
   cd pokeapi-django
   ```

2. Spin up the Docker containers:

   ```bash
   docker-compose up --build
   ```

---

## 🛠️ How to Use

### 🔗 API Endpoints

| Endpoint                               | Method | Description                         |
|----------------------------------------|--------|-------------------------------------|
| `/api/pokemons/`                       | `GET`  | List all Pokémons                  |
| `/api/pokemons/{id}/`                  | `GET`  | Retrieve a specific Pokémon         |
| `/api/pokemons/`                       | `POST` | Create a new Pokémon                |
| `/api/pokemons/{id}/`                  | `PUT`  | Update an existing Pokémon          |
| `/api/pokemons/{id}/`                  | `DELETE`| Delete a Pokémon                   |
| `/api/pokemons/job/fetch-all/`         | `POST` | Fetch the first 150 Pokémon from API|
| `/swagger/`                            | `GET`  | View API documentation (Swagger UI) |

### 🌀 Fetching Pokémons

1. Open Postman or any REST client.
2. Send a `POST` request to:
   ```
   http://localhost:8000/api/pokemons/job/fetch-all/
   ```
3. Watch the magic happen!

---

## 📂 Project Structure

```
pokeapi/
├── Dockerfile
├── Postman-Collection.json
├── README.md
├── __init__.py
├── __pycache__
├── apps
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-39.pyc
│   ├── abilities
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── pokemons
│       ├── __init__.py
│       ├── __pycache__
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       ├── models.py
│       ├── pagination.py
│       ├── permissions.py
│       ├── serializers.py
│       ├── tasks.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── celery_app.py
├── celerybeat-schedule
├── db.sqlite3
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── settings.py
├── start.sh
├── static
├── templates
├── urls.py
└── wsgi.py

```

---

## 👨‍💻 Testing

Run all unit tests:

```bash
docker exec -it pokeapi-web-1 python manage.py test
```

---

## 📧 Contact

Created with ❤️ by [Devsoriano](https://github.com/devsoriano).
