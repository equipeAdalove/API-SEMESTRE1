create database api1ads;
use api1ads;

create table formulario 
(
    func_id int primary key not null,
    nome varchar(60) not null,
    nota int not null,
    opiniao varchar(255) not null
);