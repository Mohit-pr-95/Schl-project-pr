# Medicare Hospital Management System

This is a school project developed by **Mohit Singh** and **Dev Chauhan**. It is a Command Line Interface (CLI) application written in Python that simulates a hospital management system. The application uses a MySQL database to store and manage records.

## 📊 How Much Work is Done Till Now
- **Database Integration:** Successfully connected the Python script to a local MySQL server using `mysql.connector` and `.env` for secure credential management.
- **Main Menu Structure:** The primary navigation menu is implemented, displaying options for:
  - Patient Portal
  - Doctor's Portal
  - Appointments
  - More Services
  - Billing
  - Emergency Information
  - About the Hospital
- **Patient Portal:** Menu is set up with options to Register, View, and Search patients.
  - **Patient Registration:** Fully functional. It captures patient details (Name, Age, Phone, Gender, Address, Blood Group) and securely inserts the record into the MySQL database (`Patient_name` table).
- **Doctor's Portal:** View Doctors option working and others are in progress.

## ⚙️ Setup Instructions
To run this project on your local machine, follow these steps:

### Prerequisites
- Python 3.x installed
- MySQL Server installed and running

### 1. Install Dependencies
Install the required Python modules using pip:
```bash
pip install mysql-connector-python pandas python-dotenv
```
```bash
pip install tabulate
```
### 2. Configure Database Environment Variables
For security reasons, database credentials are not hardcoded. Create a file named `.env` in the root directory of the project and add your database configuration:

```env
Database_host = localhost
Database_user = root
Database_pass = your_database_password_here
Database_name = your_database_name
```
*(Make sure not to commit your real `.env` file to version control. It is already included in `.gitignore`)*

### 3. Database Table Setup
You will need to create the corresponding table in your MySQL database for the code to execute successfully. Ensure your database contains a table named `Patient_name` with columns configured to accept:
- `ID` (Varchar/Primary Key)
- `Name` (String/Varchar)
- `Age` (Int)
- `Gender` (String/Varchar)
- `B_group` (String/Varchar)
- `Address` (String/Varchar)
- `Phone` (String/Varchar)

### 4. Run the Application
Execute the main script from your terminal:
```bash
python main.py
```

## 🚀 How It Works
1. **Launch:** Upon running the program, the user is greeted with the "Medicare Hospital" banner and the main menu options.
2. **Navigation:** Users select a service by entering the corresponding number (e.g., `1` for Patient portal). Error handling ensures invalid inputs do not crash the program.
3. **Data Entry & Management:** When entering data (like registering a new patient), the program will prompt for required details, execute an `INSERT INTO` SQL query, and commit the changes to your local MySQL database.
4. **Portals:** The logic is branching, meaning each portal (Patient, Doctor, etc.) will have its own sub-menus for specialized tasks.

## 🌟 Future Features to Implement
- Complete the Doctor's Portal logic.
- Add features to View and Search existing patients.
- Appointment scheduling module.
- Billing and emergency information systems.