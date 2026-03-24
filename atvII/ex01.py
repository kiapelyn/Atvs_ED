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
            novo.dir = self.inicio #referencia pro inicio da lista

        self.fim = novo
        self.tamanho += 1

    def inserirInicio(self, dado):
        novo = No(dado)

        if self.tamanho == 0:
            self.fim = novo

        else:
            novo.dir = self.inicio
            novo.esq = self.fim # referencia pro fim da lista
            self.fim.dir = novo
            self.inicio.esq = novo

        self.inicio = novo
        self.tamanho += 1

    def inserirPosicao(self, posicao, dado):
        posicao -= 1 # espécie de "conversão" pois o for vai inicializar em 0,
                     # assim a posição digitada é a mesma que será inserido
        novo = No(dado)

        aux = self.inicio
        #bets pensa numa lista com posicao a, b e c e a gente ta pondo o novo na segunda posiçao (entre a e b)

        if posicao < 0:
            return

        for i in range(posicao):
            aux = aux.dir # corre a lista até pegar o valor q ta na posicao q a gente quer o novo (ex: b)

        if posicao >= self.tamanho: # se a posição for igual ao tamanho, ou maior, é a ms coisa q por no fim
            self.inserirFim(dado)
            return
        elif posicao == 0:
            self.inserirInicio(dado)
        else:
            novo.esq = aux.esq # poe o endereço que ta na esquerda de b para a esquerda do novo
            novo.dir = aux # poe o endereço de b na direita do novo

            if aux.esq: # verifica que nao é o primeiro valor da lista
                novo.esq.dir = novo # poe o endereço de novo na direita do a
            else: #se for, atribui no inicio msm
                self.inicio =  novo

            novo.dir.esq = novo # poe o endereço de novo na esquerda do b

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
        aux = self.inicio
        while aux:
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
