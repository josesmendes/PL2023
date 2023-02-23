def main():
    valores = input()
    soma = 0
    word = ['0', '1,', '2']
    is_on = True
    for char in valores:
        word.pop(0)
        word.append(char)
        if char.isdigit():
            if is_on:
                soma += int(char)
        else:
            if char == '=':
                print(soma)
            else:
                listToStr = ' '.join(map(str, word))
                test = listToStr.upper()
                if test[0] == 'O' and test[2] == 'F' and test[4] == 'F':
                    is_on = False
                elif test[2] == 'O' and test[4] == 'N':
                    is_on = True


if __name__ == "__main__":
    main()
