-- Creates an index idx_name_first on the names table
-- The index is on the first letter of the name column
-- Only the first letter of the name is indexed

CREATE INDEX idx_name_first
ON names (name(1));
