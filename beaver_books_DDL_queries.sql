-- Project Step 4 Draft Version: DML and DDL Queries
-- Author: Junhyeok Jeong

--
-- Table structure for table `shopping_carts`
--

DROP TABLE IF EXISTS `shopping_carts`;

CREATE TABLE `shopping_carts` (
  `order_id` int(11) NOT NULL,
  `date` timestamp NOT NULL,
  `count` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shopping_carts`
--


INSERT INTO `shopping_carts` VALUES
	(123,'2020-02-15 13:03:42',2),
	(124,'2020-02-16 15:05:12',1);

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `order_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `address` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--


INSERT INTO `users` VALUES
	(123,'benny@oregonstate.edu','Benny','Beaver','1234 NW Corvallis Avenue, Corvallis, Oregon','gobeavs'),
	(124,'duck@uoregon.edu','Puddles','Duck','5678 SW Eugene Avenue, Eugene, Oregon','goducks');


--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;

CREATE TABLE `books` (
  `order_id` int(11) NOT NULL,
  `isbn` int(11) NOT NULL,
  `author_id` smallint(5) unsigned NOT NULL,
  `title` varchar(255) NOT NULL,
  `price` decimal(4,2) NOT NULL,
  `publisher_id` smallint(5) unsigned NOT NULL,
  `year` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books`
--

INSERT INTO `books` VALUES
	(123,0060935464,1,'To Kill a Mockingbird',17.30,1,1960),
  (123,0060934344,2,'Don Quixote',21.03,2,1605),
  (124,1684052084,3,'DuckTales: Treasure Trove',8.26,3,2018);


--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;

CREATE TABLE `authors` (
  `author_id` int(11) NOT NULL,
  `isbn` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `address` varchar(255),
  `url` varchar(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` VALUES
	(1,0060935464,'Harper','Lee','195 Broadway Floor 22, New York, NY 10007 USA', 'https://www.biography.com/writer/harper-lee'),
	(2,0060934344,'Miguel De','Cervantes','Madrid, Spain','https://www.biography.com/writer/miguel-de-cervantes'),
  (3,1684052084,'Joe','Caramagna',NULL,'https://marvel.fandom.com/wiki/Joe_Caramagna_(Earth-1218)');

--
-- Table structure for table `publishers`
--

DROP TABLE IF EXISTS `publishers`;

CREATE TABLE `publishers` (
  `publisher_id` int(11) NOT NULL,
  `isbn` int(11) NOT NULL,
  `company_name` varchar(45) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `address` varchar(255),
  `url` varchar(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `publishers`
--

INSERT INTO `publishers` VALUES
	(1,0060935464,'J. B. Lippincott & Co.','(215) 732-6200','227 S. 6th Street, Philadelphia, PA 19106 USA', NULL),
	(2,0060934344,'Ecco Press','(212) 207-7000','195 Broadway, New York, NY 10007 USA','https://www.harpercollins.com/corporate/customer-service/contact-us/'),
  (3,1684052084,'IDW Publishing','info@idwpublishing.com','2765 Truxtun Road, San Diego, CA 92106 USA','https://www.idwpublishing.com/contact/');

-- Index
ALTER TABLE `shopping_carts`
  ADD PRIMARY KEY (`order_id`);
