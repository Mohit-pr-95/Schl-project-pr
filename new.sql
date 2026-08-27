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

CREATE TABLE departments (
    ID VARCHAR(5) PRIMARY KEY,
    Department_Name VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT NOT NULL
);

INSERT INTO departments (ID, Department_Name, Description)
VALUES
    ('DEP01', 'Cardiology', CONCAT(
        'Cardiology focuses on the heart and circulatory system.', CHAR(10),
        'It diagnoses and treats conditions such as heart disease and hypertension.', CHAR(10),
        'Cardiologists evaluate heart rhythm, blood flow, and cardiovascular risk.', CHAR(10),
        'Common services include ECGs, echocardiograms, and cardiac consultations.', CHAR(10),
        'The department also supports prevention through lifestyle and risk management.'
    )),
    ('DEP02', 'Neurology', CONCAT(
        'Neurology focuses on the brain, spinal cord, and peripheral nerves.', CHAR(10),
        'It treats disorders such as epilepsy, stroke, migraine, and Parkinson disease.', CHAR(10),
        'Neurologists assess movement, sensation, memory, coordination, and reflexes.', CHAR(10),
        'Diagnostic services may include neurological examinations and brain imaging.', CHAR(10),
        'The department provides both long-term care and treatment for urgent conditions.'
    )),
    ('DEP03', 'Orthopedics', CONCAT(
        'Orthopedics deals with the bones, joints, muscles, ligaments, and tendons.', CHAR(10),
        'The department treats fractures, arthritis, sports injuries, and spinal problems.', CHAR(10),
        'Orthopedic specialists use examination and imaging to identify musculoskeletal injuries.', CHAR(10),
        'Treatment can include medicine, physical therapy, injections, or surgery.', CHAR(10),
        'Care aims to restore movement, reduce pain, and improve physical function.'
    )),
    ('DEP04', 'Dermatology', CONCAT(
        'Dermatology focuses on the skin, hair, nails, and related disorders.', CHAR(10),
        'It manages conditions such as acne, eczema, psoriasis, infections, and skin cancer.', CHAR(10),
        'Dermatologists examine changes in the skin and identify possible health concerns.', CHAR(10),
        'Services may include biopsies, allergy evaluation, and minor procedures.', CHAR(10),
        'The department also promotes skin protection, hygiene, and preventive care.'
    )),
    ('DEP05', 'Pediatrics', CONCAT(
        'Pediatrics provides medical care for infants, children, and adolescents.', CHAR(10),
        'Pediatricians monitor growth, development, nutrition, and overall wellbeing.', CHAR(10),
        'The department treats childhood illnesses, infections, injuries, and allergies.', CHAR(10),
        'Routine services include vaccinations, health screenings, and developmental checks.', CHAR(10),
        'Care is designed to support healthy physical, emotional, and social development.'
    )),
    ('DEP06', 'Gynecology', CONCAT(
        'Gynecology focuses on the reproductive health of women and girls.', CHAR(10),
        'It provides care for menstruation, fertility, pregnancy-related concerns, and menopause.', CHAR(10),
        'Gynecologists diagnose and treat infections, hormonal conditions, and pelvic disorders.', CHAR(10),
        'Services may include examinations, screening, counseling, and minor procedures.', CHAR(10),
        'The department supports preventive care and informed reproductive health decisions.'
    )),
    ('DEP07', 'Oncology', CONCAT(
        'Oncology focuses on the prevention, diagnosis, and treatment of cancer.', CHAR(10),
        'Oncologists assess tumors and develop treatment plans based on each patient''s needs.', CHAR(10),
        'Treatment may involve surgery, chemotherapy, radiation, immunotherapy, or targeted therapy.', CHAR(10),
        'The department coordinates care with pathology, radiology, and other specialties.', CHAR(10),
        'It also provides monitoring, symptom management, and supportive care during treatment.'
    )),
    ('DEP08', 'Radiology', CONCAT(
        'Radiology uses medical imaging to examine structures and processes inside the body.', CHAR(10),
        'Radiologists interpret X-rays, ultrasound scans, CT scans, and MRI examinations.', CHAR(10),
        'Imaging helps doctors diagnose injuries, infections, tumors, and other conditions.', CHAR(10),
        'Some radiology services use image guidance for minimally invasive procedures.', CHAR(10),
        'The department emphasizes accurate interpretation and appropriate radiation safety.'
    )),
    ('DEP09', 'Psychiatry', CONCAT(
        'Psychiatry focuses on mental health, emotions, behavior, and psychological wellbeing.', CHAR(10),
        'Psychiatrists evaluate and treat conditions such as depression, anxiety, and addiction.', CHAR(10),
        'Care may combine medication, psychotherapy, behavioral strategies, and counseling.', CHAR(10),
        'The department provides assessment for both ongoing and urgent mental health needs.', CHAR(10),
        'Treatment plans respect patient goals, safety, privacy, and individual circumstances.'
    )),
    ('DEP10', 'Ophthalmology', CONCAT(
        'Ophthalmology focuses on the eyes and the visual system.', CHAR(10),
        'Ophthalmologists diagnose and treat vision problems, eye diseases, and eye injuries.', CHAR(10),
        'Common conditions include cataracts, glaucoma, retinal disorders, and infections.', CHAR(10),
        'Services include vision testing, eye examinations, medication, and surgical care.', CHAR(10),
        'Regular assessment helps preserve sight and identify problems at an early stage.'
    )),
    ('DEP11', 'Urology', CONCAT(
        'Urology focuses on the urinary system and the male reproductive system.', CHAR(10),
        'Urologists treat kidney stones, urinary infections, prostate conditions, and cancers.', CHAR(10),
        'The department evaluates problems affecting the kidneys, bladder, and urinary tract.', CHAR(10),
        'Treatment may include medication, endoscopic procedures, or reconstructive surgery.', CHAR(10),
        'Care combines symptom relief, disease management, and protection of organ function.'
    )),
    ('DEP12', 'Endocrinology', CONCAT(
        'Endocrinology focuses on hormones and the glands that produce them.', CHAR(10),
        'It treats diabetes, thyroid disorders, osteoporosis, and other hormonal conditions.', CHAR(10),
        'Endocrinologists assess how hormonal changes affect metabolism and body functions.', CHAR(10),
        'Care may include laboratory testing, medication, nutrition advice, and monitoring.', CHAR(10),
        'The department helps patients manage chronic conditions and prevent complications.'
    ));

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