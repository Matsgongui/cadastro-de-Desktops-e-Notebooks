# 💻 Cadastro de Produtos: Desktops e Notebooks

Este projeto em Python implementa um sistema orientado a objetos com interface gráfica para cadastro de Desktops e Notebooks. Ele utiliza conceitos como herança, encapsulamento , classes abstratas e polimorfismo.

---

## 📚 Estrutura do Projeto

### Classes:

- `Categoria`: Representa uma categoria com `id` e `nome`.
- `Produto` (abstrata): Superclasse de `Desktop` e `Notebook`, com atributos como `modelo`, `cor`, `preço`, `categoria`, além de:
  - Método abstrato `cadastrar()`
  - Método `getInformacoes()`
- `Desktop`: Herda de `Produto`, possui atributo **fracamente privado** `potenciaDaFonte`. Reimplementa `getInformacoes()`.
- `Notebook`: Herda de `Produto`, possui atributo **fortemente privado** `tempoDeBateria`. Reimplementa `getInformacoes()`.

---

## 🖼️ Interface Gráfica

Desenvolvida com a biblioteca `tkinter`, a interface permite ao usuário:

- Selecionar o tipo de produto (Desktop ou Notebook)
- Preencher os dados do produto (modelo, cor, preço, categoria)
- Informar a potência da fonte (para Desktops) ou tempo de bateria (para Notebooks)
- Cadastrar o produto e visualizar os dados em uma janela de confirmação
