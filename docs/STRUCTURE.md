# Basic structure of the project

### Project tree
```
├── LICENSE
├── README.md
├── docker <-- Docker related files for setting dev/prod environment up. 
│   ├── Dockerfile <-- Build docker image
│   ├── docker-compose.yml <-- Compose file
│   └── init_db.sh <-- Tiny file used for the Dockerfile for creating database within container
├── docs <-- Technical decisions related folder
│   └── STRUCTURE.md
├── requirements.txt <-- Dependencies
├── src <-- Source code
│   ├── app <-- FastAPI core application
│   │   ├── api.py <-- Entry point containing FastAPI() object
    │   ├── exceptions <-- Custom exceptions
    │   │   ├── exceptions.py
    │   │   └── __init__.py
│   │   ├── models <-- Pydantic models
│   │   │   ├── __init__.py
│   │   │   └── task.py
│   │   ├── repository <-- Data layer (CRUD)
│   │   │   ├── __init__.py
│   │   │   ├── base_repository.py
│   │   │   └── task_repository.py
│   │   ├── routers <-- HTTP Endpoints
│   │   │   ├── __init__.py
│   │   │   └── tasks.py
│   │   ├── services <-- Business logic, validations and rules
│   │   │   ├── __init__.py
│   │   │   └── tasks_service.py
│   │   └── utils <-- Auxiliary functions
│   │       ├── __init__.py
│   │       ├── fetch_all.py
│   │       ├── fetch_one.py
│   │       └── validate_date.py
│   └── db <-- Database access and setup
│       ├── __init__.py
│       ├── connection.py
│       └── scripts
│           ├── __init__.py
│           └── setup.py
└── tests <-- Test I've not written yet.
```

# 📁 app/  
It contains the core of the FastAPI application: the main instance (`api.py`), routers, services (business logic), repositories (data access), Pydantic models, and internal utilities.
It's the folder where the actual API logic resides.

# 📁 db/  
It contains everything related to the application's internal persistence layer. This includes the SQLite connection configuration (connection.py), as well as database initialization (scripts/)

# 📁 docker/
This includes all files related to the containerization and deployment of the project. The Dockerfile, docker-compose.yml, and any scripts necessary to build and run the application within containers reside here. It represents the infrastructure and runtime layer in real-world or production environments.

# 📁 docs/  
It contains the project documentation, including explanations of the architecture, code structure, design patterns used, and any other information relevant to developers. It serves as a technical reference and a guide for understanding the project design.