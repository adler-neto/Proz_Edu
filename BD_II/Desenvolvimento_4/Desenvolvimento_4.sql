-- Uma loja tem um banco de dados que contém todo o controle de vendas de 
-- produtos e de cadastro de clientes. Pensando nisso, 
-- crie uma função para somar todos os clientes que foram cadastrados na loja durante um dia.

-- Criando a função
DELIMITER $$

CREATE FUNCTION ContarClientesPorDia(data DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE totalClientes INT;
    
    SELECT COUNT(*) INTO totalClientes
    FROM Clientes
    WHERE DATE(data_cadastro) = data;
    
    RETURN totalClientes;
END $$

DELIMITER ;

-- Adicionando a Coluna data_cadastro
ALTER TABLE Clientes ADD COLUMN data_cadastro DATE;

-- Cadastrando novos clintenes 
INSERT INTO Clientes (nome, email, telefone, data_cadastro) VALUES
('João Silva', 'joao.silva@example.com', '11999999999', '2024-08-25'),
('Maria Oliveira', 'maria.oliveira@example.com', '11988888888', '2024-08-25');

-- Execuntando a função
SELECT ContarClientesPorDia('2024-08-25') AS TotalClientes;
