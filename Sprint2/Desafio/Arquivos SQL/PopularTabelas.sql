-- Script que pega os dados da tabela tb_locacao e popula o BD após a normalização

--         Popular Cliente
INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(2, 'Cliente dois', 'São Paulo', 'São Paulo', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(3, 'Cliente tres', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(4, 'Cliente quatro', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(6, 'Cliente seis', 'Belo Horizonte', 'Minas Gerais', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(10, 'Cliente dez', 'Rio Branco', 'Acre', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(20, 'Cliente vinte', 'Macapá', 'Amapá', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(22, 'Cliente vinte e dois', 'Porto Alegre', 'Rio Grande do Sul', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(23, 'Cliente vinte e tres', 'Eusébio', 'Ceará', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(5, 'Cliente cinco', 'Manaus', 'Amazonas', 'Brasil');

INSERT INTO Cliente
(id, nome, cidade, estado, pais)
VALUES(26, 'Cliente vinte e seis', 'Campo Grande', 'Mato Grosso do Sul', 'Brasil');


--         Popular Vendedor
INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(5, 'Vendedor cinco', 0, 'São Paulo');

INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(6, 'Vendedora seis', 1, 'São Paulo');

INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(7, 'Vendedora sete', 1, 'Rio de Janeiro');

INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(8, 'Vendedora oito', 1, 'Minas Gerais');

INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(16, 'Vendedor dezesseis', 0, 'Amazonas');

INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(30, 'Vendedor trinta', 0, 'Rio Grande do Sul');

INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(31, 'Vendedor trinta e um', 0, 'Ceará');

INSERT INTO Vendedor
(id, nome, sexo, estado)
VALUES(32, 'Vendedora trinta e dois', 1, 'Mato Grosso do Sul');


--         Popular Carro
INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(98, 'AKJHKN98JY76539', 'Fiat', 'Fiat Uno', 2000, 1);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(99, 'IKJHKN98JY76539', 'Fiat', 'Fiat Palio', 2010, 1);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(3, 'DKSHKNS8JS76S39', 'VW', 'Fusca 78', 1978, 1);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(10, 'LKIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996, 1);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(7, 'SSIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996, 1);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(6, 'SKIUNS8JS76S39', 'Nissan', 'Versa', 2019, 1);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(2, 'AKIUNS1JS76S39', 'Nissan', 'Versa', 2019, 2);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(4, 'LLLUNS1JS76S39', 'Nissan', 'Versa', 2020, 2);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(1, 'AAAKNS8JS76S39', 'Toyota', 'Corolla XEI', 2023, 3);

INSERT INTO Carro
(id, classi, marca, modelo, ano, idcombustivel)
VALUES(5, 'MSLUNS1JS76S39', 'Nissan', 'Frontier', 2022, 4);


--         Popular Combustivel
INSERT INTO Combustivel
(id, tipo)
VALUES(1, 'Gasolina');
INSERT INTO Combustivel
(id, tipo)
VALUES(2, 'Etanol');
INSERT INTO Combustivel
(id, tipo)
VALUES(3, 'Flex');
INSERT INTO Combustivel
(id, tipo)
VALUES(4, 'Diesel');


--         Popular Locacao
INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(1, 2, 98, 5, '20150110', '10:00', 2, 100, '20150112', '10:00', 25412);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(2, 2, 98, 5, '20150210', '12:00', 2, 100, '20150212', '12:00', 29450);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(3, 3, 99, 6, '20150213', '12:00', 2, 150, '20150215', '12:00', 20000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(4, 4, 99, 6, '20150215', '13:00', 5, 150, '20150220', '13:00', 21000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(5, 4, 99, 7, '20150302', '14:00', 5, 150, '20150307', '14:00', 21700);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(6, 6, 3, 8, '20160302', '14:00', 10, 250, '20160312', '14:00', 121700);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(7, 6, 3, 8, '20160802', '14:00', 10, 250, '20160812', '14:00', 131800);
INSERT INTO Locacao

(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(8, 4, 3, 6, '20170102', '18:00', 10, 250, '20170112', '18:00', 151800);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(9, 4, 3, 6, '20180102', '18:00', 10, 280, '20180112', '18:00', 152800);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(10, 10, 10, 16, '20180302', '18:00', 10, 50, '20180312', '18:00', 211800);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(11, 20, 7, 16, '20180401', '11:00', 10, 50, '20180411', '11:00', 212800);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(12, 20, 6, 16, '20200401', '11:00', 10, 150, '20200411', '11:00', 21800);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(13, 22, 2, 30, '20220501', '8:00', 20, 150, '20220521', '18:00', 10000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(14, 22, 2, 30, '20220601', '8:00', 20, 150, '20220621', '18:00', 20000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(15, 22, 2, 30, '20220701', '8:00', 20, 150, '20220721', '18:00', 30000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(16, 22, 2, 30, '20220801', '8:00', 20, 150, '20220721', '18:00', 40000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(17, 23, 4, 31, '20220901', '8:00', 20, 150, '20220921', '18:00', 55000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(18, 23, 4, 31, '20221001', '8:00', 20, 150, '20221021', '18:00', 56000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(19, 23, 4, 31, '20221101', '8:00', 20, 150, '20221121', '18:00', 58000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(20, 5, 1, 16, '20230102', '18:00', 10, 880, '20230112', '18:00', 1800);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(21, 5, 1, 16, '20230115', '18:00', 10, 880, '20230125', '18:00', 8500);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(22, 26, 5, 32, '20230125', '8:00', 5, 600, '20230130', '18:00', 28000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(23, 26, 5, 32, '20230131', '8:00', 5, 600, '20230205', '18:00', 38000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(24, 26, 5, 32, '20230206', '8:00', 5, 600, '20230211', '18:00', 48000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(25, 26, 5, 32, '20230212', '8:00', 5, 600, '20230217', '18:00', 68000);

INSERT INTO Locacao
(id, idCliente, idCarro, idVendedor, "data", hora, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, kmCarro)
VALUES(26, 26, 5, 32, '20230218', '8:00', 1, 600, '20230219', '18:00', 78000);