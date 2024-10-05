-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: brqxd0rfhpuczons9wai-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 05-10-2024 a las 20:06:15
-- Versión del servidor: 8.0.22-13
-- Versión de PHP: 8.2.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `brqxd0rfhpuczons9wai`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributo`
--

CREATE TABLE `atributo` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `descripcion` varchar(300) COLLATE utf8mb4_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `atributo`
--

INSERT INTO `atributo` (`id`, `nombre`, `descripcion`, `estado`) VALUES
(1, 'Direccion', 'Direccion del dueño', 1),
(2, 'Tipo', 'Tipo de Mascota', 1),
(3, 'Nombre', 'Nombre del encargado', 1),
(4, 'Direccion', 'Direccion del encargado', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributoxusuario`
--

CREATE TABLE `atributoxusuario` (
  `id` int NOT NULL,
  `id_usuario` int NOT NULL,
  `id_atributo` int NOT NULL,
  `valor` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `atributoxusuario`
--

INSERT INTO `atributoxusuario` (`id`, `id_usuario`, `id_atributo`, `valor`, `descripcion`, `estado`) VALUES
(6, 6, 1, 'Calle43 #5-A', 'Direccion del dueño de la mascota x', 1),
(7, 7, 1, 'Carrera80 #54-A', 'Direccion del dueño de las mascotas llamadas Susi y Mishifu', 1),
(10, 12, 2, 'Perro', 'Zeus es un perro de raza Pitbull y esta registrado con el ID 10', 1),
(11, 7, 2, 'Perro', 'Susi es un perro de raza Pincher y esta registrado con el ID 7', 1),
(12, 29, 2, 'Perro', 'Kratos es un perro de raza Pudull y esta registrado con el ID 11', 1),
(13, 31, 2, 'Gato', 'Firulais es un gato de raza Egipcia y esta registrado con el ID 12', 1),
(14, 14, 2, 'perro', 'Habib Tiene un perro', 1),
(16, 14, 1, 'Carrera 51B', 'Direccion de Habib', 1),
(17, 12, 1, 'Calle 38 14A', 'Direccion de Jesus', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota`
--

CREATE TABLE `mascota` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `tipo_mascota` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `id_propietario` int NOT NULL,
  `coordenadas` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `fecha_hora` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mascota`
--

INSERT INTO `mascota` (`id`, `nombre`, `tipo_mascota`, `id_propietario`, `coordenadas`, `fecha_hora`, `estado`) VALUES
(7, 'Susi', 'Perra', 7, 'Soledad', '2024-09-28 20:48:19', 1),
(9, 'Destructor de universos', 'Chihuahua', 14, 'Barranquilla', '2024-10-02 17:53:18', 1),
(10, 'Zeus', 'Perro', 12, 'Barranquilla', '2024-10-04 17:47:36', 1),
(11, 'Kratos', 'Perro', 29, 'Barranquilla', '2024-10-04 17:48:03', 0),
(12, 'Firulais', 'Gato', 31, 'Ponedera', '2024-10-04 17:49:06', 0),
(13, 'Mishifu', 'Perro', 7, 'Soledad', '2024-10-04 17:49:36', 1),
(14, 'Galaxy', 'Perro', 14, 'Ponedera', '2024-10-04 17:53:05', 0),
(15, 'Junior', 'Gato', 27, 'Soledad', '2024-10-04 17:53:52', 1),
(16, 'UNITY', 'Perro', 30, 'Soledad', '2024-10-04 17:54:35', 0),
(17, 'Keilyn', 'Gato', 30, 'Soledad', '2024-10-04 17:55:00', 0),
(19, 'Fenrir', 'Perro', 14, 'Asgard', '2024-10-04 19:24:53', 1),
(21, 'Thor', 'Perro', 7, 'Soledad', '2024-10-05 03:53:36', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre`, `estado`) VALUES
(1, 'Administrador', 1),
(2, 'Usuario', 1),
(3, 'Mascota', 1),
(4, 'Encargado', 1),
(5, 'Moderador', 1),
(6, 'Veterinario', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `apellido` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `documento` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `id_rol` int DEFAULT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `email`, `password`, `nombre`, `apellido`, `documento`, `telefono`, `id_rol`, `estado`) VALUES
(6, 'Tristandonado@gmail.com', '123456', 'Tristan gabriel', 'Donado gutierrez', '1042421710', '3013968109', 2, 1),
(7, 'Juancharris@gmail.com', '123456677', 'Juan David', 'Charris Barcelo', '11223344', '3008644854', 2, 1),
(12, 'Jesus@gmail.com', 'Jesus123', 'Jesus Alfredo', 'Coronado Vertel', '1012345645', '3015456156', 2, 1),
(14, 'hmorales@gmail.com', '5555', 'Habib', 'Minaya', '1000001', '301273723', 1, 0),
(27, 'Jesus@gmail.com.co', '142545561', 'Jesus', 'Camilo', '1231232', '156354', 1, 0),
(28, 'Henry@hotmail.com}', 'H78945984', 'Henry', 'Cardona0', '12324341', '156355', 2, 1),
(29, 'David@hotmail.com', 'hidsjnd6215615', 'David', 'Perejil', '23434231', '156356', 2, 0),
(30, 'Mauricio@gmail.com', 'Carlos252426', 'Mauricio', 'Venezuela', '213243243', '156357', 2, 0),
(31, 'Vertuz@gmail.com', 'Hasjsidonc44', 'Vertuz', 'Vertel', '231233454', '156358', 2, 0),
(32, 'Pedro@hotmail.com', '81515123135', 'Pedro', 'Lopez', '543545353', '156359', 1, 0),
(41, 'JuanCH@gmail.com', '123456', 'Juan', 'Charris', '10214578', '3014758495', 1, 1),
(42, 'Jesus25487@gmail.com.co', '142545561', 'Jesus', 'Camilo', '1231232', '156354', 1, 1),
(43, 'H215487@hotmail.com', 'H78945984', 'Henry', 'Cardona0', '12324341', '156355', 2, 1),
(44, 'David@gmail.com', 'hidsjnd6215615', 'David', 'Perejil', '23434231', '156356', 2, 0),
(45, 'MauricioA2415@gmail.com', 'Carlos252426', 'Mauricio', 'Venezuela', '213243243', '156357', 2, 0),
(46, 'Vertuz987564@gmail.com', 'Hasjsidonc44', 'Vertuz', 'Vertel', '231233454', '156358', 2, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `atributoxusuario`
--
ALTER TABLE `atributoxusuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`,`id_atributo`),
  ADD KEY `id_atributo` (`id_atributo`);

--
-- Indices de la tabla `mascota`
--
ALTER TABLE `mascota`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_propietario` (`id_propietario`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `atributo`
--
ALTER TABLE `atributo`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `atributoxusuario`
--
ALTER TABLE `atributoxusuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `mascota`
--
ALTER TABLE `mascota`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `atributoxusuario`
--
ALTER TABLE `atributoxusuario`
  ADD CONSTRAINT `atributoxusuario_ibfk_1` FOREIGN KEY (`id_atributo`) REFERENCES `atributo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `atributoxusuario_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `mascota`
--
ALTER TABLE `mascota`
  ADD CONSTRAINT `mascota_ibfk_1` FOREIGN KEY (`id_propietario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
