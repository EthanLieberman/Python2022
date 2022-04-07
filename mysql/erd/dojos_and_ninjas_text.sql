SELECT * FROM dojos;
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('viper dojo', NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('brack dojo', NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('liquid dojo', NOW(), NOW());
DELETE FROM dojos WHERE id > 0;

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('adam', 'bronze', 26, NOW(), NOW(), 12);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('jake', 'laser', 19, NOW(), NOW(), 12);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('steven', 'stone', 29, NOW(), NOW(), 12);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('sarah', 'jackobs', 28, NOW(), NOW(), 14);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('ashley', 'jones', 27, NOW(), NOW(), 14);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ('chris', 'durden', 20, NOW(), NOW(), 14);

SELECT * FROM ninjas WHERE dojo_id = 12;
SELECT * FROM ninjas WHERE dojo_id = 14;
SELECT name FROM dojos
JOIN ninjas ON dojos.id = dojo_id WHERE ninjas.id = 13;
