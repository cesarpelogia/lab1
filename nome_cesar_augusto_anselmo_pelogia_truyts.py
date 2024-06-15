from random import randint

def ler_navios_e_tiros_jogador(arquivo):
    with open(arquivo) as arquivo_jogador:
        linhas = arquivo_jogador.readlines()

    encouracado = linhas[0].strip().replace("1;", "").split("|")
    porta_aviao = linhas[1].strip().replace("2;", "").split("|")
    submarino = linhas[2].strip().replace("3;", "").split("|")
    cruzador = linhas[3].strip().replace("4;", "").split("|")
    tiros = linhas[5].strip().replace("T;", "").split("|")

    navios = [encouracado, porta_aviao, submarino, cruzador]

    return navios, tiros

J1_navios, J1_tiros = ler_navios_e_tiros_jogador("jogador1.txt")
J2_navios, J2_tiros = ler_navios_e_tiros_jogador("jogador2.txt")

J1 = (J1_navios, J1_tiros)
J2 = (J2_navios, J2_tiros)

# Definição dos navios
navios = [
    ("1", ["E", "E", "E", "E"]),  # Encouraçado
    ("2", ["P", "P", "P", "P", "P"]),  # Porta-aviões
    ("3", ["S"]),  # Submarino
    ("4", ["C", "C"])  # Cruzador
]

def validar_navios(navios_jogador):
    limites = {1: 5, 2: 2, 3:10, 4:5}
    for tipo_navio in range(1, 5):
        if len(navios_jogador[tipo_navio - 1]) > limites[tipo_navio]:
            return False
    return True

validacao_navios_j1 = validar_navios(J1_navios)
validacao_navios_j2 = validar_navios(J2_navios)

if not validacao_navios_j1 or not validacao_navios_j2:
    print("ERROR_NR_PARTS_VALIDATION")
    exit(1)
else:
    print("Todos os navios são válidos." "\n")

tabuleiro = []

for _ in range(15):
    linha = ["O"] * 15
    tabuleiro.append(linha)

def exibir_tabuleiro(tabuleiro):
    print("     A B C D E F G H I J K L M N O")
    print("   | " + "-"*29)
    for i in range(15):
        linha_numero = str(i + 1).rjust(2, '0')
        print(f"{linha_numero} | {' '.join(tabuleiro[i])}")

# exibir_tabuleiro(tabuleiro)


def posicionar_navios(tabuleiro, jogador, navios):
    for i, (tipo_navio, _) in enumerate(navios):
        letra_navio = tipo_navio  # Já é uma letra conforme a seleção ativa
        for posicao in jogador[i]:
            if len(posicao) == 3:
                letra_linha, coluna, orientacao = posicao
                linha = ord(letra_linha.upper()) - ord('A')
                coluna = int(coluna) - 1
                if tabuleiro[linha][coluna] != "O":
                    return "ERROR_OVERWRITE_PIECES_VALIDATION"
                tabuleiro[linha][coluna] = letra_navio
            elif len(posicao) == 2:
                letra_linha, coluna = posicao
                linha = ord(letra_linha.upper()) - ord('A')
                coluna = int(coluna) - 1
                if tabuleiro[linha][coluna] != "O":
                    return "ERROR_OVERWRITE_PIECES_VALIDATION"
                tabuleiro[linha][coluna] = letra_navio
    return tabuleiro



J1_navios_posicionados = posicionar_navios(tabuleiro, J1_navios, navios)

print(exibir_tabuleiro(J1_navios_posicionados))

# Função para posicionar navio no tabuleiro
# def posicionar_navio(tabuleiro, navio, coordenadas):
#     linha, coluna, direcao = coordenadas
#     linha -= 1
#     coluna = ord(coluna.upper()) - ord('A')
#     tamanho = len(navio)
    
#     if direcao == "V":
#         for i in range(tamanho):
#             tabuleiro[linha + i][coluna] = navio[i]
#     elif direcao == "H":
#         for i in range(tamanho):
#             tabuleiro[linha][coluna + i] = navio[i]



