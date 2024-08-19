-- Tabelas normalizadas 
SELECT * FROM Cliente;

SELECT * FROM Vendedor;

SELECT * FROM Carro;

SELECT * FROM Combustivel;

SELECT * FROM Locacao;


-- Criação das views para o Modelo Dimensional

-- Dimensão Cliente
CREATE VIEW Dim_Cliente AS
SELECT id AS idCliente,
		nome AS Nome,
		cidade AS Cidade,
		estado AS Estado,
		pais AS Pais
FROM Cliente;	

-- Dimensão Vendedor
CREATE VIEW Dim_Vendedor AS
SELECT id AS idVendedor,
		nome AS Nome,
		sexo AS Sexo,
		estado AS Estado
FROM Vendedor;

-- Dimensão Carro
CREATE VIEW Dim_Carro AS
SELECT id AS idCarro,
		classi AS Classi,
		marca AS Marca,
		modelo AS Modelo,
		ano AS Ano
FROM Carro;

-- Dimensão Combustivel
CREATE VIEW Dim_Combustivel AS
SELECT id AS idCombustivel,
		tipo AS Tipo
FROM Combustivel;	

-- Fato Locacao
CREATE VIEW Fato_Locacao AS
SELECT l.id AS idLocacao,
		l.idCliente,
		l.idVendedor,
		l.idCarro,
		c.id AS idCombustivel,
		l.kmCarro,
		l.data AS Data,
		l.hora AS Hora,
		l.qtdDiaria AS Quantidade_Diaria,
		l.vlrDiaria AS Valor_Diaria,
		l.dataEntrega AS Data_Entrega,
		l.horaEntrega AS Hora_Entrega
FROM Locacao l 
	JOIN Carro AS ca ON l.idCarro = ca.id
	JOIN Combustivel AS c ON ca.idCombustivel = c.id;
	
	
-- Tabelas Dimensionais

SELECT * FROM Dim_Cliente;

SELECT * FROM Dim_Vendedor;

SELECT * FROM Dim_Carro;

SELECT * FROM Dim_Combustivel;

SELECT * FROM Fato_Locacao;
