import json
import re


def main():
    path = '/home/me/PL2023/TPC4/Número,Nome,Curso,Notas'
    with open(path) as file:
        formato = re.findall(r'((\w+)({(\d),(\d)})?(:)*(\w+)?)', file.readline())
        new_f = []
        for line in file.readlines():
            line = line.strip('\n')
            linha = re.split(r',', line)
            lista_dic = {}
            i = 0

            while i < len(linha):
                (_, nome, _, minimo, maximo, _, operacao) = formato[i]
                if minimo and maximo:
                    list_size = int(maximo)
                    lista = []
                    inicial = i
                    while i < inicial+list_size:
                        if linha[i].isdigit():
                            lista.append(int(linha[i]))
                        i += 1
                    if operacao:
                        if operacao == 'sum':
                            lista = sum(lista)
                        elif operacao == 'media':
                            total = sum(lista)
                            lista = total/len(lista)
                    lista_dic[nome] = lista
                else:
                    lista_dic[nome] = linha[i]
                    i += 1
            new_f.append(lista_dic)
    output = open('teste.json', "w")
    output.write("[\n")
    for linha in new_f:
        if linha == new_f[-1]:
            jline = json.dumps(linha)
            jline = re.sub(r'\D,', '",\n\t\t', jline)
            jline = re.sub(r'{', '{\n\t\t', jline)
            jline = re.sub(r'}', '\n\t}', jline)
            output.write('\t' + jline + '\n')
        else:
            jline = json.dumps(linha)
            jline = re.sub(r'\D,', '",\n\t\t', jline)
            jline = re.sub(r'{', '{\n\t\t', jline)
            jline = re.sub(r'}', '\n\t},', jline)
            output.write('\t' + jline + '\n')

    output.write("]")
    output.close()


if __name__ == "__main__":
    main()
