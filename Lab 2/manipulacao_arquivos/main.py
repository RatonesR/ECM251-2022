#programa que escreve em um arquivo

arquivo = open("dados.txt", "a")
continuar = True

while continuar:
    #time é string
    time = input("Time (vazio para sair): ")
    #toda string vazia é falsa
    #entra no if se a string está vazia
    if not time:
        continuar = False
        continue
    arquivo.write(time + '\n')
arquivo.close()