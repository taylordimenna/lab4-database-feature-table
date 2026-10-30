-- Query 2: Count varients per tissue course site per tumor stage.
-- Expected grain = one row per tissue and stage
-- Expected row count = The number of distinct tissue source site and tumor stage. Should be less than 566.

SELECT
    s.tissue_source_site,
    p.stage,
    COUNT(DISTINCT p.patient_id) AS patient_count

FROM patients p

LEFT JOIN samples s
    ON s.patient_id = p.patient_id

GROUP BY
    s.tissue_source_site,
    p.stage

ORDER BY
    s.tissue_source_site,
    p.stage;

-- Output row count = 142
-- Each row represents a distinct tissue/stage combination. There are 142 total, hence the 142 rows.
