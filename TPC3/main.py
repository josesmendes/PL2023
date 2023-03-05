import re
import json
from os.path import exists


def to_json(lines):
    top_20 = lines[:20]
    new_file = []
    c = re.compile(
        r'(?P<id>\d+)::(?P<data>\d+-\d+-\d+)::(?P<nomeP1>[\w\s]*)?::(?P<nomeP2>[\w\s]*)?::(?P<nomeP3>[\w\s]*)?::(?P<extra>[^:]*)')
    for line in top_20:
        s = c.match(line).groupdict()
        new_file.append(s)
    return json.dumps(new_file)



def relacao(matches):
    # tio avo* , sobreinho , irmaos/irmao, avo, primo(s)
    counter = {'Tio': 0, 'Avo': 0, 'Irmao': 0, 'Primo': 0, 'Sobrinho': 0}
    for line in matches:
        for tipo in counter:
            pattern = rf'\b{tipo}\b'  # construct the regex pattern for the word
            matches = re.findall(pattern, line)
            count = len(matches)
            counter[tipo] += count
    print(counter)


def proc_por_ano(matches, c):
    processos = {}
    for line in matches:
        ano = c.match(line).group('ano')
        if not processos.get(ano):
            processos[ano] = 1
        else:
            processos[ano] += 1
    return processos


def por_seculo(matches, c):
    sec = {}
    nomes = {}
    apelidos = {}

    for line in matches:
        seculo = int(c.match(line).group('ano')) // 100
        if not sec.get(seculo):
            sec[seculo] = dict({'nome': 0, 'apelido': 0})
        for nome in [c.match(line).group('nomeP1'), c.match(line).group('nomeP2'), c.match(line).group('nomeP3')]:
            if not nomes.get(nome):
                nomes[nome] = 1
            else:
                nomes[nome] += 1
            sec[seculo]['nome'] += 1
        for apelido in [c.match(line).group('apelido1'), c.match(line).group('apelido2'),
                        c.match(line).group('apelido3')]:
            if not apelidos.get(apelido):
                apelidos[apelido] = 1
            else:
                apelidos[apelido] += 1
            sec[seculo]['apelido'] += 1
    sorted(sec)
    for anos in sec:
        print(f'seculo {anos}: nomes->{sec[anos]["nome"]} | apelidos->{sec[anos]["apelido"]}')
    sorted_nomes = list(sorted(nomes.items(), key=lambda x: x[1], reverse=True))
    sorted_apelidos = list(sorted(apelidos.items(), key=lambda x: x[1], reverse=True))
    for i in range(0, 5):
        (nome, num) = sorted_nomes[i]
        (apelido, numA) = sorted_apelidos[i]
        print(f'{i + 1}º-> nome:{nome}, {num} vezes | apelido:{apelido}, {numA} vezes')


def main():
    path = '/home/me/PL2023/TPC3/processos.txt'
    if exists(path):
        with open(path) as file:
            c = re.compile(r'(?P<id>\d+)::(?P<ano>\d+)[-\d]+::(?P<nomeP1>\w+)[\s\w]*\s(?P<apelido1>\w+)::('
                           r'?P<nomeP2>\w+)[\s\w]*\s(?P<apelido2>\w+)::(?P<nomeP3>\w+)[\s\w]*\s(?P<apelido3>\w+)::')
            lines = file.readlines()
            matches = [x for x in lines if c.match(x)]
            print('----------------ANO--------------------')
            processos = proc_por_ano(matches, c)
            for ano in processos:
                print(f'{ano}-->{processos[ano]}')
            print('----------------SECULO--------------------')
            por_seculo(matches, c)
            print('----------------RELACAO--------------------')
            relacao(matches)
            print('----------------JSON--------------------')
            js_file = to_json(lines)
            print(js_file)

if __name__ == "__main__":
    main()
