sqlite3 aluguel_carros.db < sql/diagrama_aluguel_logico.sql 
sqlite3 aluguel_carros.db < sql/dados_teste.sql 
python3 -m unittest discover src/tests -v