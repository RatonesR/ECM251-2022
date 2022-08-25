#programa que escreve em um arquivo

try:
    arquivo = open("data/dados.txt", "a")
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

except FileNotFoundError:
    print("Arquivo ou diretório não encontrado")

except ZeroDivisionError:
    print("Alguem tentou dividir por zero")

except:
    print("Algo de errado aconteceu!")

finally:
    print("Enfim terminou")