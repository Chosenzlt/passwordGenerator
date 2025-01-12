import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog

# Função para calcular a força da senha
def avaliar_forca(senha):
    if len(senha) < 8:
        return "Fraca"
    elif len(senha) < 12:
        return "Média"
    else:
        tem_maiusculas = any(c.isupper() for c in senha)
        tem_numeros = any(c.isdigit() for c in senha)
        tem_simbolos = any(c in string.punctuation for c in senha)

        if tem_maiusculas and tem_numeros and tem_simbolos:
            return "Forte"
        else:
            return "Média"

# Função para gerar senha
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError

        incluir_maiusculas = var_maiusculas.get()
        incluir_numeros = var_numeros.get()
        incluir_simbolos = var_simbolos.get()

        caracteres = string.ascii_lowercase
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_simbolos:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError("Nenhum conjunto de caracteres selecionado.")

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)

        # Avaliar a força da senha
        forca = avaliar_forca(senha)
        label_forca.config(text=f"Força da senha: {forca}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o tamanho da senha.")

# Função para salvar senha em um arquivo
def salvar_senha():
    senha = entry_senha.get()
    if not senha:
        messagebox.showwarning("Aviso", "Nenhuma senha para salvar.")
        return

    arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")],
        title="Salvar Senha"
    )
    if arquivo:
        with open(arquivo, "w") as file:
            file.write(senha)
        messagebox.showinfo("Sucesso", f"Senha salva em {arquivo}")

# Interface Gráfica
root = tk.Tk()
root.title("Gerador de Senhas Avançado")

# Tamanho da senha
frame_tamanho = tk.Frame(root)
frame_tamanho.pack(pady=10)
tk.Label(frame_tamanho, text="Tamanho da senha:").pack(side=tk.LEFT)
entry_tamanho = tk.Entry(frame_tamanho, width=5)
entry_tamanho.pack(side=tk.LEFT)

# Opções
frame_opcoes = tk.Frame(root)
frame_opcoes.pack(pady=10)

var_maiusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

tk.Checkbutton(frame_opcoes, text="Incluir Maiúsculas", variable=var_maiusculas).pack(anchor="w")
tk.Checkbutton(frame_opcoes, text="Incluir Números", variable=var_numeros).pack(anchor="w")
tk.Checkbutton(frame_opcoes, text="Incluir Símbolos", variable=var_simbolos).pack(anchor="w")

# Botão para gerar senha
btn_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
btn_gerar.pack(pady=10)

# Campo para exibir a senha gerada
entry_senha = tk.Entry(root, width=40, font=("Helvetica", 14), justify="center")
entry_senha.pack(pady=10)

# Força da senha
label_forca = tk.Label(root, text="Força da senha: ")
label_forca.pack(pady=5)

# Botão para salvar senha
btn_salvar = tk.Button(root, text="Salvar Senha", command=salvar_senha)
btn_salvar.pack(pady=10)

# Rodar a aplicação
root.mainloop()
