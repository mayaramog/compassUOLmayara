CREATE TABLE Cliente 
( 
 id INT PRIMARY KEY,  
 nome VARCHAR(100) NOT NULL,  
 cidade VARCHAR(40) NOT NULL,  
 estado VARCHAR(40) NOT NULL,  
 pais VARCHAR(40) NOT NULL DEFAULT 'Brasil'
)

CREATE TABLE Combustivel 
( 
 id INT PRIMARY KEY,  
 tipo VARCHAR(20) NOT NULL  
)

CREATE TABLE Carro 
( 
 id INT PRIMARY KEY, 
 classi VARCHAR(50) NOT NULL UNIQUE,  
 marca VARCHAR(80) NOT NULL,  
 modelo VARCHAR(80) NOT NULL,  
 ano INT NOT NULL,  
 idCombustivel INT NOT NULL, 
 
 FOREIGN KEY (idCombustivel) REFERENCES Combustivel (id)
)

CREATE TABLE Vendedor 
( 
 id INT PRIMARY KEY,  
 nome VARCHAR(15) NOT NULL,  
 sexo SMALLINT CHECK (sexo IN (0, 1)),
 estado VARCHAR(40) NOT NULL  
)

CREATE TABLE Locacao 
( 
 id INTEGER PRIMARY KEY AUTOINCREMENT,  
 idCliente INT NOT NULL,  
 idCarro INT NOT NULL,  
 idVendedor INT NOT NULL, 
 kmCarro INT NOT NULL DEFAULT 0,
 data DATE NOT NULL DEFAULT (DATE('now')),  
 hora TIME NOT NULL DEFAULT (TIME('now')),  
 qtdDiaria INT NOT NULL,  
 vlrDiaria DECIMAL(18, 2) NOT NULL,  
 dataEntrega DATE NOT NULL,
 horaEntrega TIME NOT NULL,
 
 FOREIGN KEY (idCliente) REFERENCES Cliente (id),
 FOREIGN KEY (idCarro) REFERENCES Carro (id),
 FOREIGN KEY (idVendedor) REFERENCES Vendedor (id)
)