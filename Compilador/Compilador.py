# IMPORTANTE: Durante a análise sintática, não chamamos a função responsável pela análise léxica porque ela já foi executada, o que 
# vai contra a proposto inicial do trabalho na qual teríamos que chamar a função scanner quando precisasse na análise sintática.
# Por isso foi criado uma lista com todas tokens reconhecidos pela analisador léxico para que sejá usada na análise sintática. E não 
# garantimos que o analisador sintático consiga tratar todos os erros possíveis. Por isso, pode acontecer uma falha caso 
# altere o código fonte com algum tipo de erro que não conseguimos prever.

# < ---------------------------- Léxico ---------------------------- >
# Implementando o dicionário de dados
# cada linha da tabela de transição corresponde a um estado começando em q0. As colunas representam as transições.
# Visualização _|D |L |. |.....
#             q0|  |  |  |....
#             q1|  |  |  |.....

Tabela_de_Transição = [ 
    [1, 9, None, 10, None, 7, None, 0, 0, 0, 17, 19, 13, 13, 13, 13, 14, 15, 16, 18, 9, 9, None, None],
    [1, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None,
     4, 4, None],
    [3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, 4, 4, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, 5, 5, None, None, None, None, None, None,
     None, None, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None],
    [9, 9, 9, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9,
     9, None],
    [10, 10, 10, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, 18, 20, None, None, None, None, None, None, 18,
     None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     18, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None]
]

# o que se encontra entre '' na deifinição do alfabeto é o caracter lido no arquivo txt "fonte.txt." que se encontra na mesma pasta deste que este código. Já o número que se encontra
# após ':' é a coluna correspondente ao caracter lido. Os número se encontram na coluna 0 da tabela, enquanto o alfabeto se encontra na coluna 1.
# os demais caracteres como '>', '<', etc possuem cada um uma coluna para si.
# Desta forma quando lemos o caracter entre '' o programa vê o valor da coluna correspondente. Ambos serão usados mais a frente na função scanner

alfabeto = {
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,
    'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 21, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
    'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1,
    'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 20, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 1, 'M': 1,
    'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1,
    '_': 2,
    '{': 3,
    '}': 4,
    '"': 5,
    '.': 6,
    ' ': 7,
    '\t': 8,
    '\n': 9,
    '<': 10,
    '>': 11,
    '-': 12,
    '+': 13,
    '*': 14,
    '/': 15,
    '(': 16, 
    ')': 17,
    ';': 18,
    '=': 19,
    ':': 22,
    '\\': 23
}

lista = []

# Aqui é especificado os estados finais to autômato e o tipo de lexema que é gerado nesse estado final
estados_finais = {
    1: 'num',
    3: 'num',
    6: 'num',
    8: 'literal',
    9: 'id',
    11: 'comentario',
    12: 'EOF',  # fim de arquivo
    13: 'opm',
    14: 'ab_p',  # abre parêntese
    15: 'fc_p',  # fecha parêntese
    16: 'pt_v',  # ponto e vírgula
    17: 'opr',
    18: 'opr',  # operador
    19: 'opr',
    20: 'rcb',
    21: "Erro"
}

#IMPORTANTE para o Semântico
tipo_estados_finais = {
    1: 'int',
    3: 'float',
    6: 'float',
    8: 'string',
    9: None,
    11: None,
    12: None,  
    13: None,
    14: None,  
    15: None,  
    16: None,  
    17: None,
    18: None,  
    19: None,
    20: None,
    21: None
}

# erros léxicos
estados_erros = {
    0: 'Caminho não reconhecido',
    2: 'Numeral incorreto',
    4: 'Numeral incorreto',
    5: 'Numeral incorreto',
    7: 'Literal incorreto',
    10: 'Comentário Incorreto'
}

# aqui é listado o token e como ele é visto no arquivo. Ex: inicio no arquivo pode ser lido como inicio
tabela_token_part1 = {
    'inicio': 'inicio',
    'varinicio': 'varinicio',
    'varfim': 'varfim',
    'escreva': 'escreva',
    'leia': 'leia',
    'se': 'se',
    'entao': 'entao',
    'fimse': 'fimse',
    'fim': 'fim',
    'inteiro': 'inteiro',
    'lit': 'lit',
    'real': 'real'
}

# aqui é listado o tipo de cada token, completando o dicionário tabela_token_part1
tabela_token_part2 = {
    'inicio': None,
    'varinicio': None,
    'varfim': None,
    'escreva': None,
    'leia': None,
    'se': None,
    'entao': None,
    'fimse': None,
    'fim': None,
    'inteiro': None,
    'lit': None,
    'real': None
}

