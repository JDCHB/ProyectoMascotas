create database pruebacl

use pruebacl

create table usuarios(
    id int auto_increment,
    email varchar(255) not null,
    password varchar(255) not null,
    nombre varchar(255) not null,
    apellido varchar(255) not null,
    documento varchar(255)  not null,
    telefono varchar(255) not null,
    primary key(id)
)

insert into usuarios (email,password,nombre,apellido,documento,telefono)
values ('pedro@gamil.com','p123456','pedro','picasso','11223344','3204566789')

CREATE TABLE `mascotas`.`mascota` (
    `id` INT NOT NULL AUTO_INCREMENT ,
    `nombre` VARCHAR(255) NOT NULL ,
    `tipo_mascota` VARCHAR(255) NOT NULL ,
    `id_dueño` INT NOT NULL ,
    `Cordenadas` VARCHAR(255) NOT NULL ,
    `fecha_hora` DATE NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;