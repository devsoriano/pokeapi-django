# Pokémon API Project

Este proyecto proporciona una API para gestionar y consumir datos relacionados con Pokémon, incluyendo detalles como habilidades, tipos, peso y más.

## Características

- **Gestión de Pokémon**: Incluye un `job` que obtiene datos de Pokémon desde la [PokeAPI](https://pokeapi.co/).
- **Habilidades**: Guarda información única sobre las habilidades de los Pokémon, incluyendo descripciones.
- **Paginación**: La API permite obtener datos paginados para mejorar la experiencia del usuario.
- **Caché**: Optimización de rendimiento mediante almacenamiento en caché.

---

## Tecnologías utilizadas

- **Backend**: Django
- **Base de datos**: PostgreSQL
- **Caché**: Django Cache (LocMemCache o Redis, según configuración)
- **Docker**: Contenedores para el despliegue
- **Frontend**: Vite + React (separado)

---

## Instalación y configuración

### Requisitos previos

- Docker y Docker Compose instalados en tu sistema.
- Python 3.10 o superior.

### Clonar el repositorio

```bash
git clone https://github.com/devsoriano/pokeapi-django.git
```

### Correr el proyecto

```bash
 docker-compose up --build
```

- Al ejecutar este comando la shell hará muchas cosas por nosotros, todos los comandos de manage.py necesarios para crear las tablas necesarias y poblarlas

### Probar los servicios en localhost 
- [Job para poblar datos (Local)](http://localhost:8000/run-job/)
  <img width="998" alt="image" src="https://github.com/user-attachments/assets/a17400d9-f759-40fc-b643-92d4c29edd16">

- [Consultar Pokemons (Local)](http://localhost:8000/get-pokemons/?page=1)
  <img width="998" alt="image" src="https://github.com/user-attachments/assets/a0d66020-8170-42e8-b08a-f7377127c307">

- [Catálogo de habilidades (Local)](http://localhost:8000/get-abilities/)
  <img width="998" alt="image" src="https://github.com/user-attachments/assets/61f88ad8-01e2-465d-b542-e55aa56661c4">

### Probar los servicios productivos (AWS)
- [Job para poblar datos (Producción)](http://18.208.163.231:8000/run-job/)
  <img width="998" alt="image" src="https://github.com/user-attachments/assets/748de65b-79ea-4f4c-8da6-24d40b53304c">

- [Consultar Pokemons (Producción)](http://18.208.163.231:8000/get-pokemons/?page=1)
  <img width="998" alt="image" src="https://github.com/user-attachments/assets/b33f5975-98aa-430e-ab75-bf806f13456a">


- [Catálogo de habilidades (Producción)](http://18.208.163.231:8000/get-abilities/)
  <img width="998" alt="image" src="https://github.com/user-attachments/assets/24db3605-c9fc-48ab-8fda-9318bb8d0fc1">

### Superadmin
Para ingresar como administrador se toma:

- [Admin local](http://localhost:8000/admin/)
  ![image](https://github.com/user-attachments/assets/4a19ee50-1f0a-4224-be56-21e2a05d1688)
  
- [Admin productivo](http://18.208.163.231:8000/admin/)
  ![image](https://github.com/user-attachments/assets/74ca0948-e6e2-4d32-8add-9e3f42fd45d9)

### Credenciales:

- Usuario: admin
- Password: Un1Tip5?¿xl

### Una vez logueado se pueden ver los servicios ya poblados

![image](https://github.com/user-attachments/assets/34bb7ee6-6c5a-413b-9df4-70cb4e8211a5)

![image](https://github.com/user-attachments/assets/f770904d-76af-476f-9518-4d8f7a97eb16)

![image](https://github.com/user-attachments/assets/2c2f8464-4ad1-4082-9534-7cdf58b7349b)


### Mejoras por hacer

- Realizar un caché en Redis
- Variables de entorno
- Separación semántica a controladores
- Certificado ssh 


