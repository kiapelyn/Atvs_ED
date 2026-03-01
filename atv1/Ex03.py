class Livro:
    def __init__(self, titulo: str, autor: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self) -> bool:
        if self.disponivel:
            print("Emprestimo disponivel")
        else: print("Emprestimo indisponivel")
        return self.disponivel

    def devolver(self) -> bool:
        if self.disponivel == False:
            print("Devolução possível")
            return True
        else:
            print("Livro não está emprestado")
            return False

    def __str__(self):
        if self.disponivel: disp = "Disponível"
        else: disp = "Emprestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | Status: {disp}"

class Usuario:
    def __init__(self, nome: str, ra: int):
        self.nome = nome
        self.ra = ra
        self.lista = []

    def emprestar_livro(self, livro):
            if livro.emprestar():
                self.lista.append(livro)
                livro.disponivel = False
                print("Empréstimo realizado")
            else:
                print("Livro indisponível")

    def devolver_livro(self, livro):
        if livro in self.lista:
            if livro.devolver():
                self.lista.remove(livro)
                livro.disponivel = True
                print("Devolução realizada")
        else:
            print("Devolução inexistente")

    def listas_livros(self) -> list:
        return self.lista

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro: Livro):
        for i in self.livros:
            if i.titulo == livro.titulo:
                print("Este livro já foi cadastrado")
                return
        self.livros.append(livro)
        print("Livro cadastrado com sucesso")

    def cadastrar_usuario(self, usuario: Usuario):
        for i in self.usuarios:
            if i.ra == usuario.ra:
                print("RA já cadastrado")
                return
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso")

    def buscar(self, ra: int, titulo: str):
        usuario, livro = None, None
        for i in self.usuarios:
            if i.ra == ra:
                usuario = i
                break
        for i in self.livros:
            if i.titulo == titulo:
                livro = i
                break
        return usuario, livro

    def realizar_emprestimo(self, ra: int, titulo: str):
        usuario, livro = self.buscar(ra, titulo)

        if usuario is None: print("Usuário não cadastrado")
        elif livro is None: print("Livro não cadastrado")
        else: usuario.emprestar_livro(livro)

    def realizar_devolucao(self, ra: int, titulo: str):
        usuario, livro = self.buscar(ra, titulo)

        if usuario is None: print("Usuário não cadastrado")
        elif livro is None: print("Livro não cadastrado")
        else: usuario.devolver_livro(livro)

    def listar_livros_disponiveis(self):
        disponiveis = []
        for i in self.livros:
            if i.disponivel:
                disponiveis.append(i)
        return disponiveis

    def listar_livros_emprestados_usuarios(self, ra):
        for i in self.usuarios:
            if i.ra == ra:
                return i.listas_livros()
        return []


#INSTANCIAS
biblioteca = Biblioteca()

#PROGRAMA PRINCIPAL
def main():
    while True:
        print(" ========== MENU ==========\n"
        "1. Cadastrar livro\n"
        "2. Cadastrar usuário\n"
        "3. Realizar empréstimo\n"
        "4. Realizar devolução\n"
        "5. Listar livros disponíveis\n"
        "6. Listar livros emprestados ao usuário\n"
        "7. Finalizar")
        op = int(input("Escolha uma opção: "))
        print()
        match op:
            case 1:
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                livro = Livro(titulo, autor)
                biblioteca.cadastrar_livro(livro)
            case 2:
                nome = input("Nome do usuário: ")
                ra = int(input("RA do usuário: "))
                usuario = Usuario(nome, ra)
                biblioteca.cadastrar_usuario(usuario)
            case 3:
                ra = int(input("RA do usuário: "))
                titulo = input("Título do livro: ")
                biblioteca.realizar_emprestimo(ra, titulo)
            case 4:
                ra = int(input("RA do usuário: "))
                titulo = input("Título do livro: ")
                biblioteca.realizar_devolucao(ra, titulo)
            case 5:
                livros = biblioteca.listar_livros_disponiveis()
                if livros:
                    for livro in livros:
                        print(livro)
                else:
                    print("Nenhum livro disponível.")
            case 6:
                ra = int(input("RA do usuário: "))
                livros = biblioteca.listar_livros_emprestados_usuarios(ra)
                if livros:
                    for livro in livros:
                        print(livro)
                else:
                    print("Nenhum livro emprestado para este usuário.")
            case 7:
                print("Encerrado")
                break
            case _:
                print("Opção invalida!")

        print()

if __name__ == "__main__":
    main()

