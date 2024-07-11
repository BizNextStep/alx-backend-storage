-- SQL script to create a stored procedure ComputeAverageScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE num_corrections INT;
    DECLARE avg_score FLOAT;
    
    -- Calculate total score and number of corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, num_corrections
    FROM corrections
    WHERE user_id = user_id;
    
    -- Compute average score
    IF num_corrections > 0 THEN
        SET avg_score = total_score / num_corrections;
    ELSE
        SET avg_score = 0; -- default value if no corrections found
    END IF;
    
    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
    
END //

DELIMITER ;