#Aqui começa qa função que faz o papel de analisador léxico
def scanner(conteudo, length):

    global verificador
    estadoatual = 0
    aux = 0
    ponteiro = 0
    lexema = ""
    linha = 1
    coluna = 1
    
    # Vai percorrer todo o arquivo lendo caracter por acaracter até um espaço vazio. Quando cheganoespaço vazio verifica o tipo e o token do lexema
    # e printa na tela.
    #Quando encontra uma transição não existente dentro da tabela de transição, é exibida a linha e a coluna onde o erro ocorreu, o que gerou o erro e o
    #tipo de erro especificado no dicionário 'erros léxicos'
    while(ponteiro < length):
        if (conteudo[aux] not in alfabeto):
            print("----------------------------------")
            print("Caracter inválido do alfabeto")
            verificador = False
            print("Na linha: ", linha, ". Na coluna: ", coluna)
            print("----------------------------------")
            estadoatual = 0
            ponteiro += 1
            aux += 1
            lexema = ""
        else:
            
            a = Tabela_de_Transição[estadoatual][alfabeto[conteudo[aux]]]

            if a is None and estadoatual in estados_finais:
                if (estados_finais[estadoatual] != 'id'):
                    saida = "Lexema: " + lexema + "\tToken: " + estados_finais[estadoatual] + "\tTipo: " + str(tipo_estados_finais[estadoatual])
                    lista.insert(ponteiro, [estados_finais[estadoatual], lexema, str(tipo_estados_finais[estadoatual]), linha, coluna])
                    #fazer uma fila dos tokens
                else:
                    if (lexema in tabela_token_part1):
                       saida = "Lexema: " + lexema + "\tToken: " + tabela_token_part1[lexema] + "\tTipo: " + str(tabela_token_part2[lexema])
                       lista.insert(ponteiro, [tabela_token_part1[lexema], lexema, str(tipo_estados_finais[estadoatual]), linha , coluna])
                       #fazer uma fila dos tokens
                    else:
                       # Quando um id é lido e não está na tabela de símbolos ele é adicionado
                        saida = "Lexema: " + lexema + "\tToken: " + estados_finais[estadoatual] + "\tTipo: " + str(tipo_estados_finais[estadoatual])
                        lista.insert(ponteiro, [estados_finais[estadoatual], lexema, str(tipo_estados_finais[estadoatual]), linha, coluna])
                        #fazer uma fila dos tokens
                        tabela_token_part1[lexema] = estados_finais[estadoatual]
                        tabela_token_part2[lexema] = None
                estadoatual = 0
                lexema = ""
            elif (a is None) and (estadoatual not in estados_finais):
                print("----------------------------------")
                print(estados_erros[estadoatual])
                verificador = False
                print("Na linha ", linha, "e coluna ", coluna)
                print("----------------------------------")
                estadoatual = 0
                ponteiro += 1
                aux += 1
                coluna += 1
                lexema = ""
            elif (estadoatual == 10 and ponteiro == (length -1)):
                print("----------------------------------")
                print(estados_erros[estadoatual])
                verificador = False
                print(" \nNa linha ", linha, "e coluna ", coluna)
                print("----------------------------------")
                
                ponteiro += 1
            elif (estadoatual == 7) and ponteiro == (length -1): 
                print("----------------------------------")
                print(estados_erros[estadoatual])
                verificador = False
                print("\nNa linha ", linha, "e coluna ", coluna)
                print("----------------------------------")
                
                ponteiro += 1           
            else:
                if ((a == 0) and (conteudo[aux] == "\n" or conteudo[aux] == "\t" or conteudo[aux] == " ")):
                    if conteudo[aux] == "\n":
                        linha += 1
                        coluna = 1
                else: 
                    lexema = lexema + conteudo[aux]
                estadoatual = a
                aux += 1
                ponteiro += 1
                coluna += 1

    lista.insert(length, ["EOF", None, None, linha, 0])



# < ---------------------------- Sintático ---------------------------->
tabela_Goto = [
[1,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,3,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,5,6,None,7,None,None,8,13,None,None],
[None,None,15,16,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,19,6,None,7,None,None,8,13,None,None],
[None,None,None,None,None,21,6,None,7,None,None,8,13,None,None],
[None,None,None,None,None,22,6,None,7,None,None,8,13,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,25,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,31,None,32,None,None,33,13,None,30],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,36,16,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,38,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,42,43,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,31,None,32,None,None,33,13,None,46],
[None,None,None,None,None,None,31,None,32,None,None,33,13,None,47],
[None,None,None,None,None,None,31,None,32,None,None,33,13,None,48],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,50,None,None,49,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,56,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,58,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
]

