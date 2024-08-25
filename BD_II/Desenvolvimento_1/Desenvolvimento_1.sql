-- Criando o BD
CREATE DATABASE CadastroClientes;
USE CadastroClientes;

--Criando a tabela clientes
CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(15)
);

--Criando a tabela Endereços
CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(15)
);

-- Criando a tabela pedidos
CREATE TABLE Pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    data_pedido DATE,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
);

-- Inserindo Clientes
INSERT INTO Clientes (nome, email, telefone) VALUES
('João Silva', 'joao.silva@example.com', '11999999999'),
('Maria Oliveira', 'maria.oliveira@example.com', '11988888888'),
('Carlos Santos', 'carlos.santos@example.com', '11977777777');

-- Inserindo Endenreços
INSERT INTO Enderecos (cliente_id, endereco, cidade, estado, cep) VALUES
(1, 'Rua A, 123', 'São Paulo', 'SP', '01000-000'),
(2, 'Rua B, 456', 'Rio de Janeiro', 'RJ', '20000-000'),
(3, 'Rua C, 789', 'Belo Horizonte', 'MG', '30000-000');

-- Inserindo Pedidos
INSERT INTO Pedidos (cliente_id, data_pedido, valor_total) VALUES
(1, '2024-08-01', 150.00),
(2, '2024-08-02', 250.00),
(3, '2024-08-03', 350.00),
(1, '2024-08-04', 450.00);

-- Realizando consulta com Joins
-- Consulta: Listar os clientes com seus respectivos endereços
SELECT 
    Clientes.nome, 
    Enderecos.endereco, 
    Enderecos.cidade, 
    Enderecos.estado, 
    Enderecos.cep
FROM 
    Clientes
JOIN 
    Enderecos ON Clientes.cliente_id = Enderecos.cliente_id;

-- Consulta: Listar os clientes com seus respectivos pedidos
 SELECT 
    Clientes.nome, 
    Pedidos.data_pedido, 
    Pedidos.valor_total
FROM 
    Clientes
JOIN 
    Pedidos ON Clientes.cliente_id = Pedidos.cliente_id;

--Consulta: Listar os clientes que têm pedidos acima de R$ 300,00
SELECT 
    Clientes.nome, 
    Pedidos.data_pedido, 
    Pedidos.valor_total
FROM 
    Clientes
JOIN 
    Pedidos ON Clientes.cliente_id = Pedidos.cliente_id
WHERE 
    Pedidos.valor_total > 300.00;
