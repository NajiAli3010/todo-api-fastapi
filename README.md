# 📋 TODO API (FastAPI)

This project is a simple REST API for managing tasks.
It allows users to add tasks, view all tasks, and delete tasks.

The application is built using **FastAPI**, one of the fastest modern frameworks for creating APIs in Python.

---

## 🚀 How to Run Locally

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Start the application**:

```bash
uvicorn app.main:app --reload
```

By default, the server will be available at:  
[http://localhost:8000](http://localhost:8000)

---

## 🐳 Running with Docker

You can also run the app inside a Docker container:

```bash
docker build -t todo-api .
docker run -d -p 8000:8000 todo-api
```

---

## 🧪 Testing

Unit tests are written using **pytest**.

To run the tests locally:

```bash
pytest
```

The tests cover adding a task, listing tasks, and deleting tasks.

---

## 🔄 CI/CD

This project uses **GitHub Actions** for Continuous Integration.  
Every time new code is pushed:
- Linting is checked (with black and ruff),
- Type hints are validated (with mypy),
- Unit tests are run (with pytest).

Only if all checks pass, changes are considered ready.

---

## 📂 Project Structure

```plaintext
app/
├── main.py       # Main FastAPI app
├── models.py     # Task model
├── crud.py       # Task operations (create, list, delete)
tests/
└── test_main.py  # Unit tests
Dockerfile         # Docker config
requirements.txt   # Python dependencies
.github/
└── workflows/
    └── tests.yml # GitHub Actions workflow
```
