import os
import shutil

# versão v. 1.0

caminho = os.getcwd()
parts = []

def gerador_de_pastas():

    mess("GERADOR DE PASTAS BY BRUNO v. 1.0")

    input("Pressione enter para iniciar ...")

    if verpasta():

        if verarquivo():
            with open('lista.txt', 'r', encoding="utf-8") as file:
                for x in file:
                    parts.append(x.replace('\n', ''))
            if len(parts) > 0:
                    gerapastas()
            else:
                print('\n')
                mess("O arquivo lista.txt está vazio!")
        else:
            print('\n')
            mess("Por favor, preencha o arquivo lista.txt com os nomes das pastas")
    else:
        print('\n')
        mess("A pasta itens não está vazia")

    input("Pressione enter para fechar ...")

def mess(x):
    b = len(x) + 2
    print(b * "#")
    print((f"#{x}#").upper())
    print(b * "#")
    print("\n")

def verpasta():
    if os.path.isdir("itens"):
        if len(os.listdir("Itens")) == 0:
            return True
        else: return False
    else:
        os.mkdir(os.path.join(caminho, "Itens"))
        return True

def verarquivo():
    if os.path.isfile("lista.txt"):
        return True
    else:
        arquivo = open('lista.txt', 'w', encoding="utf-8")
        arquivo.close()
        return False

def gerapastas():
    if os.path.isfile("aviso.jpg"):
        for y in parts:
            os.mkdir(os.path.join("Itens", y))
            shutil.copy("aviso.jpg", os.path.join(caminho, "Itens", y, y + ".jpg"))
            shutil.copy("aviso.jpg", os.path.join(caminho, "Itens", y, "EMB " + y + ".jpg"))
        mess("Quantidade de pastas criadas: {}!".format(len(parts)))
    else:
        mess("Arquivo aviso.jpg não encontrado")

if __name__ == "__main__":
    gerador_de_pastas()
