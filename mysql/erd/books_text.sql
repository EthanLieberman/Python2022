INSERT INTO authors (name, created_at, updated_at)
VALUES ('Jane Austen', NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at)
VALUES ('Emily Dickerson', NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at)
VALUES ('Fyodor Dostoevsky', NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at)
VALUES ('William Shakespeare', NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at)
VALUES ('Lau Tzu', NOW(), NOW());


SELECT * FROM authors;

INSERT INTO books (book_name, num_of_pages, created_at, updated_at)
VALUES ('C Sharp', 500, NOW(), NOW());
INSERT INTO books (book_name, num_of_pages, created_at, updated_at)
VALUES ('Java', 356, NOW(), NOW());
INSERT INTO books (book_name, num_of_pages, created_at, updated_at)
VALUES ('Python', 550, NOW(), NOW());
INSERT INTO books (book_name, num_of_pages, created_at, updated_at)
VALUES ('PHP', 207, NOW(), NOW());
INSERT INTO books (book_name, num_of_pages, created_at, updated_at)
VALUES ('Ruby', 600, NOW(), NOW());

SELECT * FROM books;

UPDATE books SET book_name = 'C#' WHERE id = 1;

UPDATE authors SET name = 'Bill' WHERE id = 4;


INSERT INTO favorites (author_id, book_id)
VALUES (1, 1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4),(4,5);

SELECT * FROM favorites;

SELECT name FROM authors JOIN favorites ON authors.id = favorites.author_id WHERE book_id = 3;

SELECT * FROM authors JOIN favorites ON authors.id = favorites.author_id JOIN books ON favorites.book_id = books.id;
