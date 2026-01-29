from transformers import pipeline

LABELS = ["Produtivo", "Improdutivo"]

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def classify_email(text: str):
    result = classifier(text, LABELS)

    return {
        "categoria": result["labels"][0],
        "confianca": round(result["scores"][0], 3)
    }
