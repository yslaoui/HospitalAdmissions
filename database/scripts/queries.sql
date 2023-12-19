-- Average billing amount per medication for all hospitals

SELECT 
    medical_conditions.medical_condition AS medical_condition, 
    AVG(billing_amount) AS average_billing 

FROM 
    admissions 
JOIN 
    medical_conditions ON admissions.medical_condition_id=medical_conditions.id


-- hospital with the highest amount of emergency admissions

SELECT
   hospitals.hospital,
   COUNT(*) AS emergencies
FROM
   admissions 
JOIN
   hospitals ON  hospitals.id = admissions.hospital_id
JOIN
   admission_types ON admissions.admission_type_id=admission_types.id
WHERE
   admission_types.admission_type='Emergency'
GROUP BY
   hospitals.hospital
ORDER BY
   COUNT(*) DESC
LIMIT 10;

-- Insurance providers with highest summed billing amount

SELECT
   insurances.insurance AS insurance_company,
   SUM(admissions.billing_amount) AS billings
FROM
   admissions
JOIN
   insurances ON admissions.insurance_id=insurances.id 


GROUP BY
   insurance_company


ORDER BY
   Billings DESC;


-- Most common medication prescribed for each type of medical condition

WITH prescription_counts AS
   (
       SELECT
           medical_conditions.medical_condition AS illness,
           medications.medication AS pills,
           COUNT(*) AS number_of_perscriptions
       FROM
           admissions
       JOIN
           medications ON admissions.medication_id=medications.id
       JOIN
           medical_conditions ON admissions.medical_condition_id=medical_conditions.id
       GROUP BY
           illness, pills 
   ), prescription_max AS
       (
           SELECT
               illness,
               MAX(number_of_perscriptions) AS maximum_prescriptions    
           FROM
               prescription_counts
           GROUP BY
               illness
       )
SELECT
   prescription_counts.illness,
   prescription_counts.pills,
   prescription_counts.number_of_perscriptions
FROM
   prescription_counts
JOIN
   prescription_max ON prescription_counts.illness=prescription_max.illness
   AND prescription_counts.number_of_perscriptions=prescription_max.maximum_prescriptions;


-- Doctors who admitted patients more than once 

SELECT
   doctors.doctor AS docs,
   COUNT(*) AS number_of_admissions
FROM
   admissions
JOIN
   doctors ON admissions.doctor_id=doctors.id
JOIN
   hospitals ON admissions.hospital_id=hospitals.id
GROUP BY
   docs
HAVING COUNT(*) > 1
ORDER BY number_of_admissions desc;






