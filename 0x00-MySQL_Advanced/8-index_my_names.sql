-- SQL script to create an index idx_name_first on the first letter of names table

-- Drop index if exists (in case script needs to be rerun)
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create index on the first letter of the name column
CREATE INDEX idx_name_first ON names (LEFT(name, 1));

-- Show index information after creation
SHOW INDEX FROM names;

