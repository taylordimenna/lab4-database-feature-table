# Schema Write-Up For Task 1
The tables are: ```genes```, ```mutations```, ```patients```, and ```samples```.

## ```genes``` Table
### Rows
There are 17,756 rows in this table.

### Columns
For the ```genes``` table, the columns are: ```gene_symbol```, ```entrez_gene_id```, and ```chromosome```.
- ```gene_symbol``` is the symbol of the gene.
- ```entrez_gene_id``` is the Entrez identifer that is associated to the gene.
- ```chromosome``` is the recorded chromosome.

### Primary Key
```gene_symbol```

### Foreign Keys
None

### Grain
Each row represents one gene.

## ```mutations``` Table
### Rows
There are 200,789 rows in this table.

### Columns
For the ```mutations``` table, the columns are: ```mutation_id```, ```sample_id```, ```gene_symbol```, ```variant_classification```, ```variant_type```, ```protein_change```, ```chromosome```, ```start_pos```, ```end_pos```, ```t_ref_count```, and ```t_alt_count```.
- ```mutation_id``` is the identifier for a mutation record.
- ```sample_id``` is the sample associated with the mutation.
- ```gene_symbol``` is the gene associated with the mutation.
- ```variant_classification``` is the classification of the varient. An example of this would be if it was classified as a missense mutation (```Missense_Mutation```).
- ```variant_type```  is the type of varient.
- ```protein_change``` is the recorded protein level change. This may not be available for all of the rows.
- ```chromosome``` is the chromosome associated with the record.
- ```start_pos``` is the start position of the genome.
- ```end_pos``` is the end position of the genome.
- ```t_ref_count``` is the recorded number of reads that support the reference allele.
- ```t_alt_count``` is the recorded number of reads that support the alternate allele.

### Primary Key
```mutation_id```

### Foreign Keys
```mutations.sample_id``` must correspond to ```samples.sample_id```.
```mutations.gene_symbol``` must correspond to ```genes.gene_symbol```.

### Grain
Each row represents one mutation that is associated with a sample and a gene. 

## ```patients``` Table
### Rows
There are 566 rows in this table.

### Columns
For the ```patients``` table, the columns are: ```patient_id```, ```sex```, ```age_at_diagnosis```, ```stage```, ```vital_status```, and ```followup_months```.
- ```patient_id``` is the identifier for the patient.
- ```sex``` is the recorded sex.
- ```age_at_diagnosis``` is the patient's age at diagnosis.
- ```stage``` is the recorded cancer stage.
- ```vital_status``` is the recorded vital status, so either living or deceased.
- ```followup_months``` is the duration between follow-ups.

### Primary Key
```patient_id```

### Foreign Keys
None

### Grain
Each row represents one patient and their recorded values.

## ```samples``` Table
### Rows
There are 566 rows in this table.

### Columns
For the ```samples``` table, the columns are: ```sample_id```, ```patient_id```, ```tissue_source_site```, ```tmb_nonsynonyous```, ```aneuploidy_score```, and ```msi_mantis_score```.
- ```sample_id``` is the identifier for the sample.
- ```patient_id``` is the patient associated with the sample.
- ```tissue_source_site``` is the site where the tissue was sourced from.
- ```tmb_nonsynonyous``` is the recorded tumor mutation burden measure (TMB). This is the total number of mutations found in cancer cells.
- ```aneuploidy_score``` is the recorded aneuploidy score.This is the a measurement that quantifies the total number of chromosome gains/losses in a tumor.
- ```msi_mantis_score``` is the recorded MSI MANTIS score. This is the value used to detect microsatellite instability (MSI) in cancer samples used by next gen sequencing data (NGS).

### Primary Key
```sample_id```.

### Foreign Keys
```samples.patient_id``` must correspond to ```patients.patient_id```.

### Grain
Each row represents one sample and its associated measurements. Each row is linked to a patient.


- Describe how the tables relate (one-to-many, one-to-one) in your own words, or with a simple diagram, based on what you checked in the database, not guessed from the column names
## Relatedness of Each Table
