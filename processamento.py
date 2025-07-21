import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
from openai import OpenAI

# Certifique-se de que o caminho do Tesseract está correto para o seu sistema
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Cria o cliente da nova API
client = OpenAI(api_key="GROQ_API_KEY",
                 base_url="https://api.groq.com/openai/v1"
                 )

def extrair_texto_pdf_ocr(caminho_pdf):
    texto = ''
    doc = fitz.open(caminho_pdf)
    for pagina in doc:
        # Renderiza página como imagem
        pix = pagina.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        # Passa a imagem no Tesseract OCR
        texto_pagina = pytesseract.image_to_string(img, lang='por')
        texto += texto_pagina + '\n'
    return texto

def classificar_processo(caminho_pdf):
    texto_pdf = extrair_texto_pdf_ocr(caminho_pdf)

    prompt = f"""
Você é um assistente jurídico. Analise o texto a seguir e extraia as seguintes informações:

- Número do processo
- Nome do autor
- Nome do réu
- Data de ajuizamento
- Tribunal onde o processo está tramitando
- Vara onde o processo está tramitando
- Assunto principal
- Valor da causa (se houver)

Texto:
\"\"\"{texto_pdf}\"\"\"

Responda em formato JSON.
"""

    resposta = client.chat.completions.create(
        #se você tiver acesso ao modelo GPT-4, use-o aqui
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    resultado = resposta.choices[0].message.content
    print("📋 Resposta do modelo:\n", resultado)
    return resultado
