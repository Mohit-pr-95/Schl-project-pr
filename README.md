# Medicare Hospital Management System

This is a school project developed by **Mohit Singh (Python code writer)** and **Dev Chauhan (Database manager)**. It is a Command Line Interface (CLI) application written in Python that simulates a hospital management system. The application connects to a MySQL database to securely store, retrieve, and manage patient, doctor, appointment, and department records.

---

## 📊 Current Progress & Implemented Features

### 1. Database Integration & Robust Error Handling
- Secure database connection with `mysql.connector` using environment variables managed by `python-dotenv`.
- Credentials remain protected and outside version control via `.env`.
- Connection and query failures are wrapped with comprehensive `try...except...finally` blocks to ensure clean error messages and automatic connection cleanup.

### 2. Main Navigation Menu
The central navigation hub allows users to select from various hospital services:
- **1) Patient portal**
- **2) Doctor's portal**
- **3) Appointments**
- **4) More services (Hospital services)**
- **5) Billing** *(Upcoming)*
- **6) Emergency information** *(Upcoming)*
- **7) About the hospital** *(Upcoming)*
- **8) Exit**

---

### 3. Patient Portal (`Patient's Portal`)
- **Patient Registration:**
  - Captures full patient profile: Name, Age, Gender, Blood Group, Address, and Phone Number.
  - Automatically generates a formatted unique Patient ID (e.g., `PT9U1`, `PT9U2`, etc.) based on existing records.
  - Formats phone numbers with country code prefix (`+91 `).
  - Securely inserts records into the `patients_info` MySQL table.
- **View Patient Details:**
  - Validates ID prefix (`PT9U`) before searching the database.
  - Retrieves patient details and renders them in a formatted tabular layout using `pandas.DataFrame.to_markdown()`.
  - Includes validation and graceful notification if the ID is not found.

---

### 4. Doctor's Portal (`Doctor's Portal`)
- **View All Doctors:**
  - Queries `doctors_info` table to retrieve all staff doctors.
  - Displays doctor IDs, names, specializations, and years of experience in a clean markdown table.
- **Search Doctors by Department:**
  - Interactive selection menu supporting **12 clinical departments**:
    1. Cardiology
    2. Dermatology
    3. Endocrinology
    4. Gynecology
    5. Neurology
    6. Oncology
    7. Ophthalmology
    8. Orthopedics
    9. Pediatrics
    10. Psychiatry
    11. Radiology
    12. Urology
  - Dynamically filters and displays specialists matching the selected department.

---

### 5. Appointments Module (`Appointments`)
- **Book an Appointment:**
  - Collects patient's name, age, gender, and selected medical department (from 12 divisions).
  - Automatically assigns a doctor randomly from available doctors in that department using Python's `random` module.
  - Generates a unique appointment ID (e.g., `AP9U1`, `AP9U2`, etc.).
  - Saves the record into the `appointments` MySQL table with current date (`dt.date.today()`).
  - Displays immediate booking confirmation in a formatted Markdown table.
- **View Appointment Details:**
  - Allows patients/staff to query appointment records using their unique Appointment ID (`AP9U..`).
  - Fetches and displays patient name, appointed doctor, medical division, and appointment date in a neat table.
  - Validates ID format and alerts if the appointment ID does not exist.
- **Cancel Appointment:**
  - Allows cancellation of existing appointments via Appointment ID (`AP9U..`).
  - Validates existence, executes a SQL `DELETE` query, commits the change to the database, and confirms cancellation.

---

### 6. Hospital Services (`Hospital services`)
- **Departments Explorer:**
  - **View All Departments:** Displays a numbered master list of all 12 hospital departments.
  - **Detailed Department Info:**
    - Queries the `departments` table to show department ID (`DEP01` - `DEP12`), department name, and an in-depth clinical description.
    - Dynamically computes and displays the total number of doctors currently serving in that department.
    - Displays a live roster of available doctors in that department with their Doctor IDs, Names, and Experience (in years).
- **Upcoming Services:**
  - Menu placeholders prepared for **Laboratories**, **Ambulance**, and **Pharmacy** services.

---

## ⚙️ Setup Instructions

### Prerequisites
- **Python 3.x**
- **MySQL Server** installed and running

### 1. Install Dependencies
Install all necessary Python packages:
```bash
pip install mysql-connector-python pandas python-dotenv tabulate
```
*(Note: `tabulate` is required by Pandas to output markdown-formatted tables.)*

### 2. Configure Environment Variables
Create a `.env` file in the root of the project directory (ensure this file is ignored by Git):
```env
Database_host = localhost
Database_user = root
Database_pass = your_database_password_here
Database_name = your_database_name
```

### 3. Database Schema Setup
Set up the required tables and data in your MySQL database (see `new.sql`):

```sql
CREATE DATABASE IF NOT EXISTS new_database;
USE new_database;

CREATE TABLE patients_info (
    ID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    B_goup VARCHAR(10) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL
);

CREATE TABLE doctors_info (
    ID VARCHAR(7) PRIMARY KEY,
    Names VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Experience INT NOT NULL
);

CREATE TABLE appointments (
    ID VARCHAR(7) PRIMARY KEY,
    P_Name CHAR(30) NOT NULL,
    Doctor CHAR(30) NOT NULL,
    Division CHAR(20) NOT NULL,
    Date DATE NOT NULL
);

CREATE TABLE departments (
    ID VARCHAR(5) PRIMARY KEY,
    Department_Name VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT NOT NULL
);
```

### 4. Run the Application
Start the program by executing:
```bash
python main.py
```

---

## 🚀 How It Works
1. **Launch:** Running `main.py` establishes a connection to MySQL, opens the Medicare Hospital CLI welcome banner, and displays the main menu.
2. **Interactive CLI Navigation:** Users input numerical choices with built-in validation to prevent application crashes.
3. **Database Operations:**
   - **Insertions:** Patient registrations and appointment bookings execute parameterized `INSERT` SQL queries and commit changes.
   - **Retrieval:** Details for patients, doctors, appointments, and departments are retrieved using dynamic and parameterized `SELECT` SQL queries.
   - **Deletions:** Appointment cancellations execute parameterized `DELETE` SQL queries.
4. **Tabular Presentation:** Query results and confirmations are converted into Pandas DataFrames and formatted using `to_markdown()` for clean terminal display.

---

## 🌟 Future Roadmap
- [x] Implement Patient Registration & Profile View.
- [x] Implement Doctor Directory & Department Filter.
- [x] Implement Full Appointment Lifecycle (Book, View, Cancel).
- [x] Implement Hospital Departments Overview & Detailed Doctor Rosters.
- [ ] Implement Laboratories, Ambulance, and Pharmacy services.
- [ ] Develop Hospital Billing & Invoice generation module.
- [ ] Add Emergency Services and Hospital Contact/About sections.
- [ ] Add support for updating existing patient/doctor records.