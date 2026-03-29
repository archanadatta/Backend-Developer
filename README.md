# 🚀 FastAPI + React Task Manager (RBAC)

A full-stack web application built using FastAPI (backend) and React (frontend) implementing authentication, role-based access control (RBAC), and CRUD operations.

---

## 📌 Features

### 🔐 Authentication
- User Registration & Login
- Password hashing using bcrypt
- JWT-based authentication

### 👤 Role-Based Access Control
- Roles: `user`, `admin`
- Admin-only actions:
  - Delete any task
  - View all tasks
- First registered user becomes **admin**

### 📋 Task Management (CRUD)
- Create tasks
- View tasks
- Update tasks
- Delete tasks (Admin only)

### 🎨 Frontend (React)
- Login & Register pages
- Dashboard with task management
- Conditional UI (admin vs user)
- Inline success/error messages

### 📄 API Documentation
- Swagger UI available at: http://127.0.0.1:8000/docs


### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication

### Frontend
- React.js
- Axios

---

## ⚙️ Setup Instructions

### 🔹 Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

### 🔹 Backend
cd frontend
npm install
npm start


🔐 Security
Password hashing (bcrypt)
JWT token authentication
Role-based route protection
Input validation using Pydantic


🧪 How to Test
Register first user → becomes admin
Login → get JWT token
Access dashboard
Perform CRUD operations
Admin can delete tasks & view all tasks


📸 Screens
Login Page
Register Page
Dashboard (User/Admin)
