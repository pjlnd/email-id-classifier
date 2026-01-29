from fastapi import FastAPI
from app.schemas import EmailInput, EmailResponse
from app.nlp.preprocess import preprocess
from app.nlp.classifier import classify_email
from app.nlp.response_generator import generate_response

app = FastAPI(title="Email Classifier API")

@app.post("/classificar-email", response_model=EmailResponse)
def classificar_email(email: EmailInput):
    raw_text = f"{email.assunto} {email.corpo}"

    processed_text = preprocess(raw_text)
    classification = classify_email(processed_text)
    resposta = generate_response(
        classification["categoria"],
        raw_text
    )

    return {
        "categoria": classification["categoria"],
        "confianca": classification["confianca"],
        "resposta_sugerida": resposta
    }
