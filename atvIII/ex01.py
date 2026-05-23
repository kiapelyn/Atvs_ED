# alguém tem muito tempo livre... e não sou eu
from random import randint

id_usado = []

class Musica:
    def __init__(self, titulo: str, artista:str, duracao: int, genero: str):
        self.id_chave = self._gerar_id()
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.genero = genero
        self.reproducoes = 0

    def _gerar_id(self):
        novo_id = randint(0, 9999)
        while novo_id in id_usado:
            novo_id = randint(0, 9999)
        id_usado.append(novo_id)
        return novo_id

    def __str__(self):
        return f"[{self.id_chave}] {self.titulo} - {self.artista} ({self.genero}) | {self.duracao}s | {self.reproducoes} reproduções"


class No:
    def __init__(self, musica):
        self.musica = musica
        self.esq = None
        self.dir = None

class ArvredeSom:
    def __init__(self):
        self.raiz = None
        
    def inserir_musica(self, dado):
        self.raiz = self._inserir(self.raiz, dado)
    
    def _inserir(self, no, dado):
        if no is None:
            print(f"Música '{dado.titulo}' cadastrada com sucesso! ID gerado: {dado.id_chave}")
            return No(dado)
        
        if dado.id_chave < no.musica.id_chave:
            no.esq = self._inserir(no.esq, dado)
        elif dado.id_chave > no.musica.id_chave:
            no.dir = self._inserir(no.dir, dado)
        
        return no

    def buscar_por_id(self, id_buscado):
        return self._buscar(self.raiz, id_buscado)

    def _buscar(self, no, id_buscado):
            if no is None:
                return None
            if id_buscado == no.musica.id_chave:
                return no.musica
            if id_buscado < no.musica.id_chave:
                return self._buscar(no.esq, id_buscado)
            return self._buscar(no.dir, id_buscado)

        
    def ouvir_musica(self, id_buscado):
        musica = self.buscar_por_id(id_buscado)
        if musica:
            musica.reproducoes += 1
            print(f"Tocando agora: {musica.titulo} - {musica.artista}. Reproduções: {musica.reproducoes}")
        else:
            print("Erro: Música não encontrada.")

    def remover_musica(self, id_buscado):
        self.raiz, removido = self._remover(self.raiz, id_buscado)
        if removido:
            print("Música removida com sucesso.")
        else:
            print("Erro: Música não encontrada para remoção.")

    def _remover(self, no, id_buscado):
        if no is None:
            return None, False
        
        removido = False
        if id_buscado < no.musica.id_chave:
            no.esq, removido = self._remover(no.esq, id_buscado)
        elif id_buscado > no.musica.id_chave:
            no.dir, removido = self._remover(no.dir, id_buscado)
        else:
            removido = True

            if no.esq is None and no.dir is None:
                return None, removido

            if no.esq is None:
                return no.dir, removido
            elif no.dir is None:
                return no.esq, removido
            

            sucessor = self.buscar_menor(no.dir)
            no.musica = sucessor.musica
            no.dir, removido = self._remover(no.dir, sucessor.musica.id_chave)
            
        return no, removido

    def buscar_menor(self, no):
        while no.esq is not None:
            no = no.esq
            
        return no

    def relatorio_top5(self):
        todas_musicas = []
        self._coletar_todas(self.raiz, todas_musicas)
        
        # Obrigado selmini e amigo do selmini, uma função a menos escrita :D
        todas_musicas.sort(key=lambda m: m.reproducoes, reverse=True)
        
        print("=== Relatório Top-5 Músicas Mais Tocadas ===")
        if not todas_musicas:
            print("Nenhuma música cadastrada.")
            return
            
        top5 = todas_musicas[:5]
        for i in range(len(top5)):
            m = top5[i]
            print(f"{i+1} -> {m.titulo} - {m.artista} ({m.reproducoes} reproduções)")

    def _coletar_todas(self, no, lista):
        if no is not None:
            self._coletar_todas(no.esq, lista)
            lista.append(no.musica)
            self._coletar_todas(no.dir, lista)

    def relatorio_por_genero(self, genero_buscado):
        print(f"=== Relatório de Músicas do Gênero: {genero_buscado} ===")
        encontrou = self._relatorio_por_genero_recursivo(self.raiz, genero_buscado.lower())
        if not encontrou:
            print("Nenhuma música encontrada para este gênero.")

    def _relatorio_por_genero_recursivo(self, no, genero_buscado):
        encontrou = False
        if no is not None:
            if self._relatorio_por_genero_recursivo(no.esq, genero_buscado):
                encontrou = True
            if no.musica.genero.lower() == genero_buscado:
                print(f"{no.musica.titulo} - {no.musica.artista} | {no.musica.duracao}s | {no.musica.reproducoes} reproduções")
                encontrou = True
            if self._relatorio_por_genero_recursivo(no.dir, genero_buscado):
                encontrou = True
        return encontrou

def main():
    sistema = ArvredeSom()
    
    while True:
        print("========= MENU =========\n"
            "1 - Cadastrar música\n"
            "2 - Buscar música\n"
            "3 - Ouvir música\n"
            "4 - Remover música\n"
            "5 - Relatório Top-5\n"
            "6 - Relatório por gênero\n"
            "7 - Encerrar")

        op = int(input("Escolha uma opção: "))
        print()

        match op:
            case 1:
                titulo = input("Título da música: ")
                artista = input("Artista: ")
                duracao = int(input("Duração (segundos): "))
                genero = input("Gênero: ")
                nova_musica = Musica(titulo, artista, duracao, genero)
                sistema.inserir_musica(nova_musica)
                print()

            case 2:
                id_busca = int(input("Informe o ID da música: "))
                musica = sistema.buscar_por_id(id_busca)
                if musica:
                    print("Música encontrada:")
                    print(musica)
                    print()
                else:
                    print("Música não encontrada.")
                    print()


            case 3:
                id_busca = int(input("Informe o ID da música que deseja ouvir: "))
                sistema.ouvir_musica(id_busca)
                print()

            case 4:
                id_busca = int(input("Informe o ID da música que deseja remover: "))
                sistema.remover_musica(id_busca)
                print()

            case 5:
                sistema.relatorio_top5()
                print()

            case 6:
                genero = input("Informe o gênero: ")
                sistema.relatorio_por_genero(genero)
                print()

            case 7:
                print("Encerrando o sistema")
                break

            case _:
                print("Opção inválida")
                print()

if __name__ == "__main__":
    main()
