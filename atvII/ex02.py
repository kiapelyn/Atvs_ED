# a pessoa q montou isso n está mentalmente estável, sem ofensas, muito obrigada

'''Semaforo custa 8
Hospital custa 4
Energia custa 9
Transporte custa 5'''

'''ordem: 
- semaforo -> 8 pra 5
- hospital -> 4 pra 1
- energia -> 9 pra 6
- transporte -> 5 pra 2
- semaforo -> 5 pra 2
- hospital -> 1 pra concluído
- energia -> 6 pra 3
- transporte -> 2 pra concluído
- semaforo -> 2 pra concluído
- energia -> 3 pra concluído'''

'''O que falta:

7. Exibir ao final um relatório completo com os tempos de espera e retorno de cada processo.
Simulação completa

'''

# precisa ser um loop até tudo concluir, oq acabou tem q sair, tem q ser duplamente encadeado circular

''' cara oq diabos é pra por de input? dados seria o nome do processo e o tempo necessário?'''

class No:
    def __init__(self, dado: dict):
        self.dado = dado
        self.dir = None
        self.esq = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserirFim(self, nome, tempo):
        novo = No({
            "nome": nome,
            "tempo_restante": tempo,
            "tempo_total": tempo,
            "tempo_retorno": None
        })

        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
            novo.dir = novo
            novo.esq = novo
        else:
            self.fim.dir = novo
            novo.esq = self.fim
            novo.dir = self.inicio
            self.inicio.esq = novo
            self.fim = novo

        self.tamanho += 1

    def executar(self, fatia):
        if self.tamanho == 0:
            return

        tempo_global = 0
        dado = self.inicio

        while self.tamanho > 0:
            if dado.dado["tempo_restante"] > fatia:
                tempo_execucao = fatia
            else:
                tempo_execucao = dado.dado["tempo_restante"]

            dado.dado["tempo_restante"] -= tempo_execucao
            tempo_global += tempo_execucao

            aux = dado.dir

            if dado.dado["tempo_restante"] == 0:
                dado.dado["tempo_retorno"] = tempo_global
                self.remover(dado)

            dado = aux

    # remove o concluído
    def remover(self, dado):
        if self.tamanho == 0 or dado is None:
            return

        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            dado.esq.dir = dado.dir
            dado.dir.esq = dado.esq

            if dado == self.inicio:
                self.inicio = dado.dir

            if dado == self.fim:
                self.fim = dado.esq

        self.tamanho -= 1


def main():
    lista = ListaDupla()

    fatia = int(input("Qual a fatia de tempo? "))
    while fatia <= 0:
        fatia = int(input("Digite uma fatia maior que 0: "))

    qtd = int(input("Quantos processos serão inseridos? "))

    for i in range(qtd):
        print(f"Processo {i+1}:")

        nome = input("Nome: ")
        tempo = int(input("Tempo necessário: "))

        lista.inserirFim(nome, tempo)

    lista.executar(fatia)

    print("Execução finalizada.")
    #sinceramente, n tenho certeza de nada, amh quando eu adaptar pro relatório eu descubro :D


if __name__ == "__main__":
    main()
