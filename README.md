# 🚀 Minimal Observability Stack with Traefik, Fluent Bit & FastAPI

Welcome to the **most minimal logging & observability demo**! 🎪 This project is **not** a production-ready setup but a **simple, beginner-friendly demonstration** of how core components work together using **Docker containers**. If you're new to Traefik, Fluent Bit, Elasticsearch, and FastAPI, this is for you! 🚀

---

## 🎯 What's Inside?

✔️ **Traefik** - A reverse proxy and load balancer 🛡️\
✔️ **Fluent Bit** - A lightweight log processor 💜\
✔️ **Elasticsearch** - Stores and indexes logs 🔍\
✔️ **Kibana** - Visualizes logs beautifully 📊\
✔️ **FastAPI** - A simple app generating logs ⚡\
✔️ **Prometheus** - Collects metrics from services 📈\
✔️ **Grafana** - Visualizes metrics from Prometheus 📊

---

## 🏠 Architecture Overview

```plaintext
                     +--------------------+
                     |    FastAPI App     |
                     +---------+----------+
                               |
                               v
                     +---------+-----------+
                     |       Traefik       |
                     +----+---------+------+
                          |         |
              +-----------+         +---------+
              |                               |
    +---------v----------+           +--------v----------+
    |     Fluent Bit     |           |   Prometheus      |
    +---------+----------+           +--------+----------+
              |                               |
    +---------v--------------+       +--------v----------+
    | Elasticsearch + Kibana |       |      Grafana      |
    +------------------------+       +-------------------+
```

### 🚀 Request Flow

1. **User makes a request** (e.g., `http://localhost/api`).
2. **Traefik receives the request** and routes it to the appropriate backend service (FastAPI).
3. **FastAPI processes the request** and returns a response.
4. **Traefik forwards the response** back to the user.

Meanwhile, in the background:
- **Fluent Bit collects logs** from Traefik and FastAPI, then forwards them to Elasticsearch.
- **Prometheus scrapes metrics** from Traefik and FastAPI.
- **Grafana visualizes the collected metrics.**
- **Kibana visualizes the logs** stored in Elasticsearch.

So, **Traefik is the first point of contact** for all incoming requests before they reach FastAPI. 🚀

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

```sh
git clone https://github.com/joseph815132231518/traefik-demo.git
cd traefik-demo
```

### 2️⃣ Start Everything 🚀

Spin up all services with Docker Compose:

```sh
docker-compose up -d
```

### 3️⃣ Check the Logs 🤨

Ensure Fluent Bit is forwarding logs correctly:

```sh
docker logs traefik-demo-fluent-bit-1
```

Or query Elasticsearch:

```sh
curl -X GET "http://localhost:9200/_cat/indices?v"
```

### 4️⃣ Open Kibana & Set Up Index 🎩✨

1. Go to http://localhost:5601
2. Navigate to Stack Management → Index Patterns
3. Click Create Index Pattern
4. Select the index traefik-logs
5. Choose @timestamp as the time filter field
6. Click Create Index Pattern
7. Navigate to Discover and check for logs

### 5️⃣ Test the FastAPI App ⚡

```sh
curl -X GET "http://localhost/api"
```

Or visit: [http://localhost/api](http://localhost/api)

---

## 📌 Available Endpoints

- **Traefik Dashboard** → [http://localhost:8080](http://localhost:8080)
- **Prometheus UI** → [http://localhost:9090](http://localhost:9090)
- **Grafana UI** → [http://localhost:3000](http://localhost:3000) (default login: `admin` / `admin`)
- **FastAPI Endpoint** → [http://localhost/api](http://localhost/api)
- **Kibana UI** → [http://localhost:5601](http://localhost:5601)
- **Elasticsearch API** → [http://localhost:9200](http://localhost:9200)

---

## ⚠️ Important Notes

- **This is not a production setup!** It's purely educational to show how each component works. 🧪
- **Missing logs in Kibana?** Check Fluent Bit logs: `docker logs traefik-demo-fluent-bit-1`
- **Elasticsearch index issues?** Ensure Fluent Bit is correctly configured.
- **Grafana is running!** Access it at [http://localhost:3000](http://localhost:3000) (login: `admin` / `admin`).

---

## 🎉 Contributing

PRs are welcome! If you think something can be improved for beginners, feel free to contribute! 😎🔥

---

## 🐜 License

MIT - Feel free to use, modify, and share! 🚀
