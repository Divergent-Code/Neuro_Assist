# Neuro-Assist: AI-Powered Accessibility Solution
![Neuro-Assist Logo](docs/neuro_assist_logo.png)

## 📌 Overview
Neuro-Assist is an AI-driven accessibility platform designed to support neurodiverse individuals in various aspects of life, including learning, employment, daily routine management, and mental health monitoring. The platform leverages AI and modern web technologies to provide personalized assistance, secure data handling, and an interactive user experience.

---

## 🎯 Key Features

### 🔹 Personalized Learning Assistance  
🧠 AI-powered recommendations based on individual learning patterns.
📚 Access to curated learning materials tailored to user preferences.

### 🔹 Employment Support  
🔍 AI-driven job recommendations and resume-building tools.
📋 Job application tracking with insights and suggestions.

### 🔹 Routine & Task Management  
⏳ IoT-enabled routine planning and task reminders.
📅 Smart scheduling with priority-based task automation.

### 🔹 Mental Health Monitoring  
💙 AI-based mood tracking and mental health insights.
📊 Data visualization for emotional trends and well-being.

### 🔹 Community Engagement  
🗣️ AI-driven chat assistance for social interaction guidance.
🎭 VR-based social training and real-life interaction simulations.

---

## 🏗️ System Architecture

Neuro-Assist follows a scalable and modular architecture with separate frontend, backend, and database components. The system ensures security, efficiency, and a seamless user experience.

```
Neuro-Assist Project Structure:

📂 neuro_assist/
│── 📂 frontend/ (React.js Web & Flutter Mobile UI)
│── 📂 backend/ (FastAPI API Server)
│── 📂 database/ (PostgreSQL, schema.sql, db.py connection)
│── 📂 tests/ (Unit & Integration Tests targeting port 8000)
│── 📜 README.md
```

### 🚀 Technology Stack
| Component        | Technology Used      |
|-----------------|---------------------|
| Frontend        | React.js, Flutter   |
| Backend         | FastAPI, Python     |
| Database        | PostgreSQL          |
| AI Models       | Google Gemini 2.0 (via lightweight request API) |
| Security        | AES Encryption, JWT, HTTPS |
| Cloud Services  | Google Cloud, Vultr |

---

## 🔐 Security Measures
✅ **Data Encryption** – AES encryption for sensitive data.  
✅ **Secure Authentication** – JWT-based token authentication.  
✅ **HTTPS Communication** – End-to-end encrypted requests.  
✅ **Database Security** – Encrypted PostgreSQL storage.  

---

## 📊 Visual Representation

### **1️⃣ Neuro-Assist Architecture Diagram**
```plaintext
+----------------------------------+
|        Neuro-Assist Platform     |
+----------------------------------+
|  📱 Mobile App (Flutter) | 🖥️ Web UI (React) |
+----------------------------------+
|          Backend API (FastAPI)   |
+----------------------------------+
|   AI Processing (Gemini 2.0 API)  |
+----------------------------------+
| Database (PostgreSQL, Redis Cache)|
+----------------------------------+
```

### **2️⃣ Data Flow Diagram (DFD)**
```plaintext
User → UI → API Gateway → FastAPI → Gemini 2.0 → Database → Response → UI
```

---

## 🚀 Installation & Setup

### **Prerequisites**
- Python 3.12+
- Node.js 18+
- PostgreSQL
- Flutter SDK (optional, for mobile)

### **Backend Setup**
```sh
cd backend/app
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
*(FastAPI server automatically binds database tables and hosts on http://localhost:8000)*

### **Web Frontend Setup**
```sh
cd frontend/web
npm install
npm start
```
*(Web frontend boots on http://localhost:3000 connecting to http://localhost:8000)*

### **Database Setup (Manual Option)**
The backend automatically creates tables on start, but you can manually initialize Postgres via:
```sh
psql -U postgres -d neuro_assist -f database/schema.sql
```

---

## 🛠️ Testing

To run the standalone unit and integration test scripts:
```sh
# Run backend tests
python tests/backend_tests.py

# Run integration tests
python tests/integration_tests.py
```

---

## 🎯 Future Enhancements
- 📌 **AI-based Speech Assistance**
- 📌 **Expanded IoT Integration for Task Automation**
- 📌 **Multi-Language Support**
- 📌 **Blockchain-based Secure Data Storage**

---

## 📞 Contact & Support
For any queries or collaboration, reach out via [prashantbansal529@gmail.com](mailto:email@example.com) or visit our [GitHub Repository](https://github.com/neuro-assist).

Let's build an inclusive digital world together! 🚀
