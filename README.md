# Lab 4 Database Feature Table
Contains my work for Lab 4: Database Feature Table

## Setup
### 1. Clone the repository to your local computer.
Run the following command:

    git clone https://github.com/taylordimenna/lab4-database-feature-table.git

### 2. Move into repository
Run the following command:

    cd lab4-database-feature-table

You are now inside the ```lab4-database-feature-table``` directory.

### 3. Install Pandas
Run the following command:

    python -m pip install pandas

### 4. Rebuild Final Feature Table
To rebuild ```patient_feature_table.tsv```, run the following command:

    python feature_table/build_feature_table.py

#### Usage Notes of ```build_feature_table.py```
What the script expects:
- The original dataset ```cohort.db``` to be located within the ```data``` directory.
- The SQL query files to be located within the ```sql_queries directory.
- Both python and pandas to be installed.


What the script outputs:
- The final feature table ```patient_feature_table.tsv``` within the ```feature_table``` directory.

This table contains all 566 patients within ```cohort.db```.

## Missing Data Handling
There were some data that was missing from the source database. These missing values were either preserved (NA) or filled in (with 0), depending on the data type. NA indicates that there was no information recorded whereas 0 indicates that no mutation was recorded. Either way, no patient data was removed.
- Sex: There were 52 patients that had missing sex values. These were retained as NA.
- Age: There were 71 patients that had missing age values. These were retained as NA.
- Tumor stage: There were 54 patients that had missing stage values. These were retained as NA.
- Gene mutation counts: Any patient that had missing gene counts were filled with zero. A zero indicates that there was no mutation found in that gene for the patient, whereas a numerical value means that there is a mutation within that gene.

Before and after these changes, there were 566 rows within the created table, showing how no patients were dropped on accident.

## Repository Contents
The ```data``` folder contains the starting data, inspection script, and schema documentation.
- ```cohort.db``` is the original data containing the 566 patient records.
- ```inspect_db.py``` is the script used to easily inspect the database.
- ```schema_understanding.md```is the documentation for task 1 explaining each table, the grain, and how they relate to each other.

The ```feature_table``` folder contains all the files related to the feature table.
- ```build_feature_table.py``` is the script used to build ```patient_feature_table.tsv```.
- ```data_dictionary.csv``` is the data dictionary describing what each column within ```patient_feature_table.tsv``` represents.
- ```patient_feature_table.tsv``` is the final table containing the 566 patient records.

The ```sql_queries``` folder contains the SQL queries and script for running them.
- ```query_1.sql```, ```query_2.sql```, and ```query_3.sql``` are the SQL queries.
    - ```query_1.sql``` counts the protein-altering mutations for each patient and gene.
    - ```query_2.sql``` counts varients per tissue course site per tumor stage.
    - ```query_3.sql``` gets patient level clinical and sample features.
- ```run_query.py``` is the script used to run the SQL queries.

```.gitignore``` contains the files that should not be committed to the repository.

```AI_USAGE.md``` contains information about any AI tools used to help complete this lab.

```README.md``` contains the repository contents and all the instructions needed to run it.