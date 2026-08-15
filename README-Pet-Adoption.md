# 🐾 PET ADOPTION REST API

### **Django REST Framework Backend Project**

> **Project Distinction:** A focused, lightweight REST API designed for a **Pet Adoption Management System**, demonstrating core backend development, RESTful API design, data validation, database integration, and API testing using Python and Django.

---

## 📌 Project Overview

The **Pet Adoption REST API** is a backend application developed using **Python, Django, and Django REST Framework (DRF)**.

The project provides a simple and structured API for managing pet adoption data. It allows clients such as **Postman, web applications, or frontend systems** to retrieve pet records and add new pets through RESTful API endpoints.

The project focuses on the core backend requirements:

* REST API development
* Database modeling
* User input handling
* Data validation
* JSON responses
* CRUD foundation
* API testing

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Build a functional backend using Django.
* Develop RESTful API endpoints using Django REST Framework.
* Store and manage pet information in a database.
* Accept and process client-side JSON input.
* Validate incoming data before saving it.
* Return clear JSON responses.
* Test API functionality using Postman.
* Demonstrate clean and structured backend development.

---

## 🛠️ Technology Stack

| Technology                | Purpose                      |
| ------------------------- | ---------------------------- |
| **Python**                | Backend programming language |
| **Django**                | Web framework                |
| **Django REST Framework** | REST API development         |
| **SQLite**                | Database                     |
| **Postman**               | API testing                  |
| **Django Admin**          | Data management              |

---

## 🏗️ Project Architecture

```text
Client / Postman
       │
       ▼
REST API Endpoint
       │
       ▼
Django URL Routing
       │
       ▼
View
       │
       ▼
Serializer
       │
       ▼
Validation
       │
       ▼
Django Model
       │
       ▼
Database
       │
       ▼
JSON Response
```

---

## 📂 Project Structure

```text
Pet-Adoption/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── pets/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

# 🐶 Pet Management

The system manages essential information about each pet, including:

* Pet name
* Species
* Breed
* Age
* Gender
* Adoption status

The `Pet` model provides the database structure for storing this information.

---

# 🔌 API Endpoints

## 1. Get All Pets

### Endpoint

```http
GET /api/pets/
```

### Purpose

Retrieves all available pet records from the database.

### Example Response

```json
[
    {
        "id": 1,
        "name": "Bruno",
        "species": "Dog",
        "breed": "Labrador",
        "age": 2,
        "gender": "Male",
        "adoption_status": "Available"
    }
]
```

---

## 2. Add a New Pet

### Endpoint

```http
POST /api/pets/
```

### Purpose

Accepts pet information from the client, validates the submitted data, and saves the pet to the database.

### Example Request

```json
{
    "name": "Tommy",
    "species": "Dog",
    "breed": "German Shepherd",
    "age": 1,
    "gender": "Male",
    "adoption_status": "Available"
}
```

### Successful Response

```json
{
    "message": "Pet added successfully."
}
```

### Status Code

```text
201 Created
```

---

# ✅ Data Validation

The API validates incoming data before storing it in the database.

Validation includes:

* Required fields
* Empty name validation
* Valid age values
* Valid gender choices
* Valid adoption status choices
* Serializer-level validation
* Model-level field validation

Invalid requests return:

```text
400 Bad Request
```

with an appropriate JSON error response.

---

# 🧪 API Testing

The API has been tested using **Postman**.

### Successful Tests

* ✅ GET all pets
* ✅ POST a valid pet
* ✅ Verify successful pet creation
* ✅ Verify newly created data in Django Admin

### Validation Tests

* ✅ Empty name
* ✅ Missing required field
* ✅ Invalid gender
* ✅ Invalid adoption status
* ✅ Negative age

The tests confirm that the API correctly handles both valid and invalid client input.

---

# 🔐 Authentication

Authentication is **not included** because it is not part of the specified project requirements.

The project therefore remains focused on the required:

* API endpoints
* User input
* Validation
* Database interaction
* JSON responses

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Pet-Adoption
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install django djangorestframework
```

## 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Create Admin User

```bash
python manage.py createsuperuser
```

## 7. Start Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🖥️ Django Admin

The Django Admin interface can be accessed through:

```text
http://127.0.0.1:8000/admin/
```

The admin panel allows authorized administrators to:

* Add pets
* View pets
* Edit pet information
* Delete pet records
* Filter pet records
* Search pet records

---

# 📡 API Testing with Postman

### GET Request

```text
GET http://127.0.0.1:8000/api/pets/
```

### POST Request

```text
POST http://127.0.0.1:8000/api/pets/
```

For POST requests, use:

```text
Body → raw → JSON
```

and provide the required pet information.

---

# 🔄 Request & Response Flow

### GET Request

```text
Client
  ↓
GET /api/pets/
  ↓
Django View
  ↓
Pet Model
  ↓
Pet Serializer
  ↓
JSON Response
```

### POST Request

```text
Client
  ↓
POST /api/pets/
  ↓
request.data
  ↓
Pet Serializer
  ↓
Validation
  ↓
Database
  ↓
Success / Error Response
```

---

# 📋 Requirement Completion

| Requirement           | Status      |
| --------------------- | ----------- |
| Python Backend        | ✅ Completed |
| Django Framework      | ✅ Completed |
| Django REST Framework | ✅ Completed |
| Database Model        | ✅ Completed |
| GET API               | ✅ Completed |
| POST API              | ✅ Completed |
| User Input Handling   | ✅ Completed |
| Basic Validation      | ✅ Completed |
| JSON Responses        | ✅ Completed |
| Django Admin          | ✅ Completed |
| API Testing           | ✅ Completed |

---

# 💡 Key Backend Concepts Demonstrated

This project demonstrates practical understanding of:

* Django project structure
* Django applications
* Models
* Database migrations
* Django Admin
* REST APIs
* HTTP methods
* GET requests
* POST requests
* Serializers
* Serializer validation
* Request data handling
* JSON responses
* HTTP status codes
* API testing with Postman

---

# 🚀 Project Highlights

### 🐾 Pet-Focused Backend

A practical backend scenario based on pet adoption management.

### 🔌 RESTful API

Simple and structured endpoints for client-server communication.

### 🛡️ Data Validation

Incoming data is validated before database insertion.

### 🗄️ Database Integration

Pet records are stored and managed through Django's ORM.

### 🧪 Tested API

Endpoints and validation behavior are tested using Postman.

### 🧩 Clean Architecture

The project separates models, serializers, views, and URL routing according to Django/DRF conventions.

---

# 👩‍💻 Project Purpose

This project was developed as a **Python + Django backend internship project** to demonstrate practical knowledge of backend development and RESTful API implementation.

The implementation focuses specifically on the **required project functionality**, keeping the system simple, maintainable, and easy to extend in the future.

---

## 📄 License

This project is developed for educational and internship purposes.

---

### ⭐ Pet Adoption REST API

**Built with Python • Django • Django REST Framework**
