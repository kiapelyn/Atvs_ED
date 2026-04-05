class No:
    def __init__(self, dado):
        self.dado = dado
        self.dir = None
        self.esq = None

class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserirFim(self, dado):
        novo = No(dado)

        if self.tamanho == 0:
            self.inicio = novo

        else:
            self.fim.dir = novo
            novo.esq = self.fim
            self.inicio.esq = novo
            novo.dir = self.inicio

        self.fim = novo
        self.tamanho += 1

    def inserirInicio(self, dado):
        novo = No(dado)

        if self.tamanho == 0:
            self.fim = novo

        else:
            novo.dir = self.inicio
            novo.esq = self.fim
            self.fim.dir = novo
            self.inicio.esq = novo

        self.inicio = novo
        self.tamanho += 1

    def inserirPosicao(self, posicao, dado):
        posicao -= 1
        novo = No(dado)

        if posicao < 0:
            return

        if posicao >= self.tamanho:
            self.inserirFim(dado)
            return
        
        elif posicao == 0:
            self.inserirInicio(dado)
            return

        aux = self.inicio
        for i in range(posicao):
            aux = aux.dir

        novo.esq = aux.esq
        novo.dir = aux

        if aux.esq:
            novo.esq.dir = novo
        else:
            self.inicio = novo

        novo.dir.esq = novo
        self.tamanho += 1

    def imprimir(self):
        aux = self.inicio
        contador = 0

        while contador < self.tamanho:
            print(aux.dado, end=' ')
            aux = aux.dir
            contador += 1

        print()

    def pesquisar(self, dado):
        if self.tamanho == 0:
            return None
        
        aux = self.inicio

        for _ in range(self.tamanho):
            if aux.dado == dado:
                return aux
            aux = aux.dir
        return None

    def remover(self, dado):
        aux = self.pesquisar(dado)

        if aux is not None:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None

            elif aux == self.inicio:
                self.inicio = aux.dir
                self.inicio.esq = self.fim
                self.fim.dir = self.inicio

            elif aux == self.fim:
                self.fim = aux.esq
                self.fim.dir = self.inicio
                self.inicio.esq = self.fim

            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
            self.tamanho -= 1

        aux = None


lista = ListaDupla()

def main():
    while True:
        print(" ========== MENU ==========\n"
        "1. Inserir final\n"
        "2. Inserir com posição\n"
        "3. Imprimir\n"
        "4. Remover\n"
        "5. Sair")
        op = int(input("Escolha uma opção: "))
        print()

        match op:
            case 1:
                dado = int(input("Insira o dado do final: "))
                lista.inserirFim(dado)

            case 2:
                dado = int(input("Insira o dado: "))
                posi = int(input("Insira a posição: "))
                lista.inserirPosicao(posi, dado)

            case 3:
                lista.imprimir()

            case 4:
                dado = int(input("Insira o dado: "))
                lista.remover(dado)

            case 5:
                print("Saindo do programa")
                break
            
            case _:
                print("Insira uma opção válida")
                break

if __name__ == "__main__":
    main()
