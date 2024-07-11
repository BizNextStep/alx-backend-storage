-- SQL script to create a function SafeDiv that safely divides two integers

-- Drop function if exists (in case script needs to be rerun)
DROP FUNCTION IF EXISTS SafeDiv;

-- Create function SafeDiv
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;
    
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    
    RETURN result;
END //

DELIMITER ;

