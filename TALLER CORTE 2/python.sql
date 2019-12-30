-- Adminer 4.7.3 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `python`;
CREATE DATABASE `python` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `python`;

DROP TABLE IF EXISTS `contacto`;
CREATE TABLE `contacto` (
  `correo` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL,
  `celular` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `contacto` (`correo`, `telefono`, `celular`, `direccion`) VALUES
('iglesiasat@yopmail.com',	'',	'3215726683',	'Carrera 12 Norte #16B-65');

DROP TABLE IF EXISTS `informacion`;
CREATE TABLE `informacion` (
  `info` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `informacion` (`info`) VALUES
('La Iglesia de Satán es una organización religiosa legalmente oficial, fundada en la noche de Walpurgis de 1966 por Anton Szandor LaVey en San Francisco, California. Según su sistema, este día es el año I del reino de Satanás. Actualmente, el Sumo Sacerdote de la Iglesia de Satán es Peter H. Gilmore. Actualmente tiene su sede en el barrio de Poughkeepsie, Nueva York.\r\n\r\nSADASDASD');

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `documento` varchar(255) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `usuarios` (`id`, `documento`, `contrasena`, `nombre`, `correo`) VALUES
(1,	'1112788514',	'e10adc3949ba59abbe56e057f20f883e',	'Juan David',	'juan_dx1996@hotmail.com'),
(2,	'asdasdasd',	'e10adc3949ba59abbe56e057f20f883e',	'asdasd',	'asdasd');

-- 2019-10-14 04:56:09
