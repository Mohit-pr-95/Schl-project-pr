# Medicare Hospital Management System

This is a school project developed by **Mohit Singh(Python code writer)** and **Dev Chauhan(Database manager)**. It is a Command Line Interface (CLI) application written in Python that simulates a hospital management system. The application connects to a MySQL database to securely store, retrieve, and manage patient and doctor records.

---

## 📊 Current Progress & Implemented Features

### 1. Database Integration & Security
- Secure database connection with `mysql.connector` using environment variables managed by `python-dotenv`.
- Credentials remain protected and outside version control via `.env`.

### 2. Main Navigation Menu
The central navigation hub allows users to select from various hospital services:
- **1) Patient portal**
- **2) Doctor's portal**
- **3) Appointments** *(Upcoming)*
- **4) More services** *(Upcoming)*
- **5) Billing** *(Upcoming)*
- **6) Emergency information** *(Upcoming)*
- **7) About the hospital** *(Upcoming)*
- **8) Exit**

---

### 3. Patient Portal (`Patient's Portal`)
- **Patient Registration:**
  - Captures full patient profile: Name, Age, Gender, Blood Group, Address, and Phone Number.
  - Automatically generates a formatted unique Patient ID (e.g., `PT9U1`, `PT9U2`, etc.) based on existing records.
  - Formats phone numbers with country code prefix (`+91`).
  - Securely inserts records into the `patients_info` MySQL table.
- **View Patient Details:**
  - Search and look up patient details by entering their unique Patient ID (`PT9U..`).
  - Retrieves patient details from the database and renders them in a formatted tabular layout using `pandas.DataFrame.to_markdown()`.
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
Set up the required tables in your MySQL database:

```sql
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
    ID VARCHAR(10) PRIMARY KEY,
    Names VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Experience INT NOT NULL
);
```

### 4. Run the Application
Start the program by executing:
```bash
python main.py
```

---

## 🚀 How It Works
1. **Launch:** Running `main.py` opens the Medicare Hospital CLI welcome banner and displays the main menu.
2. **Interactive CLI Navigation:** Users input the numerical choice for their desired action with built-in input validation to prevent crashes.
3. **Database Interactions:**
   - Registrations perform parameterized `INSERT` SQL operations and commit changes.
   - Searches and lookups execute dynamic `SELECT` SQL queries and fetch records.
4. **Tabular Data Presentation:** Query results are converted to Pandas DataFrames and formatted using `to_markdown()` for readable output in the terminal.

---

## 🌟 Future Roadmap
- [ ] Implement Appointment Booking & Scheduling system.
- [ ] Develop Hospital Billing & Invoice generation module.
- [ ] Add Emergency Services and Hospital Contact/About sections.
- [ ] Add support for updating and deleting patient/doctor records.