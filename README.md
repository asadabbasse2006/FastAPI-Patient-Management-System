# 🏥 Patient Management System API (FastAPI)

This document describes a **Patient Management System API** built using **FastAPI** with **JSON file-based storage**. The API supports full **CRUD (Create, Read, Update, Delete)** operations for managing patient records.

---

## 📌 Technology Stack

- **Framework:** FastAPI  
- **Language:** Python  
- **Data Storage:** JSON file (no database)  
- **Data Format:** JSON  
- **Server:** Uvicorn  

---

## 📂 Project Structure

```text
patient_management_system/
│
├── main.py              # FastAPI application entry point inlcuding Pydantic Models
├── patients.json        # JSON file used as data storage
└── README.md            # API documentation
```

---

## 📄 JSON Data Format

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "weight": 74.2,
    "height": 5.7,
  }
]
```

---

## 📦 Pydantic Model (Patient)

| Field | Type | Description |
|------|------|------------|
| id | int | Unique patient ID |
| name | str | Patient full name |
| age | int | Patient age |
| gender | str | Male / Female / Other |
| disease | str | Diagnosis |
| admitted | bool | Admission status |

---

## 🚀 API Endpoints

### 🔹 Root Endpoint

**GET /**

Returns a welcome message.

```json
{
  "message": "Patient Management System API"
}
```

---

### 🔹 Create a New Patient

**POST /patients**

Adds a new patient record.

**Request Body**
```json
{
  "id": 2,
  "name": "Alice Smith",
  "age": 25,
  "gender": "Female",
  "disease": "Malaria",
  "admitted": true
}
```

**Response**
```json
{
  "message": "Patient added successfully"
}
```

---

### 🔹 Get All Patients

**GET /patients**

Returns a list of all patients.

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "disease": "Flu",
    "admitted": true
  }
]
```

---

### 🔹 Get Patient by ID

**GET /patients/{patient_id}**

Retrieves a single patient record by ID.

```json
{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "gender": "Male",
  "disease": "Flu",
  "admitted": true
}
```

**Error Response**
```json
{
  "detail": "Patient not found"
}
```

---

### 🔹 Update Patient Details

**PUT /patients/{patient_id}**

Updates an existing patient record.

```json
{
  "name": "John Updated",
  "age": 31,
  "gender": "Male",
  "disease": "Cold",
  "admitted": false
}
```

**Response**
```json
{
  "message": "Patient updated successfully"
}
```

---

### 🔹 Delete a Patient

**DELETE /patients/{patient_id}**

Deletes a patient record by ID.

```json
{
  "message": "Patient deleted successfully"
}
```

---

## ⚠️ Error Handling

- **404** – Patient not found  
- **400** – Invalid request data  

FastAPI automatically validates input using **Pydantic models**.

---

## ▶️ How to Run the Project

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

API Documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 🌟 Future Enhancements

- Replace JSON with Database (SQLite / PostgreSQL)
- Add Authentication & Authorization (JWT)
- Pagination & Filtering
- Logging & Exception Middleware

---

## 👨‍💻 Author

**Patient Management System API**  
Built using **FastAPI** for learning backend development.

---

✅ Ideal project for learning **FastAPI CRUD operations without a database**.
