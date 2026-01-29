from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_response(category: str, email_text: str) -> str:
    if category == "Produtivo":
        prompt = (
            "Responda em português.\n"
            "Escreva uma única resposta curta, educada e profissional.\n"
            "Não repita o texto do email.\n\n"
            f"Email: {email_text}\n"
            "Resposta:"
    )
    else:
        prompt = (
            "Responda em português.\n"
            "Escreva uma única resposta curta de agradecimento.\n"
            "Não repita o texto do email.\n\n"
            f"Email: {email_text}\n"
            "Resposta:"
    )


    result = generator(
        prompt,
    max_new_tokens=60,
    do_sample=True,
    temperature=0.5,
    top_p=0.85,
    repetition_penalty=1.3,
    pad_token_id=50256
    )

    texto = result[0]["generated_text"]

    resposta = texto.split("Resposta:")[-1].strip()

    return resposta

