-- Desenvolvido por Nathally V. B. Machado
SELECT nome_fantasia, SUM(valor) as total
FROM despesas
WHERE tipo_despesa = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND trimestre = 'último'
GROUP BY nome_fantasia
ORDER BY total DESC
LIMIT 10;
