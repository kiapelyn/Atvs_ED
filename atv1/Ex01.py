# Complexidade 0(n^3)

def verifica_soma(array):
    existe = False
    
    for i in range(len(array)):
        somas = []
        if i == 0 or i == 1:
            continue
        else:
            for j in range(i):
                for k in range(j+1, i):
                    somas.append(array[j] + array[k])
                    
        if array[i] in somas:
            existe = True
            break
            
    return existe

#PROGRAMA PRINCIPAL
def main():
    qnt = int(input("Quantos valores serão inseridos? "))
    array = []

    for _ in range(qnt):
        array.append(int(input("Digite um valor: ")))
        
    existe = verifica_soma(array)

    if existe == False:
        print("Nenhum elemento é a soma de dois anteriores.")
    else: 
        print("Existe um elemento que é a soma de dois anteriores.")
        
if __name__ == "__main__":
    main()