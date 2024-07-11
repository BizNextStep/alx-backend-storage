-- SQL script to create an index idx_name_first_score on the first letter of name and score

-- Drop index if exists (in case script needs to be rerun)
DROP INDEX IF EXISTS idx_name_first_score ON names;

-- Create index on the first letter of the name column and score
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);

-- Show index information after creation
SHOW INDEX FROM names;

