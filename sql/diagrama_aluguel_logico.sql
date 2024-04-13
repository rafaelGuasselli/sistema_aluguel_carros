DROP TABLE IF EXISTS Usuarios;
DROP TABLE IF EXISTS Carros;
DROP TABLE IF EXISTS Funcionarios;

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf VARCHAR(50) UNIQUE,
    nome VARCHAR(50)
);

CREATE TABLE Carros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    taxa_dia Numero,
    taxa_hora Numero,
    placa Texto(7),
    multa Numero,
    cor Texto,
    fk_Usuario_id INTEGER,
	
	FOREIGN KEY (fk_Usuario_id) REFERENCES Carros(id)
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
--Ter o terceiro digito igual a um da permissão de criar usuarios e alugar carros.
--111 = 7 é o maximo de permissões que é dado ao gerente.
INSERT INTO Funcionarios(nome, hash_senha, cpf, permissoes) VALUES (
	'admin', 
	'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', 
	'435.402.600-72',
	7
);

--001 = 1 é o nivel dos atendentes.
INSERT INTO Funcionarios(nome, hash_senha, cpf) VALUES (
	'Rafael', 
	'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 
	'366.667.700-21',
	1
);

SELECT * FROM Funcionarios;