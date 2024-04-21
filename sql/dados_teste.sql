--Permissões são um binario de 3 digitos 000
--Ter o primeiro digito igual a um da permissão de alterar Funcionarios
--Ter o segundo digito igual a um da permissão de alterar Carros
--Ter o terceiro digito igual a um da permissão de alterar Clientes
--111 = 7 é o maximo de permissões que é dado ao gerente.
--Senha = admin
INSERT INTO Funcionarios(nome, hash_senha, cpf, permissoes) VALUES (
	'admin', 
	'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', 
	'435.402.600-72',
	7
);

INSERT INTO Cache(funcionario_atual) VALUES(1);

--011 = 3 é o nivel dos atendentes.
--Senha = 12345
INSERT INTO Funcionarios(nome, hash_senha, cpf, permissoes) VALUES (
	'Teste cliente e carros', 
	'3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 
	'a',
	3
);

INSERT INTO Funcionarios(nome, hash_senha, cpf, permissoes) VALUES (
	'Teste só cliente', 
	'3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 
	'366.667.700-20',
	1
);

INSERT INTO Funcionarios(nome, hash_senha, cpf, permissoes) VALUES (
	'Teste sem nenhuma permissão', 
	'3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 
	'366.667.700-19',
	0
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