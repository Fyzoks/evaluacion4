-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Servidor: localhost:4406
-- Tiempo de generación: 07-06-2023 a las 16:27:41
-- Versión del servidor: 5.5.42
-- Versión de PHP: 7.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de datos: `poo_c2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Dispositivos`
--

CREATE TABLE `Dispositivos` (
  `idDisp` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `ubicacion` varchar(60) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Dispositivos`
--

INSERT INTO `Dispositivos` (`idDisp`, `nombre`, `ubicacion`) VALUES
(1, 'Google Home', 'Dormitorio'),
(2, 'Alexa', 'Cocina'),
(5, 'SmartKit', 'living'),
(7, 'Prueba', 'Test'),
(8, 'test menu', 'inacap');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Mediciones`
--

CREATE TABLE `Mediciones` (
  `idMed` int(11) NOT NULL,
  `tipo` varchar(30) NOT NULL,
  `fecha` varchar(20) NOT NULL,
  `valor` int(11) NOT NULL,
  `idDisp` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Mediciones`
--

INSERT INTO `Mediciones` (`idMed`, `tipo`, `fecha`, `valor`, `idDisp`) VALUES
(1, 'humedad', '29-10-22', 56, 7);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Dispositivos`
--
ALTER TABLE `Dispositivos`
  ADD PRIMARY KEY (`idDisp`);

--
-- Indices de la tabla `Mediciones`
--
ALTER TABLE `Mediciones`
  ADD PRIMARY KEY (`idMed`),
  ADD KEY `Dispositivos_idDisp` (`idDisp`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Dispositivos`
--
ALTER TABLE `Dispositivos`
  MODIFY `idDisp` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT de la tabla `Mediciones`
--
ALTER TABLE `Mediciones`
  MODIFY `idMed` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
