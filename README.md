# Tasks API 📄

The purpose of this API is implement basic HTTP operations for an web application built in React.
It's not a fully implemented project and its own name lets you know that it isn't a complex project.
Even so, this is a small sample of all the things that I've learned so far. 
I've built bigger projects with FastAPI but they belong to the company I work for, so I can't show their code :).

---

# Why FastAPI ❓

I'm quite surprised how fast it is to develop an API with this framework and also it's nice to know that its creator is Colombian, just like I am.
The fact that it's fully async and matches other frameworks in terms of performance is very appealing.
Sometimes you don't need anything fancy or bloated and you just want to focus on one thing and do it well, that's what I think whenever I have to choose between frameworks like DRF or FastAPI.

---

# Environment setup 🛠️

Feel free to clone this project and do with this whatever you want or contribute if that's so.
```bash
git clone https://github.com/kkrlosdev/tasks_api.git
```
Then
```bash
cd tasks_api
```
Install dependencies
```bash
pip install -r requirements.txt
```
I also recommend using Docker Compose to develop and set up your own environment, there's already a file dedicated for that (make sure you have Docker Compose Plugin installed on your machine):
- Unix-like systems
```bash
docker compose -f ./docker/docker-compose.yml up --build -d
```
- Windows
```bash
docker compose -f .\docker\docker-compose.yml up --build -d
```

Then visit `http://localhost:8000/docs` on your browser to see SwaggerUI documentation.