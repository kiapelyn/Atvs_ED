array = []
frequencia = {}
maiores = []



def entrada_de_dados(qnt):
    while len(array) < qnt:
        num = (int(input("Digite um numero: ")))
        if num > qnt*4: print(f"O valor deve estar entre 0 e {qnt*4}")
        elif num < 0: print("O valor deve ser maior ou igual a 0")
        else:
            array.append(num)
    return array

def calcular_frequencia(array):
    for num in array:
        if num in frequencia:
            frequencia[num] += 1
        else: frequencia[num] = 1
    return frequencia

def calcular_maior(frequencia, maior):
    for valor in frequencia:
        if frequencia[valor] == maior:
            maiores.append(valor)
    return maiores

def main():
    qnt = int(input("Quantos elementos terá a lista? "))
    array = entrada_de_dados(qnt)
    frequencia = calcular_frequencia(array)
    maior = max(frequencia.values())
    maiores = calcular_maior(frequencia, maior)
    if (len(maiores)) == len(frequencia): print("Todos os valores apresentam a mesma frequência")
    else:
        print(f"Valor(es) mais frequênte(s): {maiores}")
        print(f"Frequência = {maior}")


if __name__ == "__main__":
    main()


