import re
import ply.lex as lex


def main():
    lista =  []
    variaveis = []
    tokens = ['COMENT', 'FCOMENT', 'ACOMENT', 'OPENCHAV', 'CLOSECHAV', 'FUNCNAME', 'VARIAVEL', 'OPENPARENT',
              'CLOSEPARENT', 'PONTOVIRG', 'FUNCTION', 'MENOS', 'MAIS', 'VEZES', 'VIRGULA', 'PONTO', 'MEANS',
              'MAIN', 'MAINNAME', 'WHILE', 'FOR', 'CORRESPONDE', 'TIPO', 'ARGUMENTO', 'ATE', 'DE', 'FIM',
              'VALOR', 'MAIOR', 'MENOR', 'AVALUES', 'ARRAY', 'VAR', 'IF', 'PRINT', 'ORETOS', 'CRETOS', 'IN']

    t_COMENT = r'//'
    t_FCOMENT = r'\*/'
    t_ACOMENT = r'/\*'
    t_OPENCHAV = r'{'
    t_CLOSECHAV = r'}'
    t_OPENPARENT = r'\('
    t_CLOSEPARENT = r'\)'
    t_FUNCTION = r'function'
    t_FUNCNAME = r'(?<=function\s)\w+'
    t_MAINNAME = r'(?<=program\s)\w+'
    t_MENOS = r'\-'
    t_MAIS = r'\+'
    t_VEZES = r'\*'
    t_PONTOVIRG = r';'
    t_VIRGULA = r','
    t_PONTO = r'\.'
    t_MEANS = r'='
    t_ARGUMENTO = r'(?<=\().+(?=\))'
    t_MAIN = r'program'
    t_WHILE = r'while'
    t_FOR = r'for'
    t_CORRESPONDE = r'='
    t_TIPO = r'\bint\b'
    t_ATE = r'\.\.'
    t_DE = r'(?<=\[)\d+(?=\.\.)'
    t_FIM = r'(?<=\.\.)\d+(?=\])'
    t_MAIOR = r'>'
    t_MENOR = r'<'
    t_ARRAY = r'\w+\[(\d+|\w+)\]'
    t_IF = r'if'
    t_PRINT = r'print'
    t_ORETOS = r'\['
    t_CRETOS = r'\]'
    t_IN = 'in'
    def t_VARIAVEL(t):
        r'(?<=int\ |for\ )\w+'
        variaveis.append(t.value)
        return t

    def t_VAR(t):
        r'\w+(?=\ \=)|(?<=while\ )\w+|(?<=if\ )\w+'
        if t.value in variaveis:
            t.type = 'VARIAVEL'
        return t

    def t_AVALUES(t):
        r"""(?<=\=\ ){(\d+,?)*}"""
        return t

    def t_VALOR(t):
        r"""(?<=\=\ )[^;,{]*|(?<=\<\ )[^;,{]*|(?<=\>\ )[^;,{]*"""
        return t


    t_ignore = ' \t\n'

    def t_error(t):
        #if not aberto_coment:
            #print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    lexer = lex.lex()
    '''
    data = "/* factorial.p\
-- 2023-03-20\
-- by jcr\
*/\
\
int i;\
\
// Função que calcula o factorial dum número n\
function fact(n){\
    int res = 1;\
    while res > 1 {\
        res = res * n;\
        res = res - 1;\
    }\
}\
\
// Programa principal\
program myFact{\
    for i in [1..10]{\
        print(i, fact(i));\
    }\
}"'''
    data = open('data', 'r')
    file = (data.readlines())
    aberto_coment = False
    for line in file:
        lexer.input(line)
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            if tok.type == 'COMENT':
                break
                pass
            if tok.type == 'ACOMENT':
                lista.append(tok)
                aberto_coment = True
            if tok.type == 'FCOMENT':
                aberto_coment = False
            if not aberto_coment:
                lista.append(tok)
                print(tok.type + '-> ' + tok.value + " na frase: " + line)
    print(lista)


if __name__ == "__main__":
    main()
