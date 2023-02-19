from os.path import exists


def por_doenca(path):
    fst = True
    doente = [0, 0]
    saudvl = [0, 0]
    file = open(path, 'r')
    for line in file.readlines():
        if fst:
            fst = False
        else:
            parsed = line.split(',')
            if int(parsed[5]) == 1:
                if parsed[1] == 'M':
                    doente[0] += 1
                else:
                    doente[1] += 1
            else:
                if parsed[1] == 'M':
                    saudvl[0] += 1
                else:
                    saudvl[1] += 1
    file.close()
    print(doente)
    print(saudvl)


def por_idade(path):
    fst = True
    doente = {}
    saudvl = {}
    file = open(path, 'r')
    for line in file.readlines():
        if fst:
            fst = False
        else:
            parsed = line.split(',')
            if int(parsed[5]) == 1:
                escalao = int(parsed[0]) // 5
                val = doente.get(escalao)
                if val is None:
                    doente[escalao] = 1
                else:
                    doente[escalao] = val + 1
            # else:
            #  val = doente.get(x)
            #         if val is None:
            #             val = 0  escalao = int(parsed[0]) // 5
            #    val = saudvl.get(int(parsed[0]) // 5)
            #    if val is None:
            #        saudvl[escalao] = 1
            #    else:
            #        saudvl[escalao] = val + 1
    file.close()
    print('-----------------porIdade------------------')
    for x in range(0, max(doente.keys()) + 1):
        val = doente.get(x)
        if val is None:
            val = 0
        print(f"[{x * 5}-{((x + 1) * 5) - 1}]-->{val}")
    # print(doente)
    # print(saudvl)


def por_col(path):
    fst = True
    doente = {}
    saudvl = {}
    file = open(path, 'r')
    for line in file.readlines():
        if fst:
            fst = False
        else:
            parsed = line.split(',')
            if int(parsed[5]) == 1:
                escalao = int(parsed[3]) // 10
                val = doente.get(escalao)
                if val is None:
                    doente[escalao] = 1
                else:
                    doente[escalao] = val + 1
            # else:
            #   escalao = int(parsed[3])//10
            #  val = saudvl.get(escalao)
            # if val is None:
            #    saudvl[escalao] = 1
            # else:
            #   saudvl[escalao] = val + 1
    file.close()
    print('-----------------Colesterol------------------')
    for x in range(0, max(doente.keys()) + 1):
        val = doente.get(x)
        if val is None:
            val = 0
        print(f"[{x * 10}-{((x + 1) * 10) - 1}]-->{val}")
    # print(doente)
    # print(saudvl)


def main():
    path = '/home/me/PL2023/TPC1/myheart.csv'
    if exists(path):
        por_doenca(path)
        por_idade(path)
        por_col(path)


if __name__ == "__main__":
    main()
