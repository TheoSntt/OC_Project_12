CREATE DATABASE epicevents;

USE epicevents;

CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telephone` int DEFAULT NULL,
  `nom_entreprise` varchar(255) NOT NULL,
  `date_creation` date DEFAULT (NOW()),
  `date_dernier_contact` date DEFAULT NULL,
  `id_commercial` int NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `evenement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `start_date` date,
  `end_date` date,
  `location` varchar(500),
  `attendees` int,
  `comments` varchar(1000),
  `id_support` int NOT NULL,
  `id_contrat` int NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `contrat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `start_date` date,
  `end_date` date,
  `location` varchar(500),
  `attendees` int,
  `comments` varchar(1000),
  `id_support` int NOT NULL,
  `id_contrat` int NOT NULL,
  PRIMARY KEY (`id`)
);