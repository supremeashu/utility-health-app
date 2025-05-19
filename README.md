# utility-health-app
A cross-platform utility to collect system health data An admin dashboard to centrally view this data

- `admin-backend`: Backend service using Node.js
- `admin-frontend`: Frontend web interface using React
- `system_utility`: CLI-based utilities for interacting with the backend

---


## 🛠️ Tech Stack

### 📦 Backend (`admin-backend`)
- Node.js
- Express.js
- MongoDB
- JWT for authentication
- bcrypt for password hashing

### 🎨 Frontend (`admin-frontend`)
- React
- Tailwind CSS

### 🖥️ CLI Utility (`system_utility`)
- Node.js
- Interacts with backend APIs via command-line


--- 

## ⚙️ Technologies Used

- **Frontend**: React, Tailwind CSS
- **Backend**: Node.js, Express.js, MongoDB
- **CLI Utility**: Node.js
- **Authentication**: JWT (JSON Web Tokens)

---

## 🚀 Getting Started

### 1. Clone the repository

### 2. Environment Setup
Backend (admin-backend/)
Create a .env file in admin-backend/ using .env.example as a template:

```bash
PORT=5000
MONGO_URI=your_mongodb_uri
JWT_SECRET=your_secret_key
```
Install dependencies and run:

```bash
cd admin-backend
npm install
npm start
```
Frontend (admin-frontend/)
Navigate to the frontend directory:

```bash
cd ../admin-frontend
npm install
npm start
```
This will start the development server at http://localhost:3000

---

## 🌟 Features
### Admin Frontend
Login system with JWT token handling

Dashboard UI with user and system statistics

Responsive layout using Tailwind CSS

### Backend API
User authentication with hashed passwords

Protected routes using JWT

Modular controller and route structure

### System Utility
Command-line interface to interact with the backend

Easy to use for internal scripts or automation

## 🧪 Example API Usage
- Login: POST /api/auth/login

- Get Users: GET /api/users (JWT token required)

- Update Settings: PUT /api/settings

Use tools like Postman or curl to test these endpoints.
