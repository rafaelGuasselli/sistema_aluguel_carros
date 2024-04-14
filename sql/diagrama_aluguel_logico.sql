DROP TABLE IF EXISTS Clientes;
DROP TABLE IF EXISTS Carros;
DROP TABLE IF EXISTS Funcionarios;

CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf VARCHAR(50) UNIQUE,
    nome VARCHAR(50)
);

CREATE TABLE Carros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cor VARCHAR(50),
    multa INTEGER,
    placa VARCHAR(7) UNIQUE,
	modelo VARCHAR(50),
	taxa_dia INTEGER,
	estimativa_devolucao DATETIME NULL,
    cliente_id INTEGER NULL,
	
	FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

CREATE TABLE Funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf VARCHAR(50) UNIQUE,
    nome VARCHAR(50),
    permissoes INTEGER,
	hash_senha VARCHAR(128)
);
 
--Permissões são um binario de 3 digitos 000
--Ter o primeiro digito igual a um da permissão de criar funcionarios
--Ter o segundo digito igual a um da permissão de criar carros
--Ter o terceiro digito igual a um da permissão de criar Clientes e alugar carros.
--111 = 7 é o maximo de permissões que é dado ao gerente.
INSERT INTO Funcionarios(nome, hash_senha, cpf, permissoes) VALUES (
	'admin', 
	'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', 
	'435.402.600-72',
	7
);

--001 = 1 é o nivel dos atendentes.
INSERT INTO Funcionarios(nome, hash_senha, cpf, permissoes) VALUES (
	'Rafael', 
	'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 
	'366.667.700-21',
	1
);

--Multas são aplicadas caso o carro seja devolvido 1 hora após o esperado.
INSERT INTO Carros(cor, multa, placa, modelo, taxa_dia, estimativa_devolucao) VALUES (
	'Vermelho',
	300,
	'OTM 2X22',
	'Celta',
	500,
	'2021-12-01 14:30:15'
);

INSERT INTO Carros(cor, multa, placa, modelo, taxa_dia, estimativa_devolucao) VALUES (
	'Prata',
	100,
	'RIO2A18',
	'Go',
	200,
	'2021-12-01 14:30:15'
);


INSERT INTO Clientes(cpf, nome) VALUES (
	'000.000.000-00',
	'Rafael'
);


SELECT * FROM Funcionarios;
SELECT * FROM Carros;
SELECT * FROM Clientes;