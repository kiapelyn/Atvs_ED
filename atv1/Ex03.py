class Livro:
    def __init__(self, titulo:str, autor:str, disp:bool):
        self.titulo = titulo
        self.autor = autor
        self.disp = disp
    
    def emprestar(self):
        self.disp = False
    
    def devolver(self):
        self.disp = True
    
    def __str__(self) -> str:
        if self.disp:
            disponibilidade = "Disponível"
        else:
            disponibilidade = "Indisponível"
        return f'TÍTULO: {self.titulo} | AUTOR: {self.autor} | DISPONIBILIDADE: {disponibilidade}'
    
class Usuario:
    def __init__(self, ra:int, nome:str):
        self.ra = ra
        self.nome = nome
        self.livrosEmp = []
        
    def emprestar_livro(self, livro:Livro):
        if livro.disp:
            livro.emprestar()
            self.livrosEmp.append(livro)
            print("Empréstimo executado com sucesso!")
        else:
            print("Livro indisponível.")
            
    def devolver_livro(self, livro:Livro):
        if livro in self.livrosEmp:
            livro.devolver() 
            
            nova_lista = []
            
            for l in self.livrosEmp:
                if l != livro:
                    nova_lista.append(l)
            self.livrosEmp = nova_lista
            print("Devolução executada com sucesso!")
            
        else:
            print("Não foi possível realizar a devolução.")
    
    def listar_livros(self):
        return self.livrosEmp
        
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
    
    def cadastrar_livro(self, livro:Livro):
        for livrinho in self.livros:
            if livrinho.titulo == livro.titulo:
                print("Título já cadastrado.")
                return
        self.livros.append(livro)
        print("Título cadastrado com sucesso.")
            
    def cadastrar_usuario(self, usuario:Usuario):
        for u in self.usuarios:
            if u.ra == usuario.ra:
                print("Usuário já cadastrado.")
                return
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso.")
    
    def realizar_emprestimo(self, ra, titulo):
        usuario_encontrado = next((u for u in self.usuarios if u.ra == ra), None)
        livro_encontrado = next((l for l in self.livros if l.titulo == titulo), None)
        
        if not usuario_encontrado:
            print("Usuário não encontrado.")
            return
        if not livro_encontrado:
            print("Livro não encontrado.")
            return
        
        usuario_encontrado.emprestar_livro(livro_encontrado)
            
    def realizar_devolucao(self, ra, titulo):
        usuario_encontrado = next((u for u in self.usuarios if u.ra == ra), None)
        livro_encontrado = next((l for l in self.livros if l.titulo == titulo), None)
        
        if not usuario_encontrado or not livro_encontrado:
            print("Usuário ou Livro não encontrados.")
            return
            
        usuario_encontrado.devolver_livro(livro_encontrado)
            
    def listar_livros_disponiveis(self):
        disponiveis = [l for l in self.livros if l.disp]
        if not disponiveis:
            print("Nenhum livro disponível no momento.")
        else:
            for l in disponiveis:
                print(l)
    
    def listar_livros_emprestados_usuario(self, ra):
        usuario_encontrado = next((u for u in self.usuarios if u.ra == ra), None)
        if usuario_encontrado:
            livros = usuario_encontrado.listar_livros()
            if not livros:
                print("O usuário não possui livros emprestados.")
            else:
                for l in livros:
                    print(l)
        else:
            print("Usuário não encontrado.")

def main():
    biblioteca = Biblioteca()

    while True:
        menu = int(input("\nDigite o número da operação: \n1. Cadastrar livro \n2. Cadastrar usuário \n3. Realizar empréstimo \n4. Realizar devolução \n5. Listar livros disponíveis \n6. Listar livros emprestados ao usuário \n7. Finalizar \n--> "))

        match menu:
            case 1:
                titulo = input("Título do livro: ")
                autor = input("Nome do Autor: ")
                disponibilidade = input("Disponível (0) ou Indisponível (1): ")
                disp = True if disponibilidade == '0' else False 
                biblioteca.cadastrar_livro(Livro(titulo, autor, disp))

            case 2:
                ra = int(input("RA do usuário: "))
                nome = input("Nome do usuário: ")
                biblioteca.cadastrar_usuario(Usuario(ra, nome))
            
            case 3:
                ra = int(input("RA do usuário: "))
                titulo = input("Título do livro: ")
                biblioteca.realizar_emprestimo(ra, titulo)

            case 4:
                ra = int(input("RA do usuário: "))
                titulo = input("Título do livro: ")
                biblioteca.realizar_devolucao(ra, titulo)

            case 5:
                biblioteca.listar_livros_disponiveis()
                
            case 6:
                ra = int(input("RA do usuário: "))
                biblioteca.listar_livros_emprestados_usuario(ra)
                
            case 7:
                print("Sistema finalizado.")
                break
                
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()