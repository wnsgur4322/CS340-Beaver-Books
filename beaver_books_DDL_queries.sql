-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: classmysql.engr.oregonstate.edu:3306
-- Generation Time: Mar 09, 2020 at 12:18 AM
-- Server version: 10.4.11-MariaDB-log
-- PHP Version: 7.0.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_jeongju`
--

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
CREATE TABLE `authors` (
  `author_id` int(11) UNSIGNED NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`author_id`, `first_name`, `last_name`, `address`, `url`) VALUES
(0, 'kimchi', 'tester', 'anywhere on the earth', 'https://google.com'),
(1, 'Harper', 'Lee', '195 Broadway Floor 22, New York, NY 10007 USA', 'https://www.biography.com/writer/harper-lee'),
(2, 'Miguel De', 'Cervantes', 'Madrid, Spain', 'https://www.biography.com/writer/miguel-de-cervantes'),
(3, 'Joe', 'Caramagna', NULL, 'https://marvel.fandom.com/wiki/Joe_Caramagna_(Earth-1218)'),
(4, 'Joey', 'Cavalieri', NULL, 'https://sva.edu/faculty/joey-cavalieri');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `isbn` int(10) UNSIGNED ZEROFILL NOT NULL,
  `title` varchar(255) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `publisher_id` int(11) UNSIGNED NOT NULL,
  `year` int(2) NOT NULL,
  `book_img` varchar(555) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`isbn`, `title`, `price`, `publisher_id`, `year`, `book_img`) VALUES
(0060934344, 'Don Quixote', '21.03', 2, 1605, 'https://images-na.ssl-images-amazon.com/images/I/410UIVet23L._SX311_BO1,204,203,200_.jpg'),
(0060935464, 'To Kill a Mockingbird', '17.30', 1, 1960, 'https://images-na.ssl-images-amazon.com/images/I/51JBKEB3ecL._SX295_BO1,204,203,200_.jpg'),
(1684052084, 'DuckTales: Treasure Trove', '8.26', 3, 2018, 'https://images-na.ssl-images-amazon.com/images/I/51YTMe783WL._SX329_BO1,204,203,200_.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `books_authors`
--

DROP TABLE IF EXISTS `books_authors`;
CREATE TABLE `books_authors` (
  `isbn` int(10) UNSIGNED ZEROFILL NOT NULL,
  `author_id` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books_authors`
--

INSERT INTO `books_authors` (`isbn`, `author_id`) VALUES
(0060935464, 1),
(0060934344, 2),
(1684052084, 4),
(1684052084, 3);

-- --------------------------------------------------------

--
-- Table structure for table `publishers`
--

DROP TABLE IF EXISTS `publishers`;
CREATE TABLE `publishers` (
  `publisher_id` int(11) UNSIGNED NOT NULL,
  `company_name` varchar(45) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `publishers`
--

INSERT INTO `publishers` (`publisher_id`, `company_name`, `contact`, `address`, `url`) VALUES
(1, 'J. B. Lippincott & Co.', '(215) 732-6200', '227 S. 6th Street, Philadelphia, PA 19106 USA', NULL),
(2, 'Ecco Press', '(212) 207-7000', '195 Broadway, New York, NY 10007 USA', 'https://www.harpercollins.com/corporate/customer-service/contact-us/'),
(3, 'IDW Publishing', 'info@idwpublishing.com', '2765 Truxtun Road, San Diego, CA 92106 USA', 'https://www.idwpublishing.com/contact/');

-- --------------------------------------------------------

--
-- Table structure for table `shopping_carts`
--

DROP TABLE IF EXISTS `shopping_carts`;
CREATE TABLE `shopping_carts` (
  `user_id` int(11) UNSIGNED NOT NULL,
  `isbn` int(10) UNSIGNED ZEROFILL NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shopping_carts`
--

INSERT INTO `shopping_carts` (`user_id`, `isbn`, `date`) VALUES
(1, 0060935464, '2020-02-15 21:03:42'),
(1, 0060934344, '2020-02-15 21:05:22'),
(2, 1684052084, '2020-02-16 23:05:12'),
(3, 1684052084, '2020-02-25 08:05:15');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` int(11) UNSIGNED NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `address` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `email`, `first_name`, `last_name`, `address`, `password`) VALUES
(1, 'kimchi@gmail', 'Taco', 'Kimchi', 'Super admin acccount', 'taco'),
(2, 'benny@oregonstate.edu', 'Benny', 'Beaver', '1234 NW Corvallis Avenue, Corvallis, Oregon', 'gobeavs'),
(3, 'duck@uoregon.edu', 'Puddles', 'Duck', '5678 SW Eugene Avenue, Eugene, Oregon', 'goducks'),
(4, 'test@test.com', 'kimchi', 'kimchi', 'test street ', 'test');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`author_id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`isbn`),
  ADD KEY `publisher_id` (`publisher_id`);

--
-- Indexes for table `books_authors`
--
ALTER TABLE `books_authors`
  ADD KEY `isbn` (`isbn`),
  ADD KEY `author_id` (`author_id`);

--
-- Indexes for table `publishers`
--
ALTER TABLE `publishers`
  ADD PRIMARY KEY (`publisher_id`);

--
-- Indexes for table `shopping_carts`
--
ALTER TABLE `shopping_carts`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `isbn` (`isbn`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

ALTER TABLE `authors`
  MODIFY `author_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `publishers`
  MODIFY `publisher_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`publisher_id`) REFERENCES `publishers` (`publisher_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `books_authors`
--
ALTER TABLE `books_authors`
  ADD CONSTRAINT `books_authors_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `authors` (`author_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `books_authors_ibfk_2` FOREIGN KEY (`isbn`) REFERENCES `books` (`isbn`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `shopping_carts`
--
ALTER TABLE `shopping_carts`
  ADD CONSTRAINT `shopping_carts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `shopping_carts_ibfk_2` FOREIGN KEY (`isbn`) REFERENCES `books` (`isbn`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
