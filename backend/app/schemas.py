from pydantic import BaseModel

class EmailInput(BaseModel):
    assunto: str
    corpo: str

class EmailResponse(BaseModel):
    categoria: str
    confianca: float
    resposta_sugerida: str
