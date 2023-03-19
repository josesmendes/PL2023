import re
import ply.lex as lex


def main():
    tokens = ('LEVANTAR', 'POUSAR', 'ABORTAR', 'MOEDA', 'T', 'VCOINS', 'TYPE')
    t_LEVANTAR = r'LEVANTAR'
    t_POUSAR = r'POUSAR'
    t_ABORTAR = r'ABORTAR'
    t_MOEDA = r'MOEDA'
    t_TYPE = r'[e|c]'
    t_VCOINS = r'\d+[e|c]'

    def t_T(t):
        r'T=\d+'
        t.value = t.value[2:]
        return t
    t_ignore = ' \t\n,'

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    lexer = lex.lex()
    levantado = False
    interacao = True
    saldo = 0
    while interacao:
        lexer.input(input())
        resposta = ""
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            if not levantado:
                if tok.type == 'LEVANTAR':
                    levantado = True
                    resposta = "cliente levantou"
            else:
                if tok.type == 'POUSAR':
                    resposta = "cliente pousou devolver o salde : " + str(saldo)
                    interacao = False
                elif tok.type == 'ABORTAR':
                    interacao = False
                    resposta = "devolver o salde : " + str(saldo)
                elif tok.type == 'MOEDA':
                    invalido = []
                    while True:
                        tok = lexer.token()
                        if not tok:
                            break  # No more input
                        elif tok.type == 'VCOINS':
                            valid = [1, 2, 5, 10, 20, 50]
                            valor = int(str(tok.value)[:-1])
                            if valor in valid:
                                resposta = "moeda valida"
                                if str(tok.value[-1]) == 'e':
                                    valor *= 100
                                saldo += valor
                            else:
                                invalido.append(tok.value)
                                resposta = "moeda invalida"
                    resposta = f"{invalido} - moeda invalida; saldo = {int((saldo-saldo%100)/100)}e{saldo%100}c"
                elif tok.type == 'T':
                    if re.match(r'601|641', tok.value):
                        resposta = "Esse número não é permitido neste telefone. Queira discar novo número!"
                    if re.match(r'00', tok.value):
                        if saldo < 150:
                            resposta = f"Saldo insuficiente. Necessita de mais{150-saldo}centimos"
                        else:
                            saldo -= 150
                            resposta = f"Saldo = {int((saldo-saldo%100)/100)}e{saldo%100}c"
                    if re.match(r'2', tok.value):
                        if len(tok.value) == 9:
                            if saldo < 25:
                                resposta = f"Saldo insuficiente. Necessita de mais{25-saldo}centimos"
                            else:
                                saldo -= 25
                                resposta = f"Saldo = {int((saldo-saldo%100)/100)}e{saldo%100}c"
                        else:
                            resposta = "número demasiado pequeno"
                    if re.match(r'800', tok.value):
                        if len(tok.value) == 9:
                            resposta = f"Chamada grátis. Saldo = {int((saldo-saldo%100)/100)}e{saldo%100}c"
                        else:
                            resposta = "número demasiado pequeno"
                    if re.match(r'808', tok.value):
                        if len(tok.value) == 9:
                            if saldo < 10:
                                resposta = f"Saldo insuficiente. Necessita de mais {10 - saldo} centimos"
                            else:
                                saldo -= 10
                                resposta = f"Saldo = {int((saldo - saldo % 100) / 100)}e{saldo % 100}c"
                        else:
                            resposta = "número demasiado pequeno"
        print(f"maq: {resposta}")
    print(f"maq: fim interaçao")


if __name__ == "__main__":
    main()
