create database remington;
create user user_remington with password '1q2w3e4r';
grant all privileges on database remington to user_remington;


-- se cierra sesion y se inicia con el usuario remington
--  \d  --> visualizar tablas creadas por consola
--  

create table estudiante(
    id serial primary key not null,
    nombres varchar (70) not null,
    apellidos varchar (70) not null,
    tipo_documento varchar(2) not null,
    fecha_nacimiento date not null,
    correo varchar(50) not null,
    carrera varchar(50) not null
);

create table nota(
    id serial primary key not null,
    estudiante int not null references estudiante(id) on delete cascade,
    nombre varchar (80) not null,
    valor float not null,
    materia varchar (50) not null
);