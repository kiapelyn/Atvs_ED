class No:
    def __init__(self, dado):
        self.dado = dado #-> uma lista [nome, tipo]
        self.dir = None
        self.esq = None

class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.prioridade = -1 #sem prioritários ainda
    
    def pacienteComum(self, dado):
        novo = No([dado, "Comum"])
        if self.tamanho == 0:
            self.inicio = novo
            
        else:
            self.fim.dir = novo
            novo.esq = self.fim

        self.fim = novo
        self.tamanho += 1

    def inserirInicio(self, dado):
        novo = No(dado)
        if self.tamanho == 0:
            self.fim = novo

        else:
            novo.dir = self.inicio
            self.inicio.esq = novo

        self.inicio = novo
        self.tamanho += 1
        
    def pacientePrioritario(self, dado):
        novo = No([dado, "Prioritário"])
        aux = self.inicio
        
        if self.prioridade == -1:
            self.inserirInicio([dado, "Prioritário"])
            self.prioridade += 1
            return
        
        for i in range(self.prioridade):
            aux = aux.dir
        
        novo.dir = aux.dir

        if aux.dir:
            aux.dir.esq = novo

        else:
            self.fim = novo
        aux.dir = novo
        novo.esq = aux
        
        self.prioridade += 1
        self.tamanho += 1
        
    def inserir(self, nome, prioritario):
        if prioritario == "s":
            self.pacientePrioritario(nome)

        elif prioritario == "n":
            self.pacienteComum(nome)

        else:
            print("Insira um valor válido para prioridade (s/n)")
        
    def imprimir(self):
        aux = self.inicio

        while aux:
            print(aux.dado[0], end=' ')
            aux = aux.dir
        print()
        
    def buscar(self, dado):
        posição = 1
        aux = self.inicio

        while aux:
            if aux.dado[0] == dado:
                return aux, posição
            
            aux = aux.dir
            posição += 1
        return None

    def atender(self):
        aux = self.inicio

        if aux is not None:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None

            else:
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None
            self.tamanho -= 1

        return aux.dado
        
lista = ListaDupla()
        
def main():
    while True:
        print(" ========== MENU ==========\n"
        "1. Inserir Paciente\n"
        "2. Atender Paciente\n"
        "3. Imprimir\n"
        "4. Buscar Paciente\n"
        "5. Sair")
        op = int(input("Escolha uma opção: "))
        print()

        match op:
            case 1:
                dado = input("Nome do paciente: ")
                priori = input("O paciente é prioritário? (s/n) ")
                lista.inserir(dado, priori)

            case 2:
                atendimento = lista.atender()
                print(f"Paciente {atendimento[0]} sendo atendido")

            case 3:
                lista.imprimir()

            case 4:
                resultado = lista.buscar(input("Nome do paciente: "))
                if resultado is None:
                    print("Paciente não encontrado")
                else:
                    nome, posi = resultado
                    print(f"Paciente {nome.dado[0]} está na posição {posi} e é um paciente {nome.dado[1]}")

            case 5:
                print("programa encerrado")
                break

            case _:
                break
            
if __name__ == "__main__":
    main()