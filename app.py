from flask import Flask, request, jsonify
import pdfplumber
import joblib

pipeline = joblib.load("pipeline_xgboost.pkl")

app = Flask(__name__)

def pdf_para_texto(file):
    texto = ""
    with pdfplumber.open(file) as pdf:
        for pagina in pdf.pages:
            page_text = pagina.extract_text()
            if page_text:
                texto += page_text + "\n"
    return texto

@app.route("/")
def home():
    return jsonify({
        "status": "API funcionando!",
        "endpoint": "/predict"
    })

@app.route("/exemplo", methods=["GET"])
def exemplo():
    return {
        "exemplo_json": {
            "texto": "Python developer with experience in ML"
        },
        "uso": "Envie um POST para /predict com o campo 'texto'."
    }


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "texto" not in data:
        return jsonify({"erro": "Envie o campo 'texto' no JSON."}), 400

    texto = data["texto"]
    pred = pipeline.predict([texto])[0]

    nivel = (
        "Baixa compatibilidade" if pred <= 0.50 else
        "Media compatibilidade" if pred <= 0.75 else
        "Alta compatibilidade"
    )

    return jsonify({
        "matched_score_previsto": float(pred),
        "nivel": nivel
    })

@app.route("/predict_pdf", methods=["POST"])
def predict_pdf():
    if "file" not in request.files:
        return jsonify({"erro": "Envie um arquivo PDF no campo 'file'."}), 400

    pdf_file = request.files["file"]

    try:
        texto = pdf_para_texto(pdf_file)
    except Exception as e:
        return jsonify({"erro": f"Erro ao ler PDF: {str(e)}"}), 500

    pred = pipeline.predict([texto])[0]

    nivel = (
        "Baixa compatibilidade" if pred <= 0.50 else
        "Media compatibilidade" if pred <= 0.75 else
        "Alta compatibilidade"
    )

    return jsonify({
        "matched_score_previsto": float(pred),
        "nivel": nivel
    })



if __name__ == "__main__":
    app.run(debug=True)
