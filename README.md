# 🏥 Patient Management System API (FastAPI)

This is a **Patient Management System REST API** built using **FastAPI**.  
The application performs **CRUD operations** on patient records stored in a **JSON file (`patients.json`)**.

The API also supports:
- BMI calculation
- Health verdict generation
- Sorting patients by height, weight, or BMI

---

## 📌 Tech Stack

- **Backend Framework:** FastAPI  
- **Language:** Python  
- **Data Storage:** JSON file  
- **Validation:** Pydantic  
- **Server:** Uvicorn  

---

## 📂 Project Structure

```text
.
├── main.py          # FastAPI application
├── patients.json    # JSON file storing patient records
└── README.md        # API documentation
```

---

## 📄 JSON Data Structure (`patients.json`)

```json
{
  "P001": {
    "name": "Asad Abbas",
    "city": "Ahmadpur East",
    "age": 21,
    "gender": "male",
    "height": 5.6,
    "weight": 47,
    "bmi": 33.06,
    "verdict": "Underweight"
  }
}
```

Each patient is stored with a **unique patient ID** as the key.

---

## 📦 Pydantic Models

### 🔹 Patient Model

| Field | Type | Description |
|------|------|------------|
| id | str | Unique patient ID (e.g., P001) |
| name | str | Patient name |
| city | str | City of residence |
| age | int | Age (1–120) |
| gender | male / female / others | Gender |
| height | float | Height in meters |
| weight | float | Weight in kg |
| bmi | float | Auto-calculated BMI |
| verdict | str | Health status based on BMI |

### 🔹 Computed Fields

- **BMI** = weight / height²  
- **Verdict Logic**
  - BMI < 18.5 → Underweight  
  - BMI < 25 → Normal  
  - BMI < 30 → Normal  
  - BMI ≥ 30 → Obese  

---

## 🚀 API Endpoints

### 🔹 Root Endpoint

**GET /**

```json
{
  "message": "Patient Management System"
}
```

---

### 🔹 About API

**GET /about**

```json
{
  "message": "A fully functional system to manage the patient records."
}
```

---

### 🔹 View All Patients

**GET /view**

Returns all patient records from `patients.json`.

---

### 🔹 View Patient by ID

**GET /patient/{patient_id}**

**Path Parameter**
- `patient_id` (str) → Patient ID (e.g., P001)

**Response**
```json
{
  "name": "Asad Abbas",
  "city": "Ahmadpur East",
  "age": 21,
  "gender": "male",
  "height": 5.6,
  "weight": 47,
  "bmi": 33.06,
  "verdict": "Underweight"
}
```

**Error**
- 404 → Patient Not Found

---

### 🔹 Sort Patients

**GET /sort**

**Query Parameters**
- `sort_by` → height | weight | bmi  
- `order` → asc | desc (default: asc)

**Example**
```
/sort?sort_by=bmi&order=desc
```

---

### 🔹 Create Patient

**POST /create**

**Request Body**
```json
{
  "id": "P004",
  "name": "Ali Khan",
  "city": "Lahore",
  "age": 25,
  "gender": "male",
  "height": 5.8,
  "weight": 70
}
```

**Response**
```json
{
  "message": "Patient Created Successfully"
}
```

**Error**
- 400 → Patient already exists

---

### 🔹 Update Patient

**PUT /edit/{patient_id}**

Allows **partial update** of patient data.

**Request Body**
```json
{
  "weight": 75,
  "height": 5.9
}
```

**Response**
```json
{
  "message": "Patient Updated Successfully"
}
```

---

### 🔹 Delete Patient

**DELETE /delete/{patient_id}**

**Response**
```json
{
  "message": "Patient deleted successfully"
}
```

**Error**
- 404 → Patient Not Found

---

## ⚠️ Error Handling

| Status Code | Description |
|------------|------------|
| 400 | Bad Request |
| 404 | Patient Not Found |
| 422 | Validation Error |

---

## ▶️ How to Run the Project

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

### 📘 API Docs
- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

---

## 🌟 Features Implemented

- CRUD operations using JSON
- Computed BMI & health verdict
- Sorting with query parameters
- Input validation with Pydantic
- FastAPI auto-generated documentation

---

## 🚀 Future Improvements

- Replace JSON with SQLAlchemy + SQLite
- Add authentication (JWT)
- Add pagination & filtering
- Add logging & exception middleware

---

## 👨‍💻 Author

**Asad Abbas**  
FastAPI Patient Management System  

---

✅ Ideal project for learning **FastAPI CRUD + validation + computed fields without a database**.
