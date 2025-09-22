# 🛠️ Flask Note-Taking App Deployment with Ansible

This project demonstrates how to deploy a simple note-taking web application using **Flask**, **SQLite**, and **Ansible** on an **Amazon Linux EC2 instance**.

---

## 📦 Technologies Used

- 🔹 Ansible (Role-based structure)
- 🔹 Flask (Python micro web framework)
- 🔹 SQLite (lightweight local DB)
- 🔹 Amazon Linux 2023 (EC2 t2.micro)
- 🔹 HTML (Jinja2 templates)

---

## 🧱 Project Structure

ansible-project/
├── ansible.cfg
├── deploy.yml
├── hosts
├── README.md
└── roles/
└── noteapp/
├── tasks/
│   └── main.yml
├── files/
│   ├── app.py
│   └── index.html

---

## 🚀 How to Deploy

### 1. ✅ Prerequisites

- EC2 controller instance (Ansible installed)
- EC2 agent instance (Amazon Linux, Flask installed)
- SSH access between controller and agent (via PEM key)

### 2. ⚙️ Inventory file (`hosts`)

Example:

ini
[agents]
agent1 ansible_host=AGENT_PUBLIC_IP ansible_user=ec2-user ansible_ssh_private_key_file=ansible.pem


### 3. ▶️ Run the playbook

bash
cd ansible-project
ansible-playbook -i hosts deploy.yml

---

## 📝 Web App Features

* Users can submit notes via web form
* Notes are saved to a SQLite database with timestamps
* All submitted notes are displayed in reverse chronological order

---

## 🌐 Access the App

Once deployed, access the app via the agent’s public IP:

http://<AGENT_PUBLIC_IP>

---
