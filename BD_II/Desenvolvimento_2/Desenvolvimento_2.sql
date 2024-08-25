-- Crie um banco de dados, adicione tabelas e determine quais são os atributos de cada uma. Em seguida, 
-- execute um trigger que se relacione com algum comando, como insert, select, delete ou update.

-- Criando novas tabelas
-- Criando tabela produtos
CREATE TABLE Produtos (
    produto_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    descricao TEXT,
    preco DECIMAL(10, 2),
    estoque INT
);

--Criando tabela ItensPedidos
CREATE TABLE ItensPedido (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    preco_unitario DECIMAL(10, 2),
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(produto_id)
);

-- Inserção de dados nas novas tabelas
-- Tabela produtos
INSERT INTO Produtos (nome, descricao, preco, estoque) VALUES
('Produto A', 'Descrição do Produto A', 50.00, 100),
('Produto B', 'Descrição do Produto B', 30.00, 200),
('Produto C', 'Descrição do Produto C', 20.00, 300);

-- Tabela ItensPedidos
INSERT INTO ItensPedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES
(1, 1, 2, 50.00),
(2, 2, 1, 30.00),
(3, 3, 5, 20.00),
(4, 1, 3, 50.00);

--- Criação de um Trigger
CREATE TRIGGER AtualizaEstoque
AFTER INSERT ON ItensPedido
FOR EACH ROW
BEGIN
    UPDATE Produtos
    SET estoque = estoque - NEW.quantidade
    WHERE produto_id = NEW.produto_id;
END;

-- Testando o Trigger
-- Inserindo Novo Item em Pedido
INSERT INTO ItensPedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES
(1, 2, 3, 30.00);

-- Verificando o Estoque Atualizado
SELECT * FROM Produtos WHERE produto_id = 2;
