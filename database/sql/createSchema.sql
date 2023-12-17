
CREATE TABLE IF NOT EXISTS genders (id INT AUTO_INCREMENT, gender VARCHAR(50),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS blood_types (id INT AUTO_INCREMENT, blood_type VARCHAR(5),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS hospitals (id INT AUTO_INCREMENT, hospital VARCHAR(50),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS doctors (id INT AUTO_INCREMENT, doctor VARCHAR(50),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS medications (id INT AUTO_INCREMENT, medication VARCHAR(50),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS insurances (id INT AUTO_INCREMENT, insurance VARCHAR(50),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS admission_types (id INT AUTO_INCREMENT, admission_type VARCHAR(50),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS test_results (id INT AUTO_INCREMENT, test_result VARCHAR(50),PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS medical_conditions (id INT AUTO_INCREMENT, medical_condition VARCHAR(50),PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    gender_id INT,
    blood_type_id INT,
    FOREIGN KEY (gender_id) REFERENCES genders (id) ON DELETE CASCADE,
    FOREIGN KEY (blood_type_id) REFERENCES blood_types (id) ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS admissions (
   id INT PRIMARY KEY AUTO_INCREMENT,
   date_of_admission DATETIME,
   billing_amount DECIMAL(10, 10),
   discharge_date DATETIME,   
   hospital_id INT,
   doctor_id INT,
   medication_id INT,
   insurance_id INT,
   admission_type_id INT,
   test_result_id INT,
   medical_condition_id INT,
   FOREIGN KEY (hospital_id) REFERENCES hospitals (id) ON DELETE CASCADE,
   FOREIGN KEY (doctor_id) REFERENCES doctors (id) ON DELETE CASCADE,
   FOREIGN KEY (medication_id) REFERENCES medications (id) ON DELETE CASCADE,
   FOREIGN KEY (insurance_id) REFERENCES insurances (id) ON DELETE CASCADE,
   FOREIGN KEY (admission_type_id) REFERENCES admission_types (id) ON DELETE CASCADE,
   FOREIGN KEY (test_result_id) REFERENCES test_results (id) ON DELETE CASCADE,
   FOREIGN KEY (medical_condition_id) REFERENCES medical_conditions (id) ON DELETE CASCADE
);

