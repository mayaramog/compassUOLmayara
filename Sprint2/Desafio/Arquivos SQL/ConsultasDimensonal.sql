SELECT * FROM Dim_Cliente

SELECT * FROM Fato_Locacao

SELECT idCLiente, COUNT(idCliente) AS qtd_locacoes
FROM Fato_Locacao
GROUP BY idCliente

SELECT l.idCliente, c.Nome, COUNT(l.idCliente) AS qtd_locacoes
FROM Fato_Locacao AS l
	JOIN Dim_Cliente AS c ON l.idCliente = c.idCliente 
GROUP BY l.idCliente, c.Nome;

SELECT l.idCombustivel, co.Tipo, COUNT(l.idCombustivel)
FROM Fato_Locacao l
	JOIN Dim_Combustivel AS co ON l.idCombustivel = co.idCombustivel 
GROUP BY l.idCombustivel, co.Tipo	

SELECT l.idCarro, ca.Marca, ca.Modelo, COUNT(l.idCarro), l.idCombustivel, co.Tipo
FROM Fato_locacao l
	JOIN Dim_Carro AS ca ON l.idCarro = ca.idCarro 
	JOIN Dim_Combustivel co ON l.idCombustivel = co.idCombustivel 
GROUP BY l.idCarro, l.idCombustivel

SELECT *
FROM Fato_Locacao
WHERE idCliente = 2