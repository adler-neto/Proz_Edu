-- Uma empresa de vendas tem um banco de dados com informações sobre os seus produtos. 
-- Ela precisa criar um relatório que faça um levantamento diário da quantidade de produtos comprados por dia.
-- Para ajudar a empresa, crie um procedure para agilizar esse processo.

-- Criando uma Procedure 
DELIMITER $$

CREATE PROCEDURE RelatorioDiarioVendas()
BEGIN
    SELECT 
        p.data_pedido AS Data,
        i.produto_id AS ProdutoID,
        pr.nome AS ProdutoNome,
        SUM(i.quantidade) AS QuantidadeVendida
    FROM 
        ItensPedido i
    JOIN 
        Pedidos p ON i.pedido_id = p.pedido_id
    JOIN 
        Produtos pr ON i.produto_id = pr.produto_id
    GROUP BY 
        p.data_pedido, i.produto_id
    ORDER BY 
        p.data_pedido, pr.nome;
END $$

DELIMITER ;