tabela_action = [
['S2','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1'],
['E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','ACC'],
['E2','S4','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2'],
['E3','E3','E3','E3','S12','E3','E3','E3','S10','S11','E3','E3','E3','E3','S14','E3','E3','E3','E3','E3','S9','E3'],
['E17','E17','S17','E17','S18','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','R2'],
['E3','E3','E3','E3','S12','E3','E3','E3','S10','S11','E3','E3','E3','E3','S14','E3','E3','E3','E3','E3','S9','E3'],
['E3','E3','E3','E3','S12','E3','E3','E3','S10','S11','E3','E3','E3','E3','S14','E3','E3','E3','E3','E3','S9','E3'],
['E3','E3','E3','E3','S12','E3','E3','E3','S10','S11','E3','E3','E3','E3','S14','E3','E3','E3','E3','E3','S9','E3'],
['E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','R30'],
['E16','E16','E16','E16','S23','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16'],
['E4','E4','E4','E4','S28','E4','E4','E4','E4','E4','S26','S27','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4'],
['E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','S29','E15','E15','E15','E15','E15','E15','E15','E15','E15'],
['E9','E9','E9','E9','S12','E9','E9','E9','S10','S11','E9','E9','E9','E9','S14','E9','E9','E9','E9','S34','E9','E9'],
['E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','S35','E7','E7','E7','E7','E7','E7'],
['E17','E17','E17','E17','R3','E17','E17','E17','R3','R3','E17','E17','E17','E17','R3','E17','E17','E17','E17','E17','R3','E17'],
['E5','E5','S17','E5','S18','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5'],
['E6','E6','E6','S37','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6'],
['E10','E10','E10','E10','E10','S39','S40','S41','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10'],
['E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','R10'],
['E17','E17','E17','E17','R12','E17','E17','E17','R12','R12','E17','E17','E17','E17','R12','E17','E17','E17','E17','R12','R12','E17'],
['E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','R16'],
['E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','R22'],
['E6','E6','E6','S24','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6'],
['E17','E17','E17','E17','R11','E17','E17','E17','R11','R11','E17','E17','E17','E17','R11','E17','E17','E17','E17','R11','R11','E17'],
['E6','E6','E6','S20','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6'],
['E17','E17','E17','R13','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E17','E17','E17','R14','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E17','E17','E17','R15','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E8','E8','E8','E8','S44','E8','E8','E8','E8','E8','E8','S45','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'],
['E17','E17','E17','E17','R23','E17','E17','E17','R23','R23','E17','E17','E17','E17','R23','E17','E17','E17','E17','R23','R23','E17'],
['E9','E9','E9','E9','S12','E9','E9','E9','S10','S11','E9','E9','E9','E9','S14','E9','E9','E9','E9','S34','E9','E9'],
['E9','E9','E9','E9','S12','E9','E9','E9','S10','S11','E9','E9','E9','E9','S14','E9','E9','E9','E9','S34','E9','E9'],
['E9','E9','E9','E9','S12','E9','E9','E9','S10','S11','E9','E9','E9','E9','S14','E9','E9','E9','E9','S34','E9','E9'],
['E17','E17','E17','E17','R29','E17','E17','E17','R29','R29','E17','E17','E17','E17','R29','E17','E17','E17','E17','R29','R29','E17'],
['E8','E8','E8','E8','S44','E8','E8','E8','E8','E8','E8','S45','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'],
['E17','E17','E17','E17','R4','E17','E17','E17','R4','R4','E17','E17','E17','E17','R4','E17','E17','E17','E17','R4','R4','E17'],
['E17','E17','E17','E17','R5','E17','E17','E17','R5','R5','E17','E17','E17','E17','R5','E17','E17','E17','E17','R5','R5','E17'],
['E6','E6','E6','S51','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6'],
['E17','E17','E17','R7','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E17','E17','E17','R8','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E17','E17','E17','R9','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E6','E6','E6','S52','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6'],
['E14','E14','E14','R19','E14','E14','E14','E14','E14','E14','E14','E14','E14','S53','E14','E14','E14','E14','E14','E14','E14','E14'],
['E17','E17','E17','R20','E17','E17','E17','E17','E17','E17','E17','E17','E17','R20','E17','E17','R20','E17','R20','E17','E17','E17'],
['E17','E17','E17','R21','E17','E17','E17','E17','E17','E17','E17','E17','E17','R21','E17','E17','R21','E17','R21','E17','E17','E17'],
['E17','E17','E17','E17','R26','E17','E17','E17','R26','R26','E17','E17','E17','E17','R26','E17','E17','E17','E17','R26','R26','E17'],
['E17','E17','E17','E17','R27','E17','E17','E17','R27','R27','E17','E17','E17','E17','R27','E17','E17','E17','E17','R27','R27','E17'],
['E17','E17','E17','E17','R28','E17','E17','E17','R28','R28','E17','E17','E17','E17','R28','E17','E17','E17','E17','R28','R28','E17'],
['E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','S54','E12','E12','E12','E12','E12'],
['E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','E13','S55','E13','E13','E13'],
['E17','E17','R6','E17','R6','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E17','E17','E17','E17','R17','E17','E17','E17','R17','R17','E17','E17','E17','E17','R17','E17','E17','E17','E17','R17','R17','E17'],
['E8','E8','E8','E8','S44','E8','E8','E8','E8','E8','E8','S45','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'],
['E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','S57','E11','E11','E11','E11'],
['E8','E8','E8','E8','S44','E8','E8','E8','E8','E8','E8','S45','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'],
['E17','E17','E17','R18','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'],
['E17','E17','E17','E17','R24','E17','E17','E17','R24','R24','E17','E17','E17','E17','R24','E17','E17','E17','E17','R24','E17','E17'],
['E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','R25','E17','E17','E17','E17','E17']
]

