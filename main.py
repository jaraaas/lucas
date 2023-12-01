  import random

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.numero_serie = None

    def gerar_numero_serie(self):
        pass

    def imprimir_info(self):
        print(f"{self.nome} - Preço: R${self.preco:.2f} - Número de Série: {self.numero_serie}")


class Camisa(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def gerar_numero_serie(self):
        self.numero_serie = random.choice(range(5, 100, 5))


class Caneca(Produto):
    def __init__(self, nome, preco, capacidade):
        super().__init__(nome, preco)
        self.capacidade = capacidade

    def gerar_numero_serie(self):
        self.numero_serie = random.choice(range(3, 100, 3))


class Quadrinho(Produto):
    def __init__(self, nome, preco, autor, editora):
        super().__init__(nome, preco)
        self.autor = autor
        self.editora = editora

    def gerar_numero_serie(self):
        self.numero_serie = random.choice(range(7, 100, 7))


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        for _ in range(quantidade):
            if produto.preco >= 0:
                produto.gerar_numero_serie()
                self.produtos.append(produto)
            else:
                print(f"Preço do produto {produto.nome} não pode ser negativo.")
                return False

    def remover_produto(self, produto, quantidade):
        for _ in range(quantidade):
            self.produtos.remove(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)

    def aplicar_descontos(self):
        # Aplicar desconto de caneca a cada 4 camisas
        camisas = [produto for produto in self.produtos if isinstance(produto, Camisa)]
        if len(camisas) >= 4:
            canecas_brinde = min(len(camisas) // 4, [produto for produto in self.produtos if isinstance(produto, Caneca)].count())
            for _ in range(canecas_brinde):
                caneca = next((produto for produto in self.produtos if isinstance(produto, Caneca)), None)
                if caneca:
                    self.produtos.remove(caneca)

        # Aplicar desconto de quadrinho a cada 5 quadrinhos
        quadrinhos = [produto for produto in self.produtos if isinstance(produto, Quadrinho)]
        if len(quadrinhos) >= 5:
            quadrinhos.sort(key=lambda x: x.preco)
            for i in range(min(len(quadrinhos) // 5, len(quadrinhos))):
                self.produtos.remove(quadrinhos[i])

    def finalizar_compra(self):
        self.aplicar_descontos()
        self.produtos.sort(key=lambda x: x.preco)
        for produto in self.produtos:
            produto.imprimir_info()

        print(f"\nTotal da Compra: R${self.calcular_total():.2f}")


# Função principal
def main():
    carrinho = Carrinho()

    while True:
        print("\nOpções:")
        print("1 - Adicionar Camisa")
        print("2 - Adicionar Caneca")
        print("3 - Adicionar Quadrinho")
        print("4 - Remover Produto")
        print("5 - Finalizar Compra")

        try:
            opcao = int(input("Escolha uma opção (1-5): "))
        except ValueError:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")
            continue

        if opcao == 1:
            nome = input("Nome da Camisa: ")
            preco = float(input("Preço da Camisa: "))
            tamanho = input("Tamanho da Camisa (P, M, G): ")
            quantidade = int(input("Quantidade: "))
            camisa = Camisa(nome, preco, tamanho)
            carrinho.adicionar_produto(camisa, quantidade)

        elif opcao == 2:
            nome = input("Nome da Caneca: ")
            preco = float(input("Preço da Caneca: "))
            capacidade = float(input("Capacidade da Caneca em litros: "))
            quantidade = int(input("Quantidade: "))
            caneca = Caneca(nome, preco, capacidade)
            carrinho.adicionar_produto(caneca, quantidade)

        elif opcao == 3:
            nome = input("Nome do Quadrinho: ")
            preco = float(input("Preço do Quadrinho: "))
            autor = input("Autor do Quadrinho: ")
            editora = input("Editora do Quadrinho: ")
            quantidade = int(input("Quantidade: "))
            quadrinho = Quadrinho(nome, preco, autor, editora)
            carrinho.adicionar_produto(quadrinho, quantidade)

        elif opcao == 4:
            if not carrinho.produtos:
                print("Carrinho vazio. Nada para remover.")
                continue

            print("Produtos no Carrinho:")
            for i, produto in enumerate(carrinho.produtos, start=1):
                print(f"{i} - {produto.nome}")

            try:
                escolha = int(input("Escolha o número do produto a ser removido: "))
                produto_remover = carrinho.produtos[escolha - 1]
                quantidade_remover = int(input("Quantidade a ser removida: "))
                carrinho.remover_produto(produto_remover, quantidade_remover)
                print(f"{quantidade_remover} unidades de {produto_remover.nome} removidas do carrinho.")
            except (ValueError, IndexError):
                print("Escolha inválida. Por favor, escolha um número válido.")

        elif opcao == 5:
            carrinho.finalizar_compra()
            break

        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()
