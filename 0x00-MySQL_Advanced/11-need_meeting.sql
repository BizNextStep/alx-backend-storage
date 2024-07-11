-- SQL script to create a view need_meeting that lists students needing a meeting

-- Drop view if exists (in case script needs to be rerun)
DROP VIEW IF EXISTS need_meeting;

-- Create view need_meeting
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));

