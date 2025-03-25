# Desenvolvido por Nathally V. B. Machado para o processo seletivo da IntuitiveCare

import requests
from bs4 import BeautifulSoup
import os
from zipfile import ZipFile

def baixar_pdfs():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Criar pasta para armazenar os PDFs
    os.makedirs('pdfs', exist_ok=True)
    
    # Buscar links dos anexos
    pdf_links = [link['href'] for link in soup.find_all('a', href=True) if 'Anexo' in link['href'] and link['href'].endswith('.pdf')]
    
    baixados = []
    for link in pdf_links[:2]:
        nome = link.split("/")[-1]
        r = requests.get(link)
        path = os.path.join("pdfs", nome)
        with open(path, "wb") as f:
            f.write(r.content)
        baixados.append(path)

    # Compactar os arquivos baixados
    with ZipFile("anexos_compactados.zip", "w") as zipf:
        for file in baixados:
            zipf.write(file, arcname=os.path.basename(file))

if __name__ == "__main__":
    baixar_pdfs()
