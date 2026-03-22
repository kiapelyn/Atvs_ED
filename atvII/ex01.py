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

        self.fim = novo
        self.tamanho += 1

    def inserirPosicao(self, posicao, dado):
        novo = No(dado)

        aux = self.inicio
        #bets pensa numa lista com posicao a, b e c e a gente ta pondo o novo na segunda posiçao (entre a e b)

        if posicao < 0:
            return

        for i in range(posicao):
            aux = aux.dir # corre a lista até pegar o valor q ta na posicao q a gente quer o novo (ex: b)

        if posicao >= self.tamanho: # se a posição for igual ao tamanho, ou maior, é a ms coisa q por no fim
            self.inserirFim(self, dado)
            return
        else:
            novo.esq = aux.esq # poe o endereço que ta na esquerda de b para a esquerda do novo
            novo.dir = aux # poe o endereço de b na direita do novo

            if aux.esq: # verifica que nao é o primeiro valor da lista
                novo.esq.dir = novo # poe o endereço de novo na direita do a
            else: #se for, atribui no inicio msm
                self.inicio =  novo

            novo.dir.esq = novo # poe o endereço de novo na esquerda do b


    def imprimir(self):
        aux = self.inicio
        while aux:
            print(aux.dado, end=' ')
            aux = aux.dir
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
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None

            elif aux == self.fim:
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None

            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None

        aux = None
        self.tamanho -= 1