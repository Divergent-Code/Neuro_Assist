# Neuro-Assist API Documentation

Welcome to the **Neuro-Assist API** documentation. The server is built on **FastAPI** and runs on `http://localhost:8000`. It provides a secure, modular backend for personalized learning, career assistance, routine management, and cognitive wellbeing.

---

## 🔐 Authentication & Session Security

JWT-based authentication is configured. Successful login yields a Bearer token that should be supplied in the `Authorization: Bearer <token>` header of protected routes.

### 1. Register User
* **Endpoint**: `POST /auth/register`
* **Content-Type**: `application/json`
* **Request Schema (`UserCreate`)**:
  ```json
  {
    "username": "tester",
    "email": "tester@example.com",
    "password": "securepassword123"
  }
  ```
* **Response Schema (`UserResponse`)** — *Status 201 Created*:
  ```json
  {
    "id": 1,
    "username": "tester",
    "email": "tester@example.com",
    "is_active": true,
    "created_at": "2026-05-16T22:50:00Z"
  }
  ```
  *(Note: A default blank profile is automatically initialized on registration).*

### 2. User Login
* **Endpoint**: `POST /auth/login`
* **Content-Type**: `application/json`
* **Request Schema (`UserLogin`)**:
  ```json
  {
    "email": "tester@example.com",
    "password": "securepassword123"
  }
  ```
* **Response Schema (`Token`)** — *Status 200 OK*:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }
  ```

---

## 👤 User Profile Management

### 1. Fetch My Profile (Authenticated)
* **Endpoint**: `GET /users/profile`
* **Headers**: `Authorization: Bearer <access_token>`
* **Response Schema (`UserProfileResponse`)** — *Status 200 OK*:
  ```json
  {
    "id": 1,
    "user_id": 1,
    "full_name": "tester",
    "bio": "",
    "interests": ""
  }
  ```

### 2. Fetch Profile by User ID (Direct Lookup)
* **Endpoint**: `GET /users/profile/{user_id}`
* **Response Schema (`UserProfileResponse`)** — *Status 200 OK*:
  ```json
  {
    "id": 1,
    "user_id": 1,
    "full_name": "tester",
    "bio": "",
    "interests": ""
  }
  ```

---

## 📚 Learning Assistance API

Provides personalized study logs and recommended educational content urls.

### 1. Add Learning Material
* **Endpoint**: `POST /learning/materials`
* **Request Schema (`LearningMaterialCreate`)**:
  ```json
  {
    "user_id": 1,
    "title": "Intro to Python Loops",
    "description": "Visual walkthrough of loop mechanics",
    "content_url": "https://example.com/python-loops",
    "entry_text": "I learn best when loop iterations are visualized as steps in a staircase."
  }
  ```
* **Response Schema (`LearningMaterialResponse`)** — *Status 201 Created*:
  ```json
  {
    "id": 1,
    "user_id": 1,
    "title": "Intro to Python Loops",
    "description": "Visual walkthrough of loop mechanics",
    "content_url": "https://example.com/python-loops",
    "entry_text": "I learn best when loop iterations are visualized as steps in a staircase.",
    "created_at": "2026-05-16T22:52:00Z"
  }
  ```

### 2. Fetch Learning Materials
* **Endpoint**: `GET /learning/materials`
* **Query Parameters**: `user_id` (optional, filter by specific user)
* **Response Schema**: `List[LearningMaterialResponse]`

---

## 💼 Employment Support API

Manages resume and career profile insights.

### 1. Add Job Listing / Insight
* **Endpoint**: `POST /jobs/jobs`
* **Request Schema (`JobListingCreate`)**:
  ```json
  {
    "user_id": 1,
    "title": "Junior Python Developer",
    "company": "TechCorp",
    "location": "Remote",
    "description": "Python, FastAPI development with flexible hours",
    "entry_text": "Requires good documentation skills and asynchronous work patterns."
  }
  ```
* **Response Schema (`JobListingResponse`)** — *Status 201 Created*:
  ```json
  {
    "id": 1,
    "user_id": 1,
    "title": "Junior Python Developer",
    "company": "TechCorp",
    "location": "Remote",
    "description": "Python, FastAPI development with flexible hours",
    "entry_text": "Requires good documentation skills and asynchronous work patterns.",
    "created_at": "2026-05-16T22:52:10Z"
  }
  ```

### 2. Fetch Job Listings
* **Endpoint**: `GET /jobs`
* **Query Parameters**: `user_id` (optional, filter by specific user)
* **Response Schema**: `List[JobListingResponse]`

---

## ⏳ Routine & Task Management API

Automates routine notifications and schedules.

### 1. Add Routine Task
* **Endpoint**: `POST /routine/tasks`
* **Request Schema (`RoutineTaskCreate`)**:
  ```json
  {
    "user_id": 1,
    "task_name": "Morning Planning Block",
    "schedule_time": "2026-05-16T09:00:00Z",
    "entry_text": "Review visual timeline while drinking tea."
  }
  ```
* **Response Schema (`RoutineTaskResponse`)** — *Status 201 Created*:
  ```json
  {
    "id": 1,
    "user_id": 1,
    "task_name": "Morning Planning Block",
    "schedule_time": "2026-05-16T09:00:00Z",
    "entry_text": "Review visual timeline while drinking tea."
  }
  ```

### 2. Fetch Routine Tasks
* **Endpoint**: `GET /routine/tasks`
* **Query Parameters**: `user_id` (optional, filter by specific user)
* **Response Schema**: `List[RoutineTaskResponse]`

---

## 💙 Mental Health & Mood Monitoring API

### 1. Add Mood Log Entry
* **Endpoint**: `POST /health/entries`
* **Request Schema (`MentalHealthEntryCreate`)**:
  ```json
  {
    "user_id": 1,
    "mood": "Calm",
    "notes": "Workstation is clean, lighting is soft.",
    "entry_text": "Focused and breathing steady."
  }
  ```
* **Response Schema (`MentalHealthEntryResponse`)** — *Status 201 Created*:
  ```json
  {
    "id": 1,
    "user_id": 1,
    "mood": "Calm",
    "notes": "Workstation is clean, lighting is soft.",
    "entry_text": "Focused and breathing steady.",
    "created_at": "2026-05-16T22:52:30Z"
  }
  ```

### 2. Fetch Mood Log Entries
* **Endpoint**: `GET /health/entries`
* **Query Parameters**: `user_id` (optional, filter by specific user)
* **Response Schema**: `List[MentalHealthEntryResponse]`

---

## 📚 API Execution Verification via cURL

Start the API and trigger the verification chain via command line:

```bash
# Register User
curl -X POST "http://localhost:8000/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"username": "demo", "email": "demo@example.com", "password": "password123"}'

# Login
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/json" \
     -d '{"email": "demo@example.com", "password": "password123"}'
```
