-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: b4doekmqoqseuuhpvht5-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 26-10-2024 a las 22:55:19
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
-- Base de datos: `b4doekmqoqseuuhpvht5`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributo`
--

CREATE TABLE `atributo` (
  `id` int NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `descripcion` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `atributo`
--

INSERT INTO `atributo` (`id`, `nombre`, `descripcion`, `estado`) VALUES
(1, 'Direccion', 'Direccion del dueño', 1),
(3, 'Nombre', 'Nombre del encargado', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributoxusuario`
--

CREATE TABLE `atributoxusuario` (
  `id` int NOT NULL,
  `id_usuario` int NOT NULL,
  `id_atributo` int NOT NULL,
  `valor` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `descripcion` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `collares_con_gps`
--

CREATE TABLE `collares_con_gps` (
  `id` int NOT NULL,
  `numero_serie` varchar(30) NOT NULL,
  `latitud` varchar(535) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `longitud` varchar(535) NOT NULL,
  `nivel_bateria` tinyint NOT NULL,
  `fecha_hora_ultimo_reporte` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_mascota_vinculada` int NOT NULL,
  `estado` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero_mascota`
--

CREATE TABLE `genero_mascota` (
  `id` int NOT NULL,
  `genero` varchar(50) NOT NULL,
  `estado` tinyint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `genero_mascota`
--

INSERT INTO `genero_mascota` (`id`, `genero`, `estado`) VALUES
(1, 'Macho', 1),
(2, 'Hembra', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_ubicaciones`
--

CREATE TABLE `historial_ubicaciones` (
  `id` int NOT NULL,
  `id_collar` int NOT NULL,
  `latitud` varchar(535) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `longitud` varchar(535) NOT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `distancia_recorrida` varchar(125) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota`
--

CREATE TABLE `mascota` (
  `id` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_genero_mascota` int NOT NULL,
  `id_tipo_mascota` int NOT NULL,
  `id_user` int NOT NULL,
  `fecha_hora` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
(5, 'Moderador', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_mascota`
--

CREATE TABLE `tipo_mascota` (
  `id` int NOT NULL,
  `tp_mascota` varchar(50) NOT NULL,
  `estado` tinyint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tipo_mascota`
--

INSERT INTO `tipo_mascota` (`id`, `tp_mascota`, `estado`) VALUES
(1, 'Perro', 1),
(2, 'Gato', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apellido` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `documento` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `telefono` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `id_rol` int DEFAULT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `zonas_seguras`
--

CREATE TABLE `zonas_seguras` (
  `id` int NOT NULL,
  `nombre_zona` varchar(125) NOT NULL,
  `latitud` varchar(535) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `longitud` varchar(535) NOT NULL,
  `id_mascota` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `atributoxusuario`
--
ALTER TABLE `atributoxusuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`,`id_atributo`),
  ADD KEY `id_atributo` (`id_atributo`);

--
-- Indices de la tabla `collares_con_gps`
--
ALTER TABLE `collares_con_gps`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_mascota_vinculada` (`id_mascota_vinculada`);

--
-- Indices de la tabla `genero_mascota`
--
ALTER TABLE `genero_mascota`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `genero` (`genero`);

--
-- Indices de la tabla `historial_ubicaciones`
--
ALTER TABLE `historial_ubicaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_collar` (`id_collar`);

--
-- Indices de la tabla `mascota`
--
ALTER TABLE `mascota`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_propietario` (`id_user`),
  ADD KEY `id_tipo_mascota` (`id_tipo_mascota`),
  ADD KEY `id_genero_mascota` (`id_genero_mascota`),
  ADD KEY `id_genero_mascota_2` (`id_genero_mascota`),
  ADD KEY `id_user` (`id_user`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `tipo_mascota`
--
ALTER TABLE `tipo_mascota`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `documento` (`documento`),
  ADD KEY `id_rol` (`id_rol`);

--
-- Indices de la tabla `zonas_seguras`
--
ALTER TABLE `zonas_seguras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_mascota` (`id_mascota`);

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
-- AUTO_INCREMENT de la tabla `collares_con_gps`
--
ALTER TABLE `collares_con_gps`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `genero_mascota`
--
ALTER TABLE `genero_mascota`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `historial_ubicaciones`
--
ALTER TABLE `historial_ubicaciones`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `mascota`
--
ALTER TABLE `mascota`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `tipo_mascota`
--
ALTER TABLE `tipo_mascota`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `zonas_seguras`
--
ALTER TABLE `zonas_seguras`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

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
-- Filtros para la tabla `collares_con_gps`
--
ALTER TABLE `collares_con_gps`
  ADD CONSTRAINT `collares_con_gps_ibfk_1` FOREIGN KEY (`id_mascota_vinculada`) REFERENCES `mascota` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `historial_ubicaciones`
--
ALTER TABLE `historial_ubicaciones`
  ADD CONSTRAINT `historial_ubicaciones_ibfk_1` FOREIGN KEY (`id_collar`) REFERENCES `collares_con_gps` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `mascota`
--
ALTER TABLE `mascota`
  ADD CONSTRAINT `mascota_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `mascota_ibfk_2` FOREIGN KEY (`id_tipo_mascota`) REFERENCES `tipo_mascota` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `mascota_ibfk_3` FOREIGN KEY (`id_genero_mascota`) REFERENCES `genero_mascota` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`);

--
-- Filtros para la tabla `zonas_seguras`
--
ALTER TABLE `zonas_seguras`
  ADD CONSTRAINT `zonas_seguras_ibfk_1` FOREIGN KEY (`id_mascota`) REFERENCES `mascota` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
