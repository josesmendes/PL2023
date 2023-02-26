def main():
    valores = input()
    soma = 0
    word = ['0', '1,', '2']
    is_on = True
    for char in valores:
        word.pop(0)
        word.append(char)
        if not char.isdigit():
            if char == '=':
                print(soma)
            else:
                listToStr = ''.join(map(str, word))
                test = listToStr.upper()
                if test == 'OFF':
                    is_on = False
                elif test[1:] == 'ON':
                    is_on = True
        elif is_on:
            soma += int(char)


if __name__ == "__main__":
    main()
