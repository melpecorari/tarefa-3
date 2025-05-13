import tkinter as tk

def obter_valores():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        return n1, n2
    except ValueError:
        resultado_label.config(text="Erro: valores inválidos.")
        return None, None

def somar():
    n1, n2 = obter_valores()
    if n1 is not None:
        resultado = n1 + n2
        resultado_label.config(text=f"Resultado: {resultado}")

def subtrair():
    n1, n2 = obter_valores()
    if n1 is not None:
        resultado = n1 - n2
        resultado_label.config(text=f"Resultado: {resultado}")

def multiplicar():
    n1, n2 = obter_valores()
    if n1 is not None:
        resultado = n1 * n2
        resultado_label.config(text=f"Resultado: {resultado}")

def dividir():
    n1, n2 = obter_valores()
    if n1 is not None:
        if n2 == 0:
            resultado_label.config(text="Erro: divisão por zero.")
        else:
            resultado = n1 / n2
            resultado_label.config(text=f"Resultado: {resultado}")

def zerar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado_label.config(text="Resultado: ")


janela = tk.Tk()
janela.title("calculadora")
janela.geometry("400x400")
janela.config(bg="lightblue")

tk.Label(janela, text="Adicione o valor 1:", bg="white", font=("Arial", 12)).pack(pady=5)
entrada1 = tk.Entry(janela, font=("Arial", 14))
entrada1.pack()

tk.Label(janela, text="Adicione o valor 2:", bg="white", font=("Arial", 12)).pack(pady=5)
entrada2 = tk.Entry(janela, font=("Arial", 14))
entrada2.pack()

frame_botoes = tk.Frame(janela, bg="lightblue")
frame_botoes.pack(pady=20)

tk.Button(frame_botoes, text="+", command=somar, width=5,  font=("Arial", 12)).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="-", command=subtrair, width=5, font=("Arial", 12)).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="*", command=multiplicar, width=5,  font=("Arial", 12)).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="/", command=dividir, width=5, font=("Arial", 12)).grid(row=0, column=3, padx=5)
tk.Button(frame_botoes, text="Zerar/Apagar", command=zerar, width=15, font=("Arial", 12)).grid(row=1, column=0, columnspan=4, pady=15)

resultado_label = tk.Label(janela, text="Resultado: ", font=("Arial", 16), bg="white")
resultado_label.pack(pady=10)


janela.mainloop()