dicionario_actions = {
    'inicio': 0,
    'varinicio': 1,
    'varfim': 2,
    'pt_v': 3,
    'id': 4,
    'inteiro': 5,
    'real': 6,
    'lit': 7,
    'leia': 8,
    'escreva': 9,
    'literal': 10,
    'num': 11,
    'rcb': 12,
    'opm': 13,
    'se': 14,
    'ab_p': 15,
    'fc_p': 16,
    'entao': 17,
    'opr': 18,
    'fimse': 19,
    'fim': 20,
   'EOF': 21
}

# Ao verificar o não terminal da análise sintática, a função verifica qual a posição do não terminal na tabela
dicionario_goto = {
    'P': 0,
    'V': 1,
    'LV': 2,
    'D': 3,
    'TIPO': 4,
    'A': 5,
    'ES': 6,
    'ARG': 7,
    'CMD': 8,
    'LD': 9,
    'OPRD': 10,
    'COND': 11,
    'CABEÇALHO': 12,
    'EXP_R': 13,
    'CORPO':14
}

# Regras da gramática entregues pela professora. a chave é o número da regra na gramática
# O primeiro valor entre os colchetes é a quantidade de símbolos a esquerda da regra. Eles representam o número de estados que será tirado da pilha quando a redução for feita
# O símbolo entre '' é o não terminal a direita da regra
gramatica = { 
    2: [3, 'P'],
    3: [2, 'V'],
    4: [2, 'LV'],
    5: [2, 'LV'],
    6: [3, 'D'],
    7: [1, 'TIPO'],
    8: [1, 'TIPO'],
    9: [1, 'TIPO'],
    10: [2, 'A'],
    11: [3, 'ES'],
    12: [3, 'ES'],
    13: [1, 'ARG'],
    14: [1, 'ARG'],
    15: [1, 'ARG'],
    16: [2, 'A'],
    17: [4, 'CMD'],
    18: [3, 'LD'],
    19: [1, 'LD'],
    20: [1, 'OPRD'],
    21: [1, 'OPRD'],
    22: [2, 'A'],
    23: [2, 'COND'],
    24: [5, 'CABEÇALHO'],
    25: [3, 'EXP_R'],
    26: [2, 'CORPO'],
    27: [2, 'CORPO'],
    28: [2, 'CORPO'],
    29: [1, 'CORPO'],
    30: [1, 'A']
}

reducoes = { 
    2: 'P -> inicio V A',
    3: 'V -> varinicio LV',
    4: 'LV -> D LV',
    5: 'LV -> varfim;',
    6: 'D -> id TIPO;',
    7: 'TIPO -> int',
    8: 'TIPO -> real',
    9: 'TIPO -> lit',
    10: 'A -> ES A',
    11: 'ES -> leia id;',
    12: 'ES -> escreva ARG;',
    13: 'ARG -> literal',
    14: 'ARG -> num',
    15: 'ARG -> id',
    16: 'A -> CMD A',
    17: 'CMD -> id rcb LD;',
    18: 'LD -> OPRD opm OPRD',
    19: 'LD -> OPRD',
    20: 'OPRD -> id',
    21: 'OPRD -> num',
    22: 'A -> COND A',
    23: 'COND -> CABEÇALHO CORPO',
    24: 'CABEÇALHO -> se (EXP_R) então',
    25: 'EXP_R -> OPRD opr OPRD',
    26: 'CORPO -> ES CORPO',
    27: 'CORPO -> CMD CORPO',
    28: 'CORPO -> COND CORPO',
    29: 'CORPO -> fimse',
    30: 'A -> fim'
}

# Tipos de erros sintáticos referenciados na matriz com as transições de estado da análise sintática, no caso a atabela tabela_action
erros_sintaticos = {
    'E1' : 'Esperando início',
    'E2' : 'Esperando varinicio',
    'E3' : 'Esperando escreva, id, leia,, fim ou se',
    'E4' : 'Esperando literal, num ou id',
    'E5': 'Esperando varfim ou id',
    'E6' : 'Esperando ;',
    'E7' : 'Esperando (',
    'E8' : 'Esperando id ou num',
    'E9' : 'Esperando id, leia, escreva, fimse ou se',
    'E10' : 'Esperando int, real ou lit',
    'E11' : 'Esperando então',
    'E12' : 'Esperando )',
    'E13' : 'Esperando opr',
    'E14' : 'Esperando opm',
    'E15' : 'Esperando rcb',
    'E16' : 'Esperando id',
    'E17' : 'Erro de redução'
}

