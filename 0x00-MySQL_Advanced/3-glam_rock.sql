-- SQL script to list bands with Glam rock as their main style, ranked by longevity
SELECT band_name, 
       IFNULL((2022 - formed), 0) - IFNULL((2022 - split), 0) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;

