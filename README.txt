
-----------------------------------------------------
TALENTMATCH – GLOBAL SOLUTION 2025 (FIAP)
-----------------------------------------------------

Integrantes:
- Ana Freitas – RM565559
- Luis Borges - RM566548

Disciplina: ARTIFICIAL INTELLIGENCE & CHATBOT
Professor: Daniel Soria
Entrega: CRISP-DM + Modelo de Machine Learning + API Flask

-----------------------------------------------------
Descrição do Projeto
-----------------------------------------------------

Este projeto implementa um sistema de análise automática de compatibilidade entre
currículos e vagas, utilizando técnicas de Machine Learning e Processos de Data Mining
seguindo a metodologia CRISP-DM.

O modelo final foi desenvolvido com:
- TF-IDF para vetorização de texto
- XGBoost Regressor para previsão de compatibilidade (score contínuo)
- Pipeline integrado e salvo como .pkl com joblib
- API REST em Flask permitindo predição via:
  - Texto enviado em JSON (/predict)
  - Arquivo PDF enviado via multipart form (/predict_pdf)

Foram incluídos:
- Notebook CRISP-DM completo, com todas as etapas documentadas
- Código da API Flask
- Pipeline salvo para deploy
- requirements.txt com todas as dependências utilizadas

-----------------------------------------------------
Como testar a API
-----------------------------------------------------

1. Rodar a API:
   python3 app.py

2. Testar com JSON:
   curl -X POST http://127.0.0.1:5000/predict \
        -H "Content-Type: application/json" \
        -d '{"texto":"Python developer with ML experience"}'

3. Testar com PDF:
   curl -X POST http://127.0.0.1:5000/predict_pdf \
        -F "file=@curriculos/curriculo_ana.pdf"

-----------------------------------------------------
Observações
-----------------------------------------------------
- Todos os arquivos necessários para execução estão incluídos.
- O projeto pode ser executado em qualquer ambiente com Python 3.11.
- O pipeline .pkl contém todo o pré-processamento e o modelo final.

-----------------------------------------------------
FIM DO ARQUIVO
-----------------------------------------------------


