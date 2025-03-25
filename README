# Testes de Nivelamento – IntuitiveCare

## 📁 Estrutura e Instruções

### `web_scraping/`
> **Objetivo:** Acessar o site da ANS, baixar os Anexos I e II em PDF e compactá-los.

**Como executar:**
```bash
python download_anexos.py
```
O script fará o download dos dois arquivos PDF e criará um arquivo `anexos_compactados.zip`.

---

### `transformacao_dados/`
> **Objetivo:** Extrair a tabela do Anexo I (PDF), exportar para CSV, substituir siglas e compactar.

**Como executar:**
```bash
python extrair_dados_pdf.py
```
Gera um arquivo `Teste_Nathally V B Machado.csv` e o compacta em `Teste_Nathally V B Machado.zip`.

---

### `banco_de_dados/`
> **Objetivo:** Criar tabelas SQL, importar dados da ANS e realizar análises.

**Arquivos principais:**
- `criar_tabelas.sql` – estrutura das tabelas
- `importar_dados.sql` – comandos para importar arquivos CSV
- `analise_despesas.sql` – queries analíticas solicitadas

Use o banco de dados MySQL 8+ ou PostgreSQL 10+.

---

### `api_vue/backend/`
> **Objetivo:** API em Python (Flask) para busca textual de operadoras.

**Como executar:**
```bash
pip install -r requirements.txt
python app.py
```

---

### `api_vue/frontend/`
> **Objetivo:** Interface web construída em Vue.js para consumir a API.

**Como executar:**
```bash
npm install
npm run serve
```

---

### `postman_collection.json`
> Coleção de testes no Postman para demonstrar a funcionalidade da API.

---

### `requirements.txt`
> Lista de bibliotecas Python usadas nos testes.

---

## 🧠 Observações
- O projeto foi estruturado pensando em clareza, organização e práticas reais do mercado.
- Todos os scripts foram desenvolvidos com base nos critérios do desafio proposto pela IntuitiveCare.
