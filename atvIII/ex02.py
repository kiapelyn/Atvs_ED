class Especie:
    def __init__(self, codigoRaridade:int, continenteOrigem:str, nomeComum:str, qtdAmostras:int, nomeCientifico:str):
        self.codigoRaridade = codigoRaridade       #chave avl
        self.continenteOrigem = continenteOrigem   
        self.nomeComum = nomeComum                 
        self.qtdAmostras = qtdAmostras             
        self.nomeCientifico = nomeCientifico       

    def __repr__(self):
        return f"[CR: {self.codigoRaridade:04d}] {self.nomeComum:<10} ({self.nomeCientifico}) | {self.continenteOrigem:<10} | Amostras: {self.qtdAmostras}"


class No:
    def __init__(self, especie):
        self.especie = especie 
        self.esq = None   
        self.dir = None   
        self.altura = 1         # folha começa com altura 1

    def __repr__(self):
        return str(self.especie)


class AVLArkSeed:
    def __init__(self):
        self.raiz = None

    def _altura(self, no):        
        if no is None: 
            return 0 
        return no.altura

    def _atualizar_altura(self, no):        
        # descobrimos a altura de cada lado primeiro
        altura_esq = self._altura(no.esq)
        altura_dir = self._altura(no.dir)
        
        # qual é maior? soma 1 nela
        if altura_esq > altura_dir:
            no.altura = 1 + altura_esq
        else:
            no.altura = 1 + altura_dir

    def _fator_bal(self, no):
        if no is None: 
            return 0
        return self._altura(no.esq) - self._altura(no.dir)

    def _rotacao_direita(self, z):
        y = z.esq
        T3 = y.dir
        y.dir = z
        z.esq = T3
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def _rotacao_esquerda(self, z):
        y = z.dir
        T2 = y.esq
        y.esq = z
        z.dir = T2
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def _rebalancear(self, no):
        self._atualizar_altura(no)
        fb = self._fator_bal(no)

        if fb > 1 and self._fator_bal(no.esq) >= 0:
            return self._rotacao_direita(no)
        if fb > 1 and self._fator_bal(no.esq) < 0:
            no.esq = self._rotacao_esquerda(no.esq)
            return self._rotacao_direita(no)
        if fb < -1 and self._fator_bal(no.dir) <= 0:
            return self._rotacao_esquerda(no)
        if fb < -1 and self._fator_bal(no.dir) > 0:
            no.dir = self._rotacao_direita(no.dir)
            return self._rotacao_esquerda(no)
        return no

    # a) Catalogar espécie
    def catalogar(self, especie):
        self.raiz = self._inserir(self.raiz, especie)

    def _inserir(self, no, especie):        
        if no is None:
            return No(especie)

        if especie.codigoRaridade < no.especie.codigoRaridade:
            no.esq = self._inserir(no.esq, especie)
        elif especie.codigoRaridade > no.especie.codigoRaridade:
            no.dir = self._inserir(no.dir, especie)
        else:
            return no  #assim a gnt ignora o que está duplicado

        return self._rebalancear(no)

    # d) Buscar por código de raridade
    def buscar(self, codigo):
        no_encontrado = self._buscar(self.raiz, codigo)
        if no_encontrado:
            return no_encontrado.especie
        return None

    def _buscar(self, no, codigo):
        if no is None:
            return None
        if codigo == no.especie.codigoRaridade:
            return no
        if codigo < no.especie.codigoRaridade:
            return self._buscar(no.esq, codigo)
        return self._buscar(no.dir, codigo)

    ####
    def _remover_por_codigo(self, codigo):
        self.raiz = self._remover(self.raiz, codigo)

    def _remover(self, no, codigo):
        if no is None: return None

        if codigo < no.especie.codigoRaridade:
            no.esq = self._remover(no.esq, codigo)
        elif codigo > no.especie.codigoRaridade:
            no.dir = self._remover(no.dir, codigo)
        else:
            if no.esq is None: return no.dir   
            if no.dir is None: return no.esq   

            sucessor = self._minimo(no.dir)
            no.especie = sucessor.especie 
            no.dir = self._remover(no.dir, sucessor.especie.codigoRaridade)

        return self._rebalancear(no)

    def _minimo(self, no):
        while no.esq is not None:
            no = no.esq
        return no

    # b) Alerta de extinção 
    def alerta_extincao(self, codigo_antigo, novo_codigo):
        
        especie_alvo = self.buscar(codigo_antigo)
        if especie_alvo:
            self._remover_por_codigo(codigo_antigo) # remove antigo
            especie_alvo.codigoRaridade = novo_codigo # atualiza
            self.catalogar(especie_alvo) # reinsere para balancear no novo
            print(f">> {especie_alvo.nomeComum} atualizada para raridade {novo_codigo}.")
        else:
            print(">> Espécie não encontrada.")

    # c) Resgatar espécie mais rara
    def resgatar_mais_rara(self):
        if self.raiz is None:
            print(">> Banco de sementes vazio.")
            return None
        
        # mais raro = maior valor = nó direita
        no_atual = self.raiz
        while no_atual.dir is not None:
            no_atual = no_atual.dir
            
        especie_resgatada = no_atual.especie
        self._remover_por_codigo(especie_resgatada.codigoRaridade)
        return especie_resgatada

    # e) Relatório de emergência
    def relatorio_emergencia(self):
        
        print("\n--- RELATÓRIO DE EMERGÊNCIA ---")
        self._em_ordem_dec(self.raiz)
        print("---------------------------------")

    def _em_ordem_dec(self, no):
        if no is None:
            return
        self._em_ordem_dec(no.dir)  
        print(no.especie) 
        self._em_ordem_dec(no.esq) 


