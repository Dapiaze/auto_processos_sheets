import tkinter as tk
from processamento import classificar_processo
from tkinter import filedialog, messagebox

def upload_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("PDF Files", "*.pdf"), ("Todos os arquivos", "*.*")]
    )
    if arquivo:
        messagebox.showinfo("Upload feito", f"Arquivo selecionado:\n{arquivo}")
        # Processamento de dados:
        classificar_processo(arquivo);

# Criando a janela principal
janela = tk.Tk()
janela.title("Upload de Documento")
janela.geometry("400x200")

# Botão de upload
botao = tk.Button(janela, text="📤 Fazer Upload de Arquivo", command=upload_arquivo, font=("Arial", 14), bg="#4CAF50", fg="white")
botao.pack(pady=60)

# Iniciar a interface
janela.mainloop()