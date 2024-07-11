-- Create stored procedure ComputeAverageScoreForUser
-- Computes and stores average score for a student
-- Takes 1 input parameter: user_id (users.id)

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END $$

DELIMITER ;