def menu():
    print("\n" + "="*50)
    print("SISTEMA ORBITAL ARKSEED - ANO 2203")
    print("="*50)
    print("1. Catalogar nova espécie")
    print("2. Alerta de Extinção")
    print("3. Resgatar Espécie Mais Rara")
    print("4. Buscar por código de raridade")
    print("5. Relatório de Emergência")
    print("0. Desligar Sistema")
    print("="*50)

if __name__ == "__main__":
    ark = AVLArkSeed()

    #teste
    ark.catalogar(Especie(150, "SELMINI", "Antonio", 500, "Marcos"))
    ark.catalogar(Especie(9000, "RAFAEL", "Carlos", 10, "Gimenes"))
    ark.catalogar(Especie(4500, "TATI", "Tatiana", 120, "Melhado"))
    ark.catalogar(Especie(200, ":)", "O", 3000, "Lista"))

    while True:
        menu()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            print("\n--- Catalogar Espécie ---")
            cod = int(input("Código de Raridade (1-9999): "))
            nome_c = input("Nome Comum: ")
            nome_ci = input("Nome Científico: ")
            cont = input("Continente de Origem: ")
            qtd = int(input("Quantidade de Amostras: "))
            
            nova_especie = Especie(cod, cont, nome_c, qtd, nome_ci)
            ark.catalogar(nova_especie)
            print(">> Espécie catalogada com sucesso!")

        elif opcao == "2":
            print("\n--- Alerta de Extinção ---")
            cod_antigo = int(input("Informe o código de raridade atual: "))
            cod_novo = int(input("Informe o NOVO código de raridade: "))
            ark.alerta_extincao(cod_antigo, cod_novo)

        elif opcao == "3":
            print("\n--- Resgate de Emergência ---")
            resgatada = ark.resgatar_mais_rara()
            if resgatada:
                print(">> ESPÉCIE RESGATADA: ")
                print(resgatada)

        elif opcao == "4":
            print("\n--- Busca no Banco ---")
            cod = int(input("Código de Raridade: "))
            resultado = ark.buscar(cod)
            if resultado:
                print(">> Encontrada: ")
                print(resultado)
            else:
                print(">> Código não localizado")

        elif opcao == "5":
            ark.relatorio_emergencia()

        elif opcao == "0":
            print("Finalizando sistema")
            break
        else:
            print("Opção inválida.")