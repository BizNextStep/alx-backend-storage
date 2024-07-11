SELECT origin, COUNT(*) AS total_fans
FROM (
  SELECT origin, COUNT(*) AS nb_fans
  FROM metal_bands
  GROUP BY origin
) AS subquery
GROUP BY origin
ORDER BY total_fans DESC;
