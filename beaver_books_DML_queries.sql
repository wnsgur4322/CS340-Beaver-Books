-- Name: Junhyeok (Derek) Jeong and Joelle Perez
-- Date: February 24, 2020
-- Class: CS340-400
-- Program: Project Step 4 Draft Version (DML)

--Variables are denoted by :

-- ABOUT & INDEX PAGES: no queries

-- -- -- -- -- --

-- ADMIN PAGE: 

-- view books
SELECT * FROM `books`;

-- view users
SELECT * FROM `users`;

-- add books
INSERT INTO `books` (`isbn`, `author_id`, `title`, `price`, `publisher_id`, `year`)
VALUES (:in_isbn, :in_authorID, :in_title, :in_price, :in_publisherID, :in_year);

-- delete books according to isbn
DELETE FROM `books` WHERE `isbn` = :in_isbn;

-- updates when new user registers
UPDATE `users` SET `email`= :in_email, `password` = :in_pass;

-- delete users according to email
DELETE FROM `users` WHERE `email` = :in_email;

-- when new book with new author is added
INSERT INTO `books_authors` (`isbn`, `author_id`)
VALUES (:in_isbn, :in_authorID);

-- deleting author which deletes there books
DELETE FROM `books_authors` WHERE `isbn` = :in_isbn AND `author_id` = :in_authorID;

-- deleting existing books which deletes books in shopping carts
DELETE FROM `books_shopping_carts` WHERE `isbn` = :in_isbn AND `order_id` = :in_orderID;

-- -- -- -- -- --

-- LOGIN/REGISTER PAGES:

-- inserting login info/adding new user
INSERT INTO `users` (`email`, `password`)
VALUES (:in_email, :in_pass);

-- -- -- -- -- --

-- SHOP PAGE:

-- searching available books by authors
SELECT `first_name`, `last_name` FROM `authors`;

-- searching for available books by books
SELECT `title` FROM `books`;

-- adding new book to shopping cart
INSERT INTO `shopping_carts` (`date`)
VALUES (:in_date);

-- -- -- -- -- --

-- SHOPPING CART PAGE:

-- deletes removed books
DELETE FROM `shopping_carts` WHERE `order_id` = :in_orderID;

-- updates when a new order is placed/removed
UPDATE `shopping_carts` SET `order_id` = :in_orderID, `count` = :in_count;

-- -- -- -- -- --