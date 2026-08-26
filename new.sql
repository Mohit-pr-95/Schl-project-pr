-- Active: 1787501700360@@127.0.0.1@3306@new_database
CREATE DATABASE new_database;

USE new_database;

CREATE TABLE doctors_info (
    ID VARCHAR(7) PRIMARY KEY,
    Names VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Experience INT NOT NULL
);

INSERT INTO doctors_info (ID, Names, Department, Experience)
VALUES
    ("DR9P1", 'Aarav Mehta', 'Cardiology', 12),
    ("DR9P2", 'Diya Sharma', 'Neurology', 8),
    ("DR9P3", 'Rohan Kapoor', 'Orthopedics', 15),
    ("DR9P4", 'Anaya Verma', 'Dermatology', 6),
    ("DR9P5", 'Vivaan Malhotra', 'Pediatrics', 10),
    ("DR9P6", 'Ishita Rao', 'Gynecology', 9),
    ("DR9P7", 'Kabir Sinha', 'Oncology', 18),
    ("DR9P8", 'Myra Joshi', 'Radiology', 7),
    ("DR9P9", 'Arjun Bhatia', 'Psychiatry', 11),
    ("DR9P10", 'Kiara Nair', 'Ophthalmology', 5),
    ("DR9P11", 'Aditya Iyer', 'Urology', 14),
    ("DR9P12", 'Sara Chawla', 'Endocrinology', 8),
    ("DR9P13", 'Reyansh Desai', 'Cardiology', 16),
    ("DR9P14", 'Tara Menon', 'Neurology', 13),
    ("DR9P15", 'Ayaan Khanna', 'Orthopedics', 9),
    ("DR9P16", 'Meera Saxena', 'Dermatology', 4),
    ("DR9P17", 'Atharv Kulkarni', 'Pediatrics', 12),
    ("DR9P18", 'Nisha Reddy', 'Gynecology', 10),
    ("DR9P19", 'Devansh Arora', 'Oncology', 17),
    ("DR9P20", 'Riya Dutta', 'Radiology', 6),
    ("DR9P21", 'Vihaan Oberoi', 'Psychiatry', 7),
    ("DR9P22", 'Avni Prasad', 'Ophthalmology', 11),
    ("DR9P23", 'Karan Bansal', 'Urology', 13),
    ("DR9P24", 'Sneha Pillai', 'Endocrinology', 9),
    ("DR9P25", 'Yash Thakur', 'Cardiology', 5),
    ("DR9P26", 'Aditi Roy', 'Neurology', 14),
    ("DR9P27", 'Manav Goyal', 'Orthopedics', 8),
    ("DR9P28", 'Simran Kaur', 'Dermatology', 16),
    ("DR9P29", 'Dhruv Jain', 'Pediatrics', 6),
    ("DR9P30", 'Pihu Agarwal', 'Gynecology', 12),
    ("DR9P31", 'Nakul Yadav', 'Oncology', 10),
    ("DR9P32", 'Ira Mukherjee', 'Radiology', 15),
    ("DR9P33", 'Samar Vohra', 'Psychiatry', 4),
    ("DR9P34", 'Anika Bose', 'Ophthalmology', 9),
    ("DR9P35", 'Rudra Shetty', 'Urology', 18),
    ("DR9P36", 'Mahi Fernandes', 'Endocrinology', 7),
    ("DR9P37", 'Kartik Sethi', 'Cardiology', 11),
    ("DR9P38", 'Lavanya Hegde', 'Neurology', 6),
    ("DR9P39", 'Neil Wadhwa', 'Orthopedics', 13),
    ("DR9P40", 'Aarohi Tiwari', 'Dermatology', 8),
    ("DR9P41", 'Shivam Puri', 'Pediatrics', 15),
    ("DR9P42", 'Tanvi Borkar', 'Gynecology', 5),
    ("DR9P43", 'Harsh Vardhan', 'Oncology', 12),
    ("DR9P44", 'Navya Krishnan', 'Radiology', 10),
    ("DR9P45", 'Siddharth Gill', 'Psychiatry', 16),
    ("DR9P46", 'Esha Rangan', 'Ophthalmology', 7),
    ("DR9P47", 'Moksh Patel', 'Urology', 9),
    ("DR9P48", 'Kavya Sood', 'Endocrinology', 14),
    ("DR9P49", 'Parth Srivastava', 'Cardiology', 6),
    ("DR9P50", 'Zoya Qureshi', 'Neurology', 11);

CREATE TABLE patient_info (
    ID VARCHAR(7) PRIMARY KEY,
    Name CHAR(20) NOT NULL,
    Age INT (3) NOT NULL,
    Gender CHAR(5) NOT NULL,
    B_Goup VARCHAR(5) NOT NULL,
    Address VARCHAR(30) NOT NULL
);

-- SELECT * FROM doctors_info WHERE `Department`="Neurology";

-- SELECT * FROM patients_info;

CREATE TABLE appointments (
    ID VARCHAR (7) PRIMARY KEY,
    P_Name CHAR (30) NOT NULL,
    Doctor CHAR (30) NOT NULL,
    Division CHAR (20) NOT NULL,
    Date DATE NOT NULL
);

SELECT Names from doctors_info WHERE `Department`="Gynecology";