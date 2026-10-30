# AI Usage within ```query_1.sql```
## Model used
ChatGPT (GPT-5.6 Luna)

## Error
I was unsure whether my written SQL queries had fullfilled the requirement of excluding the silent mutations. I was unsure of whether I needed to explicitly list the types of mutations to include.

## What this error means
In the SQL correctness portion of the directions, it listed how all the silent protein-altering mutations were to be exluded from the final result. I had written an existing code, but wasn't sure if it would return the correct result and exclude the silent mutations.

## Existing script
Before using AI to help me correct this mistake, I had:

    LEFT JOIN mutations m
    ON m.sample_id = s.sample_id
    AND UPPER(TRIM(m.gene_symbol)) = pg.gene_symbol
    AND UPPER(TRIM(m.variant_classification)) <> 'SILENT'


## Prompt
The prompt I typed into the LLM to allow me to correct this was:
    
    "I need help refining my SQL query for a lab. The directions say to count protein-altering mutations per patient and per gene (TP53, KRAS, EGFR, STK11, and KEAP1), but to also exclude the silent mutations. I currently have:

    LEFT JOIN mutations m
    ON m.sample_id = s.sample_id
    AND UPPER(TRIM(m.gene_symbol)) = pg.gene_symbol
    AND UPPER(TRIM(m.variant_classification)) <> 'SILENT'
    
    Is this enough or should I state the specific mutation classifications to include? These are Missense_Mutation, silent, nonsense_mutation, splice_site, frame_shift_del, frame_shift_ins, in_frame_del, in_frame_ins, translation_start_site, and nonstop_mutation."

## Output
The output given to me by the LLM was:

    "Your current approach is correct, and you do not necessarily need to list every mutation classification individually. However, there is one important distinction to consider.
    
    Your current query

    LEFT JOIN mutations m
    ON m.sample_id = s.sample_id
    AND UPPER(TRIM(m.gene_symbol)) = pg.gene_symbol
    AND UPPER(TRIM(m.variant_classification)) <> 'SILENT'

    This condition:
    AND UPPER(TRIM(m.variant_classification)) <> 'SILENT'

    excludes mutations classified as Silent while retaining every other mutation classification.

    The assignment specifically asks for protein-altering mutations. That may be a narrower category than simply counting everything that isn't silent.

    A more transparent approach is to explicitly list the nine classifications you intended to count:

    AND m.variant_classification IN (
        'Missense_Mutation',
        'Nonsense_Mutation',
        'Splice_Site',
        'Frame_Shift_Del',
        'Frame_Shift_Ins',
        'In_Frame_Del',
        'In_Frame_Ins',
        'Translation_Start_Site',
        'Nonstop_Mutation'
    )

    This approach has two advantages:
    - It explicitly identifies which mutation classifications are included in your protein-altering mutation counts.
    - It prevents other unexpected or non-protein-altering classifications from being counted simply because they aren't labeled Silent.

    One additional consideration: Because you're using a LEFT JOIN, keeping the mutation filter in the ON clause (rather than moving it to WHERE) is important. This preserves patients who have zero qualifying mutations.

    Bottom line: Your original query is logically correct for excluding silent mutations. The assignment asks you to count protein-altering mutations and exclude Silent. Explicitly listing the qualifying classifications makes your SQL more precise and makes it easier for your professor to understand exactly what your counts represent."

## Verifying the fix
To verify the fix I made the change to my script and ran it to see if the results would be similar or exactly the same. I was able to get the same amount of rows returned (2830), so I decided to keep the fix. Even if this change is unnecessary, I decided to keep it just to be safe.