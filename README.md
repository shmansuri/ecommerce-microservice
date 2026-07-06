# 🚀 E-Commerce Microservices Backend

A production-grade E-Commerce Backend built using Microservices Architecture with FastAPI.

> This project is being developed as part of a structured backend engineering roadmap focusing on production-ready architecture rather than simple CRUD applications.

---

## 🎯 Project Goal

The goal of this project is to build a scalable backend that demonstrates real-world backend engineering concepts used in modern software companies.

---

## 🏗️ Planned Architecture

```
                        API Gateway
                             │
        ┌────────────┬────────────┬────────────┐
        │            │            │
   Auth Service  Product Service  Order Service
        │            │            │
     PostgreSQL   PostgreSQL   PostgreSQL
             │
        Notification Service
```

> This architecture will evolve as the project progresses.

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- Python

### Database

- PostgreSQL

### ORM

- SQLAlchemy 2.0

### Authentication

- JWT

### Caching

- Redis

### Background Tasks

- Celery

### Message Broker

- RabbitMQ

### Containerization

- Docker
- Docker Compose

### Reverse Proxy

- Nginx

### Cloud

- AWS EC2

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
ecommerce-microservice/

ROADMAP.md

README.md

auth-service/

product-service/

order-service/

notification-service/

gateway/

docker-compose.yml
```

> The folders will be added gradually during development.

---

## 📌 Current Progress

- [x] Repository Created
- [x] Roadmap Created
- [ ] FastAPI Setup
- [ ] Auth Service
- [ ] Product Service
- [ ] Order Service
- [ ] Docker
- [ ] Redis
- [ ] RabbitMQ
- [ ] Deployment

---

## 📚 Learning Focus

This project focuses on learning and implementing:

- Clean Architecture
- Microservices
- REST APIs
- Authentication & Authorization
- Docker
- Distributed Systems Basics
- Event-Driven Architecture
- Backend Best Practices

---

## 📄 License

This repository is created for educational purposes and backend engineering practice.