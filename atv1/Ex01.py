# a complexidade do código é de O(n^2)

qnt = int(input("Quantos valores serão inseridos? "))
array = []

existe = False

for _ in range(qnt):
    array.append(int(input("Digite um valor: ")))

for i in range(len(array)):
    somas = []
    if i == 0 or i == 1:
        continue
    else:
        for j in range(i-1):
            somas.append(array[i-1]+array[j])
    if array[i] in somas:
        existe = True
        break



if existe == False:
    print("Nenhum elemento é a soma de dois anteriores")
else: print("Existe um elemento que é a soma dos dois anteriores")


