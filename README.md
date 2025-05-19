# Syntaxia Synapse

**Syntaxia Synapse** is a microlearning platform built with FastAPI, Docker, and MongoDB.  
It delivers smart educational stimuli via a modular, containerized architecture — serving as a foundation for more complex educational experiments.

## 🚀 Features

- 🌱 `/estimulo` endpoint: returns a motivational message via FastAPI
- 🐳 Dockerized setup: FastAPI + MongoDB using Docker Compose
- 🔌 Easy to run locally with one command
- 🧱 Ready to scale with more endpoints, database interactions, and background tasks

---

## 🛠 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [MongoDB](https://www.mongodb.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 📁 Project Structure

```
syntaxia-synapse/
├── api/
│   └── main.py                  # FastAPI app with /estimulo route
├── docker/
│   └── Dockerfile               # FastAPI container definition
├── docker-compose.yml          # Orchestrates API and MongoDB containers
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ How to Run Locally

Make sure you have Docker and Docker Compose installed.

1. Clone this repository:
```bash
git clone https://github.com/victoriaglara/syntaxia-synapse.git
cd syntaxia-synapse
```

2. Run the project:
```bash
docker compose up --build
```

3. Access in your browser:
```
http://localhost:8000/estimulo
```

---

## 🔮 Next Steps

- [ ] Connect FastAPI to MongoDB using Motor
- [ ] Serve real motivational content from the database
- [ ] Add route for posting new stimuli
- [ ] Include Redis caching and Kafka messaging
- [ ] Build UI or dashboard for content interaction

---

## ✨ About

This project was created by [victoriaglara](https://github.com/victoriaglara) as a proof of technical ability and as part of a professional application to PUCPR — a place of meaning and purpose.

