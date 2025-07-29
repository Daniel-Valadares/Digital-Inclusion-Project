import os
from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Caminho absoluto do diretório onde o app.py está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dados")
def dados():
    try:
        caminho_csv = os.path.join(BASE_DIR, "dados_com_coordenadas.csv")
        df = pd.read_csv(caminho_csv)

        # Corrigir nomes de colunas para JS
        df.columns = (
            df.columns.str.strip()
                      .str.replace(" ", "_")
                      .str.replace("/", "_")
                      .str.lower()
        )

        registros = df.to_dict(orient="records")
        return jsonify(registros)
    except Exception as e:
        return f"Erro ao carregar CSV: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
