CREATE DATABASE medical_records;

USE medical_records;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    diagnosis VARCHAR(255),
    contact VARCHAR(50)
);

INSERT INTO patients VALUES
(1, 'John Doe', 45, 'Hypertension', '1234567890'),
(2, 'Jane Smith', 32, 'Diabetes', '9876543210');
INSERT INTO patients VALUES(4, 'guru', 18, 'cancer', '98760982341');
select * from patients;