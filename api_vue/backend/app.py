# Desenvolvido por Nathally V. B. Machado para o processo seletivo da IntuitiveCare

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carrega o CSV com dados de operadoras
df = pd.read_csv("operadoras.csv")  # Certifique-se de que esse arquivo esteja presente na mesma pasta

@app.route("/buscar")
def buscar():
    termo = request.args.get("q", "").lower()
    resultados = df[df["nome_fantasia"].str.lower().str.contains(termo)]
    return jsonify(resultados.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
