import tkinter as tk
from tkinter import messagebox

def registrar_candidato():
    candidato = {}
    candidato["nome"] = entry_nome.get()
    candidato["idade"] = int(entry_idade.get())
    candidato["email"] = entry_email.get()
    candidato["telefone"] = entry_telefone.get()
    candidato["nota"] = float(entry_nota.get())
    return candidato

def mostrar_resultado():
    candidato = registrar_candidato()
    nota_ideal = float(entry_nota_ideal.get())
    if candidato["nota"] >= nota_ideal:
        status = "Aprovado"
    else:
        status = "Reprovado"
    
    resultado = f"Candidato: {candidato['nome']}\n" \
                f"Idade: {candidato['idade']}\n" \
                f"Email: {candidato['email']}\n" \
                f"Telefone: {candidato['telefone']}\n" \
                f"Nota: {candidato['nota']}\n" \
                f"Status: {status}"
    
    messagebox.showinfo("Resultado", resultado)

def main():
    global entry_nome, entry_idade, entry_email, entry_telefone, entry_nota, entry_nota_ideal
    
    root = tk.Tk()
    root.title("Registro de Candidato")
    
    tk.Label(root, text="Nome:").grid(row=0, column=0)
    entry_nome = tk.Entry(root)
    entry_nome.grid(row=0, column=1)
    
    tk.Label(root, text="Idade:").grid(row=1, column=0)
    entry_idade = tk.Entry(root)
    entry_idade.grid(row=1, column=1)
    
    tk.Label(root, text="Email:").grid(row=2, column=0)
    entry_email = tk.Entry(root)
    entry_email.grid(row=2, column=1)
    
    tk.Label(root, text="Telefone: (11)").grid(row=3, column=0)
    entry_telefone = tk.Entry(root)
    entry_telefone.grid(row=3, column=1)
    
    tk.Label(root, text="Nota:").grid(row=4, column=0)
    entry_nota = tk.Entry(root)
    entry_nota.grid(row=4, column=1)
    
    tk.Label(root, text="Nota de Corte:").grid(row=5, column=0)
    entry_nota_ideal = tk.Entry(root)
    entry_nota_ideal.grid(row=5, column=1)
    
    tk.Button(root, text="Registrar e Mostrar Resultado", command=mostrar_resultado).grid(row=6, column=0, columnspan=2)
    
    root.mainloop()

if __name__ == "__main__":
    main()