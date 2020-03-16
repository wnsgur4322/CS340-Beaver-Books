-- Name: Junhyeok (Derek) Jeong and Joelle Perez
-- Date: March 14, 2020
-- Class: CS340-400
-- Program: Project Step 7 (DML)

--Variables are denoted by :

-- ABOUT & INDEX PAGES: no queries

-- -- -- -- -- --

-- ADMIN PAGE: 

-- view books
SELECT books.isbn, books.title, books.price, authors.first_name, authors.last_name, publishers.company_name, books.year FROM books INNER JOIN books_authors ON books.isbn = books_authors.isbn INNER JOIN authors ON books_authors.author_id = authors.author_id INNER JOIN publishers ON books.publisher_id = publishers.publisher_id;

-- view users
SELECT * FROM `users`;

-- view authors
SELECT * FROM `authors`;

-- view publishers
SELECT * FROM `publishers`;

-- add new books
-- 'GET' method
query1: SELECT author_id, first_name, last_name from authors
SELECT publisher_id, company_name from publishers
query2: SELECT publisher_id, company_name from publishers
query3: SELECT isbn from books

-- 'POST' method
qeury1: INSERT INTO `books` (`isbn`, `title`, `price`, `publisher_id`, `year`, `book_img`)
VALUES (:in_isbn, :in_title, :in_price, :in_publisherID, :in_year, :in_book_img);
query2: INSERT INTO `books_authors` (`isbn`, `author_id`) VALUES (:in_isbn, :in_athor_id)

-- add new authors
-- 'GET' method
SELECT * FROM `authors`
-- 'POST' method
INSERT INTO `authors` (`first_name`, `last_name`, `address`, `url`) VALUES (:in_first_name, :in_last_name, :in_address, :in_url)

-- add new publishers
-- 'GET' method
SELECT * from `publishers`
-- 'POST' method
INSERT INTO `publishers` (`company_name`, `contact`, `address`, `url`) VALUES (:in_company_name, :in_contact, :in_address, :in_url)

-- delete books according to isbn
DELETE FROM `books` WHERE `isbn` = :in_isbn;

-- delete users according to email
DELETE FROM `users` WHERE `user_id` = :in_user_id;

-- when new book with new author is added
INSERT INTO `books_authors` (`isbn`, `author_id`)
VALUES (:in_isbn, :in_authorID);

-- book update
-- 'GET' method
SELECT * FROM `books` WHERE `isbn` = :in_isbn
-- 'POST' method
UPDATE `books` SET `price` = :in_price, `year` = :in_year, `book_img` = :in_book_img WHERE `isbn` = :in_isbn


-- -- -- -- -- --

-- LOGIN/REGISTER PAGES:

-- login with existed account
query1: SELECT `email`, `password` FROM `users`;
query2: SELECT `user_id` FROM `users`;

-- adding new user
-- 'GET' method
SELECT `user_id` FROM `users`;
-- 'POST' method
INSERT INTO `users` (`email`, `first_name`, `last_name`, `address`, `password`) VALUES (:in_email, :in_first_name, :in_last_name, :in_address, :in_password)

-- -- -- -- -- --

-- ACOUNT UPADATE:
-- 'GET' method
SELECT * FROM `users` WHERE `user_id` = :in_user_id;
-- 'POST' method
UPDATE `users` SET `email` = :in_email, `password` = :in_password, `address` = :in_address WHERE `user_id` = :in_user_id

-- -- -- -- -- --

-- SHOP PAGE:

-- searching available books by title
SELECT `books.title`, `books.isbn`, `authors.first_name`, `authors.last_name`, `publishers.company_name`, `books.year`, `books.price`, `books.book_img` 
	FROM `books` INNER JOIN `books_authors` ON `books.isbn` = `books_authors.isbn` INNER JOIN `authors` ON `books_authors.author_id` = `authors.author_id`
	INNER JOIN `publishers` ON `books.publisher_id` = `publishers.publisher_id` WHERE title LIKE "%:in_books_title%";


-- searching for available books by books
SELECT `books.title`, `books.isbn`, `authors.first_name`, `authors.last_name`, `publishers.company_name`, `books.year`, `books.price`, `books.book_img`
	FROM `books` INNER JOIN `books_authors` ON `books.isbn` = `books_authors.isbn` INNER JOIN `authors` ON `books_authors.author_id` = `authors.author_id`
	INNER JOIN `publishers` ON `books.publisher_id` = `publishers.publisher_id`;


-- adding new book to shopping cart
INSERT INTO `shopping_carts` (`date`)
VALUES (:in_date);

-- -- -- -- -- --

-- SHOPPING CART PAGE:

-- deletes removed books
DELETE FROM `shopping_carts` WHERE `date` = :in_date;

-- updates when a new order is placed/removed
INSERT INTO `shopping_carts` (`user_id`, `isbn`) VALUES (:in_user_id, :in_isbn);

-- -- -- -- -- --