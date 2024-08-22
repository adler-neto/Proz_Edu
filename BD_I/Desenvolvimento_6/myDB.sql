CREATE DATABASE escola;

CREATE TABLE ALUNO (
    ID SERIAL PRIMARY KEY,  -- Atributo ID como chave primária, autoincremento
    nome VARCHAR(100) NOT NULL,         -- Atributo nome, tipo varchar
    email VARCHAR(100),                 -- Atributo e-mail, tipo varchar
    endereco VARCHAR(255)               -- Atributo endereço, tipo varchar
);

SELECT * FROM escola