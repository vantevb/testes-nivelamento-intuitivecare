# Desenvolvido por Nathally V. B. Machado para o processo seletivo da IntuitiveCare

import pdfplumber
import pandas as pd
from zipfile import ZipFile

# Lista para armazenar as tabelas extraídas
tabelas = []

# Caminho para o PDF do Anexo I
caminho_pdf = "../web_scraping/pdfs/AnexoI.pdf"  # Certifique-se que esse caminho existe localmente

with pdfplumber.open(caminho_pdf) as pdf:
    for page in pdf.pages:
        try:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                tabelas.append(df)
        except:
            continue

# Concatenar todas as tabelas
df_final = pd.concat(tabelas, ignore_index=True)

# Substituições conforme legenda
df_final["OD"] = df_final["OD"].replace("S", "Consulta Odontológica")
df_final["AMB"] = df_final["AMB"].replace("S", "Ambulatorial")

# Exportar para CSV
nome_csv = "Teste_Nathally V B Machado.csv"
df_final.to_csv(nome_csv, index=False)

# Compactar o CSV
with ZipFile("Teste_Nathally V B Machado.zip", "w") as zipf:
    zipf.write(nome_csv)
