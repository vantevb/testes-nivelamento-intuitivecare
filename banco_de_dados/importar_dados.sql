-- Desenvolvido por Nathally V. B. Machado
LOAD DATA INFILE 'operadoras.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\\n'
IGNORE 1 ROWS;
