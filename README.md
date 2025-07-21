 MVP Auto

## Sobre o projeto

Este projeto realiza a extração de texto de arquivos PDF utilizando OCR (Tesseract) e classifica processos jurídicos com auxílio de IA (Groq/OpenAI).

## Como implementar e usar

### 1. Instale as bibliotecas necessárias

No terminal, execute:

```bash
pip install -r requirements.txt
```

### 2. Baixe e configure o Tesseract OCR

- Faça download do instalador em:  
    [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Instale normalmente no Windows.
- Certifique-se de que o executável está em:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

#### Adicione o idioma português

- Baixe o arquivo `por.traineddata` em:  
    [https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata](https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata)
- Coloque o arquivo em:

```text
C:\Program Files\Tesseract-OCR\tessdata
```

### 3. Obtenha uma chave de API Groq

- Crie uma conta e gere sua chave em:  
    [https://console.groq.com/keys](https://console.groq.com/keys)

### 4. Configure a chave de API como variável de ambiente

No terminal (Windows), execute:

```cmd
set GROQ_API_KEY=sua_chave_aqui
```

Ou substitua sua chave diretamente em `GROQ_API_KEY` no arquivo `processamento.py`.

### 5. Execute o projeto

No terminal, rode:

```bash
python main.py
```

Uma interface gráfica será aberta para upload de arquivos PDF. O texto será extraído e classificado automaticamente.

---

## Observações

- Não compartilhe sua chave de API publicamente.
- O projeto depende do Tesseract configurado corretamente e do idioma português instalado.
- O modelo utilizado é `llama3-70b-8192` via Groq API.

---