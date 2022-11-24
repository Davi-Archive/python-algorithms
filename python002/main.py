if __name__ == '__main__':
    produtosDiponiveis = ["Laranja", "Suco", "Carne", "Refrigerante"]
    produto = None
    listaProdutos = []
    try:
        while True:
            produto = input('Digite o produto que deseja: (Digite 0 para finalizar)')

            if produto == '0':
                break

            if produto in produtosDiponiveis:
                listaProdutos.append(produto)
            else:
                print(f"O produto {produto} não está disponivel")

            if not produto == '0':
                listaProdutos.append(produto)

        #produtosDisponiveis.sort()

        print("Produtos Disponiveis")
        print(sorted(produtosDiponiveis))
    except Exception as e:
        #log(e)
        print(e)