tipos_de_Erro_reducao = {
    5: 'Erro de redução, espera: leia, escreva, se, id ou fim',
    15: 'Erro de redução, espera: leia, escreva, se, id ou fim',
    36: 'Erro de redução, espera: leia, escreva, se, id ou fim',
    37: 'Erro de redução, espera: leia, escreva, se, id ou fim',
    51: 'Erro de redução, espera: id ou varfim',
    39: 'Erro de redução, espera: ;',
    40: 'Erro de redução, espera: ;',
    41: 'Erro de redução, espera: ;',
    19: 'Erro de redução, espera: $',
    24: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    20: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    26: 'Erro de redução, espera: ;',
    27: 'Erro de redução, espera: ;',
    28: 'Erro de redução, espera: ;',
    21: 'Erro de redução, espera: $',
    52: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    56: 'Erro de redução, espera: ;',
    43: 'Erro de redução, espera: ;',
    44: 'Erro de redução, espera: opm, ;, opr, )',
    45: 'Erro de redução, espera: opm, ;, opr, )',
    22: 'Erro de redução, espera: $',
    30: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    57: 'Erro de redução, espera: leia, escreva, se, id ou fim',
    58: 'Erro de redução, espera: )',
    46: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    47: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    48: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    34: 'Erro de redução, espera: leia, escreva, se, id, fim ou fimse',
    9: 'Erro de redução, espera: $'
}

# Função do analisador sintático
# Referente ao pseudocódigo presente no slida professora
def parser():

    global pilha_semantica, atributos, verificador
    #  Seja a o primeiro símbolo de w$
    ponteiro = 0
    a = lista[ponteiro]
    token = a[0]
    pilha = [0]

    while(True):

        # Seja s o estado ao topo da pilha
        s = int(pilha[0])
        # Verifica qual a coluna do token na tabela e busca a ação na a ser feita na tabela "tabela_action"
        coluna = dicionario_actions[token]
        tipo_action = tabela_action[s][coluna]

        # Verifica se a ação na tabela de transição é um shift com base no valor ao topo da pilha
        if(tipo_action[0] == 'S'):

            #Insere o estado da ação do shift no topo da pilha
            pilha.insert(0, int(tipo_action[1:]))
            # O estado t que é o estado do lido nas codições dadas, é adicionado ao topo da pilha
            t = int(pilha[0])

            #Empilhando terminais na pilha semântico com seus atributos
            if(token != 'pt_v'):

                atributos = [token, a[1], a[2], a[3], a[4]]
                pilha_semantica.insert(0, atributos)
                pilha_semantica.insert(0, token)

            ## como não estamos chamando a funão do léxico, que já foi executada antes de iniciar a análise sintática, precisamos de uma 
            # variável que busque na lista criada com as saídas geradas pelo léxico o token solicitado
            ponteiro += 1
            a = lista[ponteiro]
            #a recebe o próximo símbolo da entrada
            token = a[0]
        
        # Verifica se a ação na tabela de transição é um reduce com base no valor ao topo da pilha
        elif(tipo_action[0] == 'R'):

            # Na redução os dicionários 'gramatica' e 'dicionario_goto' são chamadas para verificar quantos estados da pilha devem ser removidos para que a redução seja feita
            # o estado t vai para o topo da pilha e estado da tabela 'tabela_Goto' é empilhado no topo da pilha
            # No final, a redução é exibida na tela
           reduz = int(tipo_action[1:])

           # Se a redução estiver contida na tabela "gramática" a função atribui a quantidade de desempilhamentos a 
           # serem feitos e o não terminal do lado esquerdo da gramática
           if(reduz in gramatica):

               lado_esquerdo = gramatica.get(reduz)
               numero = lado_esquerdo[0]
               not_terminal = lado_esquerdo[1]
            
            # Desempilha
           for i in range(numero):

               pilha.pop(0)

           t = int(pilha[0])

           # Busca a transição do não terminal
           tipo_goto = tabela_Goto[t][dicionario_goto[not_terminal]]
           #Empilha o valor encontrado na tabela e imprime a redução
           pilha.insert(0, int(tipo_goto))
           #Chama o token, lexema, tipo, linha e coluna
               
           semantico(reduz, not_terminal, a[3])
           
        # Verifica se a ação na tabela de transição é um estado de aceitação com base no valor ao topo da pilha
        # Aqui a análise deve terminar
        elif(tipo_action == 'ACC'):

            print("--------------------------------------")
            print("Entrada Aceita")
            print("--------------------------------------")
            break

        else:
            
            # Erro de redução
            # Quando encontra um erro faz a busca pelos seguintes do não terminal da gramática
            print("--------------------------------------")
            verificador = False
            if(tipo_action == 'E17'):
                
                print("Erro Sintático: ", tipos_de_Erro_reducao.get(s))
                tipo_erro = tipos_de_Erro_reducao.get(s)

            else:
                print("Erro Sintático: ", erros_sintaticos[tipo_action])

            print("Na linha = ", a[3])
            print("Na coluna = ", a[4])

            print("--------------------------------------")

            #Rotina de erro
            #39 or 40 or 41 or 26 or 27 or 28 or 56 or 43                     
            #Nessa rotina, se o token estiver errado, o token esperado é lido para que continue a análise
            39 or 40 or 41 or 26 or 27 or 28 or 56 or 43
            if((tipo_action == 'E17' and (s == 39 or s == 40 or s == 41 or s == 26 or s == 27 or s == 28 or s == 56 or s == 43 )) or tipo_action == 'E6'):
                token = 'pt_v'
                ponteiro -= 1
                a = lista[ponteiro]
            elif((tipo_action == 'E17' and s == 58) or tipo_action == 'E12'):
                token = 'fc_p'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E1'):
                token = 'inicio'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E7'):
                token = 'ab_p'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E2'):
                token = 'varinicio'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E16'):
                token = 'id'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E11'):
                token = 'entao'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E15'):
                token = 'rcb'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E14'):
                token = 'opm'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E13'):
                token = 'opr'
                ponteiro -= 1
                a = lista[ponteiro]
            elif(tipo_action == 'E17' and s == 39):
                token = 'opr'
                ponteiro -= 2
                a = lista[ponteiro]
            else:
                while True:
                    ponteiro += 1
                    a = lista[ponteiro]
                    token = a[0]

                    #Tokens de sincronização. Quando encontra um erro o analisador sintáticobusca da lista de tokens pelo token de sincronização
                    #Quando ele é encontrado, o parser desenpilha o topo da pilha
                    if(token == 'pt_v' or token == 'fc_p' or token == 'id'  or token == 'fimse' or token == 'fim'):
                        pilha.pop(0)
                        break




