-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  ven. 25 déc. 2020 à 00:58
-- Version du serveur :  10.4.8-MariaDB
-- Version de PHP :  7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `affar`
--

-- --------------------------------------------------------

--
-- Structure de la table `images`
--

CREATE TABLE `images` (
  `id_image` int(3) NOT NULL,
  `source` varchar(255) NOT NULL,
  `id_produit` int(3) NOT NULL,
  `premier` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `images`
--

INSERT INTO `images` (`id_image`, `source`, `id_produit`, `premier`) VALUES
(8, '131824595_1318965391814038_8740094049047053032_n.jpg', 1, 0),
(9, '131946812_416321672824686_1308836198055561259_n.png', 1, 0),
(10, '131824595_1318965391814038_8740094049047053032_n.jpg', 20, 0),
(11, '131946812_416321672824686_1308836198055561259_n.png', 20, 0),
(12, '132173521_380662763230052_26737300105979931_n.jpg', 20, 0),
(13, '131824595_1318965391814038_8740094049047053032_n.jpg', 21, 0),
(14, '131946812_416321672824686_1308836198055561259_n.png', 21, 0),
(15, '132173521_380662763230052_26737300105979931_n.jpg', 21, 0);

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

CREATE TABLE `produit` (
  `id_produit` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `categorie` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `prix` float NOT NULL,
  `date_ajout` datetime NOT NULL,
  `numero` int(11) NOT NULL,
  `ville` varchar(15) NOT NULL,
  `etat` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`id_produit`, `id`, `title`, `categorie`, `description`, `prix`, `date_ajout`, `numero`, `ville`, `etat`) VALUES
(13, 0, 'a50', '0', 'tres bon etat', 800, '2020-12-24 22:12:53', 27149406, '', 1),
(14, 0, 'lenovo', '1', 'tres bon etat', 800, '2020-12-24 22:13:51', 27149406, '', 1),
(15, 0, 'lenovo', '1', 'pas', 900, '2020-12-24 22:47:19', 27149406, '', 1),
(16, 0, 'a50', '0', 'tres bon etat', 150, '2020-12-24 22:49:11', 97651638, '', 1),
(17, 0, 'a50', '0', 'tres bon etat', 900, '2020-12-24 22:58:44', 97651638, '', 1),
(18, 0, 'a80', '0', 'tres bon etat', 1500, '2020-12-24 22:59:26', 97651638, '', 1),
(19, 0, 'a85', '0', 'tres bon etat', 1500, '2020-12-24 23:00:38', 97651638, '', 1),
(20, 0, 'a78', '0', 'ok', 3000, '2020-12-24 23:04:07', 2554812, '', 1),
(21, 38, 'pc portable', '1', 'ok', 980, '2020-12-25 00:09:21', 27149406, '', 1),
(22, 38, 'dsfdsf', '0', 'gfhfghf', 900, '2020-12-25 00:18:36', 97651638, '', 1);

-- --------------------------------------------------------

--
-- Structure de la table `uploads`
--

CREATE TABLE `uploads` (
  `id` int(11) NOT NULL,
  `file_name` varchar(150) NOT NULL,
  `upload_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `uploads`
--

INSERT INTO `uploads` (`id`, `file_name`, `upload_time`) VALUES
(20, '131824595_1318965391814038_8740094049047053032_n.jpg', '2020-12-24 20:56:29'),
(21, '131946812_416321672824686_1308836198055561259_n.png', '2020-12-24 20:56:29'),
(22, '132173521_380662763230052_26737300105979931_n.jpg', '2020-12-24 20:56:29');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(4) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pseudo` varchar(255) NOT NULL,
  `phone` int(14) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `email`, `pseudo`, `phone`, `password`) VALUES
(38, 'saifnacer4@gmail.com', 'Ben naser Saif Eddine', 27149406, 'azerty'),
(39, 'cscsc@scsc', 'alew', 97651638, '12345'),
(40, 'saifnacer4@gmail.com', 'hisoka', 245895115, '123'),
(41, 'saifnacer4@gmail.com', 'hisoka', 2147483647, '1234'),
(42, 'saifnacer4@gmail.com', 'Ben naser Saif Eddine', 27149406, 'azerty'),
(46, 'saifnacer4@gmail.com', 'hisoka', 2147483647, '123'),
(47, 'saifnacer4@gmail.com', 'hisoka', 2147483647, 'admin');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id_image`);

--
-- Index pour la table `produit`
--
ALTER TABLE `produit`
  ADD PRIMARY KEY (`id_produit`);

--
-- Index pour la table `uploads`
--
ALTER TABLE `uploads`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `images`
--
ALTER TABLE `images`
  MODIFY `id_image` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `produit`
--
ALTER TABLE `produit`
  MODIFY `id_produit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT pour la table `uploads`
--
ALTER TABLE `uploads`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
