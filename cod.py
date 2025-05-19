from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, messagebox

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Categoria: {self.categoria.nome}"

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        base_info = super().getInformacoes()
        return f"{base_info}, Potência da Fonte: {self._potenciaDaFonte}"

    def cadastrar(self):
        return f"Desktop cadastrado: {self.getInformacoes()}"

    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte

    def setPotenciaDaFonte(self, valor):
        self._potenciaDaFonte = valor

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        base_info = super().getInformacoes()
        return f"{base_info}, Tempo de Bateria: {self.__tempoDeBateria} horas"

    def cadastrar(self):
        return f"Notebook cadastrado: {self.getInformacoes()}"

    def getTempoDeBateria(self):
        return self.__tempoDeBateria

    def setTempoDeBateria(self, valor):
        self.__tempoDeBateria = valor

def cadastrar_produto():
    categoria = Categoria(1, categoria_var.get())
    modelo = modelo_entry.get()
    cor = cor_entry.get()
    preco = preco_entry.get()

    if tipo_var.get() == "Desktop":
        potencia = extra_entry.get()
        desktop = Desktop(modelo, cor, preco, categoria, potencia)
        resultado = desktop.cadastrar()
    else:
        tempo = extra_entry.get()
        notebook = Notebook(modelo, cor, preco, categoria, tempo)
        resultado = notebook.cadastrar()

    messagebox.showinfo("Cadastro realizado", resultado)

janela = tk.Tk()
janela.title("Cadastro de Produtos")

tk.Label(janela, text="Tipo de Produto:").grid(row=0, column=0)
tipo_var = tk.StringVar(value="Desktop")
ttk.Combobox(janela, textvariable=tipo_var, values=["Desktop", "Notebook"]).grid(row=0, column=1)

tk.Label(janela, text="Modelo:").grid(row=1, column=0)
modelo_entry = tk.Entry(janela)
modelo_entry.grid(row=1, column=1)

tk.Label(janela, text="Cor:").grid(row=2, column=0)
cor_entry = tk.Entry(janela)
cor_entry.grid(row=2, column=1)

tk.Label(janela, text="Preço:").grid(row=3, column=0)
preco_entry = tk.Entry(janela)
preco_entry.grid(row=3, column=1)

tk.Label(janela, text="Categoria:").grid(row=4, column=0)
categoria_var = tk.StringVar()
categoria_entry = tk.Entry(janela, textvariable=categoria_var)
categoria_entry.grid(row=4, column=1)

tk.Label(janela, text="Potência da Fonte / Tempo de Bateria:").grid(row=5, column=0)
extra_entry = tk.Entry(janela)
extra_entry.grid(row=5, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_produto).grid(row=6, column=0, columnspan=2)

janela.mainloop()
