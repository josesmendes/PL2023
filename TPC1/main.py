from os.path import exists


def por_doenca(lines):
    homem = [x for x in lines if x[1] == 'M' and x[-1]]
    mulher = [x for x in lines if x[1] == 'F' and x[-1]]
    print(f'Homes-->{len(homem)/len(lines)}\nMulheres-->{len(mulher)/len(lines)}')


def por_idade(lines):
    idade_maxima = max(int(x[0]) for x in lines)
    distrib_idades = {}
    for idade in range(30, idade_maxima, 5):
        pessoas = [x for x in lines if int(x[0]) in range(idade, idade + 5)]
        doentes = [x for x in pessoas if int(x[-1])]
        distrib_idades[(idade, idade + 4)] = len(doentes) / len(pessoas)
    print('-----------------porIdade------------------')
    for x in distrib_idades.keys():
        print(f'{x}-->{distrib_idades.get(x)}')


def por_col(lines):
    colesterol_max = max(int(x[3]) for x in lines)
    colesterol_min = min(int(x[3]) for x in lines if int(x[3]) != 0)
    distrib_col = {}
    print('-----------------Colesterol------------------')
    for colesterol in range(colesterol_min, colesterol_max, 10):
        pessoas = [x for x in lines if int(x[3]) in range(colesterol, colesterol + 10)]
        doentes = [x for x in pessoas if int(x[-1])]
        if pessoas and doentes:
            distrib_col[(colesterol, colesterol + 9)] = len(doentes) / len(pessoas)
        else:
            distrib_col[(colesterol, colesterol + 9)] = 0
    for x in distrib_col.keys():
        print(f'{x}-->{distrib_col.get(x)}')


def main():
    path = '/home/me/PL2023/TPC1/myheart.csv'
    if exists(path):
        valid_lines = []
        with open(path) as file:
            for line in file.readlines()[1::]:
                valid_lines.append(tuple(line.strip().split(',')))
            por_doenca(valid_lines)
            por_idade(valid_lines)
            por_col(valid_lines)


if __name__ == "__main__":
    main()
