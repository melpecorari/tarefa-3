import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("1090x720")
janela.config(bg="LIGHTYELLOW")
janela.option_add("*Font", ("TIMES NEW ROMAN", 100))


tela = tk.Entry(janela, font=("TIMES NEW ROMAN", 40), bd=4, relief="sunken", justify="right")
tela.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def press(tecla):
    texto = tela.get()
    if tecla == '=':
        texto = texto.replace('^', '**')
        caracteres_validos = "0123456789+-*/().c "
        if texto.strip() != "" and all(c in caracteres_validos for c in texto):
            try:
                resultado = str(eval(texto))
            except:
                resultado = "ERROR"
        else:
            resultado = "ERROR"
        tela.delete(0, tk.END)
        tela.insert(0, resultado)
    elif tecla == 'C':
        tela.delete(0, tk.END)
    else:
        tela.insert(tk.END, tecla)


estilo_botao = {
    "width": 15, "height": 2, "fg": "#0b5394", "bg": "WHITE",
    "font": ("Courier New", 20), "relief": "raised", "bd": 6
}


botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('^', 5, 2), ('=', 5, 3)
]

for (texto, linha, coluna) in botoes:
    botao = tk.Button(janela, text=texto, **estilo_botao, command=lambda tecla=texto: press(tecla))
    botao.grid(row=linha, column=coluna, padx=7, pady=7)

botao_limpar = tk.Button(janela, text="Apagar/Zerar", **estilo_botao, command=lambda: tela.delete(0, tk.END))
botao_limpar.grid(row=86, column=0, columnspan=100, padx=7, pady=7)


janela.mainloop()
