from random import randint

codigos_usados = []

class Ativo:
    def __init__(self, ticker: str, nomeEmpresa: str, setor: str, cotacaoAtual: float, qtdCotas: int, tipoAtivo: str):
        self.codigoAtivo = self._gerar_codigo()
        self.ticker = ticker
        self.nomeEmpresa = nomeEmpresa
        self.setor = setor
        self.cotacaoAtual = cotacaoAtual
        self.qtdCotas = qtdCotas
        self.tipoAtivo = tipoAtivo

    def _gerar_codigo(self):
        novo_codigo = randint(1000, 9999)
        while novo_codigo in codigos_usados:
            novo_codigo = randint(1000, 9999)
        codigos_usados.append(novo_codigo)
        return novo_codigo

    def valor_proprio(self):
        return self.cotacaoAtual * self.qtdCotas

    def __str__(self):
        return f"[{self.codigoAtivo}] {self.ticker} - {self.nomeEmpresa} ({self.tipoAtivo}) | Cotação: R$ {self.cotacaoAtual:.2f} | Cotas: {self.qtdCotas} | Valor: R$ {self.valor_proprio():.2f}"

class No:
    def __init__(self, ativo):
        self.ativo = ativo
        self.esq = None
        self.dir = None

class ArvreCapital:
    def __init__(self):
        self.raiz = None

    def cadastrar_ativo(self, ticker, nome, setor, cotacao, qtd, tipo):
        novo_ativo = Ativo(ticker, nome, setor, cotacao, qtd, tipo)
        self.raiz = self._inserir(self.raiz, novo_ativo)
        print(f"Ativo '{ticker}' cadastrado com sucesso! Código gerado: {novo_ativo.codigoAtivo}")
        return novo_ativo.codigoAtivo

    def _inserir(self, no, ativo):
        if no is None:
            return No(ativo)
        
        if ativo.codigoAtivo < no.ativo.codigoAtivo:
            no.esq = self._inserir(no.esq, ativo)
        elif ativo.codigoAtivo > no.ativo.codigoAtivo:
            no.dir = self._inserir(no.dir, ativo)
            
        return no

    def buscar_ativo(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, no, codigo):
        if no is None:
            return None
        if codigo == no.ativo.codigoAtivo:
            return no.ativo
        if codigo < no.ativo.codigoAtivo:
            return self._buscar(no.esq, codigo)
        return self._buscar(no.dir, codigo)

    def atualizar_cotacao(self, codigo, nova_cotacao):
        ativo = self.buscar_ativo(codigo)
        if ativo:
            ativo.cotacaoAtual = nova_cotacao
            print(f"Cotação do ativo {ativo.ticker} atualizada para R$ {nova_cotacao:.2f}")
        else:
            print("Erro: Ativo não encontrado.")

    def retirar_ativo(self, codigo):
        self.raiz, removido = self._remover(self.raiz, codigo)
        if removido:
            print("Ativo removido da carteira com sucesso.")
        else:
            print("Erro: Ativo não encontrado para remoção.")

    def _remover(self, no, codigo):
        if no is None:
            return None, False
        
        removido = False
        if codigo < no.ativo.codigoAtivo:
            no.esq, removido = self._remover(no.esq, codigo)
        elif codigo > no.ativo.codigoAtivo:
            no.dir, removido = self._remover(no.dir, codigo)
        else:
            removido = True
            if no.esq is None:
                return no.dir, removido
            if no.dir is None:
                return no.esq, removido
            
            sucessor = self._buscar_menor(no.dir)
            no.ativo = sucessor.ativo
            no.dir, _ = self._remover(no.dir, sucessor.ativo.codigoAtivo)
            
        return no, removido

    def _buscar_menor(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
        return atual

    def valor_patrimonial(self, no):
        if no is None:
            return 0.0
        return no.ativo.valor_proprio() + self.valor_patrimonial(no.esq) + self.valor_patrimonial(no.dir)

    def qtd_ativos_subarvore(self, no):
        if no is None:
            return 0
        return 1 + self.qtd_ativos_subarvore(no.esq) + self.qtd_ativos_subarvore(no.dir)

    def _obter_no(self, no, codigo):
        if no is None:
            return None
        if codigo == no.ativo.codigoAtivo:
            return no
        if codigo < no.ativo.codigoAtivo:
            return self._obter_no(no.esq, codigo)
        return self._obter_no(no.dir, codigo)

    def relatorio_patrimonial_subarvore(self, codigo):
        no_buscado = self._obter_no(self.raiz, codigo)
        
        if no_buscado is None:
            print("Erro: Ativo não encontrado.")
            return

        # Calcula o patrimônio total da carteira a partir da raiz
        patrimonio_total_carteira = self.valor_patrimonial(self.raiz)
        
        # Calcula o patrimônio da subarvore do ativo consultado
        patrimonio_subarvore = self.valor_patrimonial(no_buscado)
        
        # Quantidade de ativos na subarvore
        ativos_na_subarvore = self.qtd_ativos_subarvore(no_buscado)
        
        # Cálcula a participação percentual
        if patrimonio_total_carteira > 0:
            participacao = (patrimonio_subarvore / patrimonio_total_carteira) * 100
        else:
            participacao = 0.0

        ativo = no_buscado.ativo

        print("==== Relatório Patrimonial da Subárvore ===\n"
            f"Ativo consultado:    {ativo.ticker} (código: {ativo.codigoAtivo})\n"
            f"Valor próprio:       R$ {ativo.valor_proprio():.2f} (cotação: R$ {ativo.cotacaoAtual:.2f} x {ativo.qtdCotas} cotas)\n"
            f"Ativos na subárvore: {ativos_na_subarvore}\n"
            f"Valor patrimonial da subárvore: R$ {patrimonio_subarvore:.2f}\n"
            f"Participação no patrimônio total da carteira: {participacao:.1f}%")


def main():
    sistema = ArvreCapital()
    
    while True:
        print("========= MENU =========\n"
            "1 - Cadastrar ativo\n"
            "2 - Buscar ativo por código\n"
            "3 - Atualizar cotação\n"
            "4 - Retirar ativo da carteira\n"
            "5 - Valor patrimonial da subárvore\n"
            "6 - Sair do sistema")
        
        op = int(input("Escolha uma opção: "))
        
        match op:
            case 1:
                ticker = input("Ticker do ativo (ex: PETR4): ").upper()
                nome = input("Nome da empresa/fundo: ")
                setor = input("Setor: ")
                cotacao = float(input("Cotação atual: "))
                qtd = int(input("Quantidade de cotas: "))
                tipo = input("Tipo de ativo (ACAO, FII, TITULO): ").upper()
                sistema.cadastrar_ativo(ticker, nome, setor, cotacao, qtd, tipo)
                print()
                
            case 2:
                codigo = int(input("Informe o código interno do ativo: "))
                ativo = sistema.buscar_ativo(codigo)
                if ativo:
                    print("\nAtivo encontrado:")
                    print(ativo)
                else:
                    print("\nAtivo não encontrado.")
                print()
                    
            case 3:
                codigo = int(input("Informe o código interno do ativo: "))
                nova_cotacao = float(input("Informe a nova cotação: R$ "))
                sistema.atualizar_cotacao(codigo, nova_cotacao)
                print()
                
            case 4:
                codigo = int(input("Informe o código interno do ativo para remoção: "))
                sistema.retirar_ativo(codigo)
                print()
                
            case 5:
                codigo = int(input("Informe o código interno do ativo (raiz da subárvore): "))
                sistema.relatorio_patrimonial_subarvore(codigo)
                print()
                
            case 6:
                print("Encerrando o sistema")
                break
                
            case _:
                print("Opção inválida")
                print()

if __name__ == "__main__":
    main()
