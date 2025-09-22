📝 Flask Notes Webapp with Docker Compose
📘 Project Overview

This project is part of the DEPI DevOps learning series.
We built a simple note-taking web application using Python (Flask) and MySQL, containerized it with Docker, and orchestrated it with Docker Compose.

With one command, you can bring up the entire stack (Flask + MySQL) and start taking notes.

🎯 Features

Add and view notes through a web UI.

Store notes in MySQL with timestamps.

REST API endpoints:

POST /notes → create a new note

GET /notes → list all notes in JSON

GET /healthz → health check (DB connectivity)

Persistent MySQL data using Docker named volumes.

Configurable via .env file (no secrets committed).

Health checks for both services.

🏗️ Project Structure
flask-notes-docker/
│── app/
│   ├── app.py
│   ├── __init__.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│
│── db/
│   └── init/
│       └── schema.sql
│
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── .env.example
│── README.md
│── docs/ (optional screenshots/diagram)

⚙️ Setup Instructions
1. Clone the repo
git clone https://github.com/MohammedHamdy1555/DevOps-Projects/tree/main/flask-notes-docker
cd flask-notes-docker

2. Configure environment

Copy .env.example → .env and update values:

cp .env.example .env


Example:

MYSQL_ROOT_PASSWORD=changeme
DB_NAME=notesdb
DB_USER=noteuser
DB_PASSWORD=notepass

3. Start the stack
docker-compose up -d --build

4. Access the app

Web UI: http://<EC2-PUBLIC-IP>:5000

API (examples below)

🧪 API Examples
Create a Note
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"Buy milk"}' \
  http://<EC2-PUBLIC-IP>:5000/notes

List Notes
curl http://<EC2-PUBLIC-IP>:5000/notes

Health Check
curl http://<EC2-PUBLIC-IP>:5000/healthz

🗂️ Managing Containers

Stop stack:

docker-compose down


Stop & remove data:

docker-compose down -v


Logs:

docker-compose logs -f

📌 Notes

MySQL data persists in the notes_data named volume.

App runs as a non-root user inside the container.

.env.example is provided, but .env should not be committed.

