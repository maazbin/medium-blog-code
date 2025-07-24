
# 📚 Book Catalog API

A clean and simple **FastAPI** application to manage a catalog of books.  
It follows a modular structure with separate layers for API, service, CRUD, and models — using SQLite for persistence.

---

## 🚀 Features

- FastAPI-based RESTful API
- Sync database using SQLite
- Clean folder structure (clean architecture)
- Docker support
- Auto-generated Swagger UI
- Pydantic validation
- Unit and integration test setup

---

## 📦 Requirements

- Python 3.9+
- Pip
- (Optional) Docker + Docker Compose

---

## 🛠️ Run the Project (Without Docker)

### 1. Clone or extract the project

```bash
unzip book_catalog.zip
cd book_catalog
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

Visit the docs at:  
📘 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Run with Docker

### 1. Build and run

```bash
docker-compose up --build
```

App will be available at:  
📘 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✍️ API Usage Examples

### ✅ Create a Book

**POST** `/books/`  
```json
{
  "title": "The Pragmatic Programmer",
  "author": "Andy Hunt",
  "published_year": 1999,
  "summary": "A book about software craftsmanship"
}
```

---

### 📚 Get All Books

**GET** `/books/`

---

### 📖 Get a Book by ID

**GET** `/books/1`

---

### ✏️ Update a Book

**PUT** `/books/1`  
```json
{
  "title": "Updated Title",
  "author": "Updated Author",
  "published_year": 2000,
  "summary": "Updated summary"
}
```

---

### ❌ Delete a Book

**DELETE** `/books/1`

---

## 🧪 Run Tests

> Run from project root (where the `app/` folder exists):

### ✅ Linux/macOS:

```bash
PYTHONPATH=. pytest
```

### ✅ Windows PowerShell:

```powershell
$env:PYTHONPATH = "."; pytest
```

---

## 📂 Folder Structure

```
book_catalog/
├── app/
│   ├── api/v1/           # API routes
│   ├── core/             # DB connection
│   ├── crud/             # DB logic
│   ├── services/         # Business logic
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   └── main.py           # Entry point
├── tests/                # Unit + API tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 Author

Maaz 

---
