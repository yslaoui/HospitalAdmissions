# TODO create an ID for every variale that represents an entity
import pandas as pd




file_path = '/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/midterm/work/database/csv/healthcare_dataset.csv'

def factorize_column_and_save_csv(df, column_name):
    """
    Factorizes a specified column in the DataFrame, creates a new DataFrame with unique IDs,
    and exports it to a CSV file with the name derived from the column name.

    Args:
    df (pandas.DataFrame): The original DataFrame.
    column_name (str): The name of the column to be factorized.
    """
    # Create a new ID column by factorizing the specified column
    id_column = column_name + 'ID'
    df[id_column] = pd.factorize(df[column_name])[0] + 1

    # Create a new DataFrame with unique IDs and the original column
    unique_df = df[[id_column, column_name]].drop_duplicates().reset_index(drop=True)

    # Export the new DataFrame to CSV
    output_path = f'/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/midterm/work/database/csv/lookupTables/{column_name}.csv'
    unique_df.to_csv(output_path, index=False)

    return unique_df


# Read the CSV data into a DataFrame
df = pd.read_csv(file_path)

print(df.head())
# Now 'dataframe' holds the data from the CSV file and you can work with it

# =======================================
# SECTION: Creating date of birth
# =======================================

# Convert 'Date of Admission' to datetime
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
# Calculate 'Date of Birth' by subtracting the age from the year of 'Date of Admission'
df['Date of Birth'] = df.apply(lambda row: row['Date of Admission'] - pd.DateOffset(years=row['Age']), axis=1)

print(df['Date of Birth'])

# =======================================
# SECTION: Creating unique IDs
# =======================================

# -- Subsection: Patient Table --

# Create a 'PatientID' by concatenating 'Name', 'Gender', and 'Blood Type'
df['PatientConcatenate'] = df['Name'] + '_' + df['Gender'] + '_' + df['Blood Type'] + '_' + df['Date of Birth'].astype(str)
# Convert this 'PatientID' into a sequence of incrementing integers
# Each unique string combination will be assigned a unique integer
df['PatientID'] = pd.factorize(df['PatientConcatenate'])[0] + 1

# -- Subsection: Admission Table --

# Create a unique 'AdmissionID' for each row assuming each row is a unique admission
df['AdmissionID'] = range(1, len(df) + 1)


# =======================================
# SECTION: Lookup tables
# =======================================


lookupTables = ['Medical Condition', 'Doctor', 
                'Medication', 'Admission Type', 
                'Test Results', 'Insurance Provider',
                'Hospital', 'Gender', 'Blood Type']

for entity in lookupTables:
    factorize_column_and_save_csv(df, entity)

# =======================================
# SECTION: Rearranging and saving table
# =======================================

# Rearrange columns
cols = ['PatientID'] + ['AdmissionID'] + ['Date of Birth']  + [col for col in df if (col != 'PatientID' and col != 'AdmissionID' and col != 'Date of Birth')  ]
df = df[cols]


# Save the DataFrame with the new 'PatientID' and 'AdmissionID' columns to a new CSV file
output_csv_file_path = '/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/midterm/work/database/csv/healthcare_dataset_with_pks.csv'  # Replace with the desired output file path
df.to_csv(output_csv_file_path, index=False)


