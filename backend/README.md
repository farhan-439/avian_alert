Here’s a professional, updated `README.md` for your **Avian Alert backend**, based on everything we've built so far:

---

# 🐔 Avian Alert – Backend (Flask)

This backend powers **Avian Alert**, an AI-driven poultry health monitoring system. It handles user authentication, flock management, audio/image detection, and health status tracking. Built with Flask, SQLAlchemy, JWT, and deep learning integrations.

---

## ⚙️ Tech Stack

- Python + Flask
- SQLAlchemy (SQLite / PostgreSQL)
- JWT-based Authentication
- TensorFlow/Keras (for ML models)
- CORS-enabled API
- Modular project architecture

---

## 📁 Project Structure

```
avian-alert-backend/
│
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── config.py                # App config (secret key, DB URI, etc.)
│   ├── models/                  # SQLAlchemy models
│   │   ├── user.py
│   │   ├── flock.py
│   │   ├── audio_detection.py
│   │   └── image_detection.py
│   ├── services/                # Business logic
│   │   ├── auth_service.py
│   │   ├── audio_service.py
│   │   └── image_service.py
│   ├── routes/                  # API endpoints
│   │   ├── auth_routes.py
│   │   ├── flock_routes.py
│   │   ├── audio_routes.py
│   │   └── image_routes.py
│   ├── utils/                   # JWT, processing helpers
│   │   └── jwt_utils.py
│
├── uploads/images/             # Saved image uploads
├── run.py                      # Entry point
├── requirements.txt
└── README.md                   # This file
```

---

## 🔐 Authentication (Custom JWT System)

- Users register/login using email + password
- Passwords are hashed using Werkzeug
- JWTs issued on login, with 7-day expiry
- `@jwt_required` decorator protects all user-specific routes
- Token payload:
```json
{
  "user_id": 42,
  "exp": 1745567890
}
```

**Authorization Header Format:**
```http
Authorization: Bearer <your-jwt-token>
```

---

## 🧬 Database Models

### `User`
- `id`, `email`, `password`, `created_at`

### `Flock`
- `id`, `name`, `location`, `user_id`, `created_at`

### `AudioDetection`
- `id`, `flock_id`, `prediction`, `confidence`, `timestamp`

### `ImageDetection`
- `id`, `flock_id`, `prediction`, `confidence`, `image_path`, `timestamp`

---

## 📦 API Routes

### 🔑 Auth (`/auth`)
| Method | Endpoint       | Description              |
|--------|----------------|--------------------------|
| POST   | `/register`    | Register a new user      |
| POST   | `/login`       | Authenticate and get JWT |

---

### 🐓 Flocks (`/api/flocks`)
| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| GET    | `/`              | Get all user’s flocks   |
| POST   | `/`              | Create a new flock      |

---

### 🎧 Audio Detection (`/api/audio`)
| Method | Endpoint        | Description                            |
|--------|-----------------|----------------------------------------|
| POST   | `/upload`       | Upload audio file for prediction       |

**Form Data:**  
- `audio`: audio file (`.wav`, `.mp3`, etc.)  
- `flock_id`: integer

---

### 📸 Image Detection (`/api/image`)
| Method | Endpoint        | Description                            |
|--------|-----------------|----------------------------------------|
| POST   | `/upload`       | Upload image for disease classification |

**Form Data:**  
- `image`: image file  
- `flock_id`: integer

---

## 🚀 Running the App

### 1. Clone and Install
```bash
git clone <repo-url>
cd avian-alert-backend
pip install -r requirements.txt
```

### 2. Run Server
```bash
export FLASK_APP=run.py
flask run
```

### 3. Initialize DB
```python
from app import create_app
from app.models.user import db
app = create_app()
with app.app_context():
    db.create_all()
```

---

## 📌 Next Steps

- Add `/simulate_farm` for audio simulation
- Add email/notification support
- Integrate frontend dashboard

---

Let me know if you want this generated into a file or zipped into a GitHub starter repo!