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
        auxiliar = []
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
                auxiliar.append({
                                 "nome": dado.dado["nome"],
                                 "tempo_total": dado.dado["tempo_total"],
                                 "tempo_espera": tempo_global - dado.dado["tempo_total"],
                                 "tempo_retorno": tempo_global
                                 })
                self.remover(dado)

            dado = aux
            
        return auxiliar

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
        
    def calcular_medias(self, auxiliar):
        media_espera = 0
        media_retorno = 0
        
        for i in range(len(auxiliar)):
            media_espera += auxiliar[i]['tempo_espera']
            media_retorno += auxiliar[i]['tempo_retorno']
            
        media_espera /= len(auxiliar)
        media_retorno /= len(auxiliar)
            
        return media_espera, media_retorno
        

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

    auxiliar = lista.executar(fatia)
    media_espera, media_retorno = lista.calcular_medias(auxiliar)


    print("RELATÓRIO FINAL - ARIA Recovery Module.")
    print(f"Faria de tempo (quantum): {fatia} unidades")
    print("----------------------------------------------------------")
    print(f"Processo      Tempo Total   Tempo Espera   Tempo Retorno")
    for i in range(len(auxiliar)):
        print(f"{auxiliar[i]['nome']}    {auxiliar[i]['tempo_total']}     {auxiliar[i]['tempo_espera']}     {auxiliar[i]['tempo_retorno']}")
    
    print(f"média do tempo de espera: {media_espera}")
    print(f"média do tempo de retorno: {media_retorno}")
    
    if media_espera < 16:
        print('ARIA reativada com sucesso.')
    else:
        print("Falha crítica confirmada. Iniciando protocolo de desligamento de emergência.")

if __name__ == "__main__":
    main()