# < ---------------------------- Semântico ---------------------------- >

objeto = ''
pilha_semantica = []
pilha_auxiliar = []
temp = 0
verificador = True


#Confere o tipo da variável declarada no Mgol e faz a troca para o equivalente em C
def tipo_tabelaDeSimbolos(tipo):

    global pilha_semantica, atributos
    tipoAtributo = None
    if(tipo == 'inteiro'):
        tipoAtributo = 'int'
    elif(tipo == 'real'):
        tipoAtributo = 'float'
    elif(tipo == 'lit'):
        tipoAtributo = 'string'

    #Adiciona o tipo lido a tabela de tipos dos tokens lidos no léxico
    tabela_token_part2[tipo] = tipoAtributo
    
    atributos = pilha_semantica[3]
    atributos[2] = tipoAtributo
    pilha_semantica[3] = atributos

    tabela_token_part2[atributos[1]] = tipoAtributo

def semantico(reduz, not_Terminal, linhaErro):
    
    global objeto, pilha_semantica, pilha_auxiliar, atributos, temp, verificador
    arquivo = open('codigo.c', 'w')

    #Aqui se inicia a verificação da redução feita no sintático. Cada redução possui sua particularidade e será tratada dentro de cada if descrito
    if(reduz == 5):

        if(verificador == True):

            objeto = objeto + '\n\n\n'

    elif(reduz == 6):

        # id.tipo <- TIPO.tipo
        atributos = pilha_semantica[3]
        lexema = atributos[1]
        tipo = atributos[2]
        pilha_semantica.pop(0)
        atributos = pilha_semantica[2]
        pilha_semantica.insert(0, lexema)
        if(tipo == 'string'):

            if(verificador == True):
            
                    objeto = objeto + "\tliteral" + ' ' + str(lexema) + ';\n'

        else:
            
            if(verificador == True):

                objeto = objeto + "\t" + str(tipo) + ' ' + str(lexema) + ';\n'

        for i in range(4):
            
            pilha_semantica.pop(0)


    elif(reduz == 7 or reduz == 8 or reduz == 9):

        pilha_semantica.pop(0)
        pilha_semantica.insert(0, not_Terminal)
        atributos = pilha_semantica[1]
        tipo = atributos[0]
        tipo_tabelaDeSimbolos(tipo)

    elif(reduz == 11):
       
        # Verifica o tipo do token e faz a impressão da linha de scanf do código em C para que o valor da variável criada seja recebido
        atributos = pilha_semantica[1]
        atributos[2] = tabela_token_part2[atributos[1]]
        pilha_semantica[1] = atributos
        if(atributos[2] != None):

            if(atributos[2] == 'string'):

                if(verificador == True):
                    objeto = objeto + '\tscanf("%s", ' + '&' + str(atributos[1]) + ');\n'
            
            elif(atributos[2] == 'int'):

                if(verificador == True):
                    objeto = objeto + '\tscanf("%d", ' + '&' + str(atributos[1]) + ');\n'

            elif(atributos[2] == 'float'):

                if(verificador == True):
                    objeto = objeto + '\tscanf("%lf", ' + '&' + str(atributos[1]) + ');\n'
        else:

            # Acho chegar a esse momento do código todas as variáveis daclaradas terão um tipo dentro do dicionário de tipos. Caso ainda não haja um tipo
            # é porque a variável ainda não foi declarada. Sendo assim um erro deve ser exibido em tela.
            print("--------------------------------------")
            print('Erro: Variável não declarada')
            verificador = False
            atributos = pilha_semantica[1]
            print("Na linha: ", linhaErro)
            print("--------------------------------------")

        for i in range(4):
            
            #remove os dois primeiros elementos da pilha. Como adiciomos uma lista dentro de outra (na verdade apontamos) a instrução pop() só entende a necessidade
            # de remover uma das listas. Sendo assim, a lista que foi passada como atributo permanece como primeiro item da lista quando a a funão pop() é executada
            # É necessário que ela seja executada 4 vezes para os dois primeiros elementos (token e lista) sejam removidos por complet.
            pilha_semantica.pop(0)


    elif(reduz == 12):

        # Imprimir ( printf(“ARG.lexema”); )
        atributos = pilha_semantica[1]
        if(atributos[2] == 'int'):

            if(verificador == True):
                objeto = objeto + '\tprintf("%d", ' + str(atributos[1]) + ');\n'

        elif(atributos[2] == 'float'):

            if(verificador == True):
                objeto = objeto + '\tprintf("%lf", ' + str(atributos[1]) + ');\n'

        elif(atributos[2] == 'string' and atributos[0] == 'id'):

            if(verificador == True):
                objeto = objeto + '\tprintf("%s", ' + str(atributos[1]) + ');\n'

        else:

            if(verificador == True):
                objeto = objeto + '\tprintf(' + str(atributos[1]) + ');\n'

    elif(reduz == 13 or reduz == 14 or reduz == 19 or reduz == 21):
        
        # 13. ARG.atributos <- literal.atributos
        # 14.ARG.atributos <- num.atributos
        # 19. LD.atributos <- OPRD.atributos
        # 21. OPRD.atributos <- num.atributos
        pilha_semantica.pop(0)
        pilha_semantica.insert(0, not_Terminal)

    elif(reduz == 15):
        
        # Verificar se o identificador foi declarado
        atributos = pilha_semantica[1]
        lexema = atributos[1]
        tipo = tabela_token_part2[lexema]
        atributos[2] = tipo
        pilha_semantica[1] = atributos
        atributos = pilha_semantica[1]

        # ARG.atributos ß id.atributos
        if(atributos[2] == 'int' or atributos[2] == 'float' or atributos[2] == 'string'):
            
            pilha_semantica.pop(0)
            pilha_semantica.insert(0, not_Terminal)

        # Erro semântico
        else:

            print("--------------------------------------")
            print("ERRO: A variável não foi declarada")
            verificador = False
            atributos = pilha_semantica[1]
            print("Na linha: ", linhaErro)
            print("--------------------------------------")

    elif(reduz == 17):

        # Verificar se id foi declarado
        atributos = pilha_semantica[5]
        tipo = tabela_token_part2[atributos[1]]
        atributos[2] = tipo
        pilha_semantica[5] = atributos

        # Realizar verificação do tipo entre os operandos id e LD
        if(tipo == 'int' or tipo == 'float' or tipo == 'string'):

            atributos = pilha_semantica[1]
            tamanho = len(atributos)         
            if(tamanho == 2):

                atributos1 = pilha_semantica[1]
                tipo1 = atributos1[1]
                atributos2 = pilha_semantica[5]
                tipo2 = atributos2[2]
                if(tipo1 == tipo2):

                    atributos3 = pilha_semantica[3]
                    if(atributos3[1] == '<-'):

                        #tipo = atributos3[1]
                        pass
                        
                    # Imprimir (id.lexema rcb.tipo LD.lexema)
                    if(verificador == True):
                        objeto = objeto + '\t' + str(atributos2[1]) + ' = ' + str(atributos1[0]) + ';\n'

                # Erro semântico
                else:
                    
                    print("--------------------------------------")
                    print("ERRO: Tipos diferentes para atribuição")
                    print("--------------------------------------")
                    verificador = False
  
            elif(tamanho == 5):

                atributos1 = pilha_semantica[1]
                tipo1 = atributos1[2]
                atributos2 = pilha_semantica[5]
                tipo2 = atributos2[2]
                if(tipo1 == tipo2):

                   #atributos3 = pilha_semantica[3]
                   if(verificador == True):
                       objeto = objeto + '\t' + str(atributos2[1]) + ' = ' + str(atributos[1]) + ';\n'

                # Erro semântico
                else:

                    print("--------------------------------------")
                    print("ERRO: Tipo diferentes para atribuição")
                    print("Na linha: ", linhaErro)
                    print("--------------------------------------")
                    verificador = False
                
        # Erro semântico
        else: 
            print("--------------------------------------")
            print("ERRO: A variável não declarada")
            verificador = False
            atributos = pilha_semantica[5]
            print("Na linha: ", linhaErro)
            print("--------------------------------------")

    elif(reduz == 18):

        atributo1 = pilha_semantica[1]
        atributo2 = pilha_semantica[5]
        atributo3 = pilha_semantica[3]
        
        # Verificar se tipo dos operandos são equivalentes e diferentes de literal
        if(atributo1[2] == atributo2[2]):

            # Imprimir (Tx = OPRD.lexema opm.tipo OPRD.lexema)
            if(verificador == True):
                objeto = objeto +'\t' + str(atributo2[2]) + ' T' + str(temp) + ' = ' + str(atributo2[1]) + ' ' + str(atributo3[1]) + ' ' + str(atributo1[1]) + ';\n'
            
            # Gerar uma variável numérica temporária Tx
            tipo = atributo1[2]
            temp = temp + 1

        # Erro semântico
        else:

            print("--------------------------------------")
            print("ERRO: Operandos com tipos incompátiveis")
            print("Na linha: ", linhaErro)
            print("--------------------------------------")
            verificador = False
            tipo = None

        for i in range(6):

            pilha_semantica.pop(0)
        
        # LD.lexema <- Tx
        atributo = ''
        atributo = atributo + 'T' + str(temp - 1)
        pilha_semantica.insert(0, [atributo, tipo])
        pilha_semantica.insert(0, not_Terminal)

    elif(reduz == 20):

        atributos = pilha_semantica[1]
        lexema = atributos[1]
        tipo = tabela_token_part2[lexema]
        atributos[2] = tipo
        pilha_semantica[1] = atributos
        atributos = pilha_semantica[1]

        # Verificar	se	o	identificador	está	declarado
        if(atributos[2] == 'int' or atributos[2] == 'float' or atributos[2] == 'string'):
            
            # OPRD.atributos <- id.atributos
            pilha_semantica.pop(0)
            pilha_semantica.insert(0, not_Terminal)

        else:

            # Erro semântico
            print("--------------------------------------")
            print("ERRO: A variável não foi declarada")
            verificador = False
            atributos = pilha_semantica[1]
            print("Na linha: ", linhaErro)
            print("--------------------------------------")

    elif(reduz == 23):
        
        # Imprimir	(})	no	arquivo	objeto
        objeto = objeto +'\t}\n'

    elif(reduz == 24):

        # Imprimir	(if(EXP_R.lexema){)	no	arquivo	objeto
        atributo = pilha_semantica[5]
        if(verificador == True):
            objeto = objeto + '\tif(' + str(atributo) + ')\n\t{\n'
        pass

    elif(reduz == 25):

        atributo1 = pilha_semantica[1]
        atributo2 = pilha_semantica[5]
        atributo3 = pilha_semantica[3]

        # Verificar se os tipos de dados de OPRD são iguais ou equivalentes
        if(atributo1[2] == atributo2[2]):


            # Imprimir (Tx = OPRD.lexema opr.tipo OPRD.lexema)
            if(verificador == True):
                objeto = objeto + '\t'+ str(atributo2[2]) + ' T' + str(temp) + ' = ' + str(atributo2[1]) + ' ' + str(atributo3[1]) + ' ' + str(atributo1[1]) + ';\n'
            
            # Gerar uma variável booleana temporária Tx
            temp = temp + 1

        else:

            # Erro semântico
            print("--------------------------------------")
            print("ERRO: Operandos com tipos incompátiveis")
            verificador = False
            print("Na linha: ", linhaErro)
            print("--------------------------------------")

        for i in range(6):

            pilha_semantica.pop(0)
        
        atributo = ''
        atributo = atributo + 'T' + str(temp - 1)
        pilha_semantica.insert(0, atributo)
        pilha_semantica.insert(0, not_Terminal)

    elif(reduz == 2):
       
        if(verificador == True):
            objeto = objeto + '\tsystem("PAUSE");'
            objeto = objeto + "\n}"


    if(verificador == True):
        arquivo.write("#include <stdio.h>\n" + "#include <stdlib.h>\n\n" + "typedef char literal[256];\n" + "void main()\n{\n" + objeto)
    arquivo.close()
    

# < ---------------------------- Main ---------------------------- >
def main():
    
    global objeto
    # Faz a leitura do arquivo "fonte.txt"
    file = open('fonte.txt', 'r')

    if file:
        print("Arquivo Encontrado")
    else:
        print("Arquivo não encontrado")

    conteudo = file.read()

    scanner(conteudo, len(conteudo))
    print("--------------------------------------")
    parser()
    file.close()

main()