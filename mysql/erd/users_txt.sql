SELECT * FROM users;
INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ('jess', 'swift', 'j@s.com',NOW(), NOW());

SELECT email FROM users WHERE users.id = 1;
SELECT * FROM users WHERE id = 3;

UPDATE users SET last_name = 'pancakes' WHERE id = 3;
DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name;
SELECT * FROM users ORDER BY first_name DESC;