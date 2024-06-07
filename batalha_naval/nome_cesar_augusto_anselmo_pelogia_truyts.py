from random import randint

def ler_navios_e_tiros_jogador(arquivo):
    with open(arquivo) as arquivo_jogador:
        linhas = arquivo_jogador.readlines()

    encouracado = linhas[0].strip().replace("1;", "").split("|")
    porta_aviao = linhas[1].strip().replace("2;", "").split("|")
    submarino = linhas[2].strip().replace("3;", "").split("|")
    cruzador = linhas[3].strip().replace("4;", "").split("|")
    tiros = linhas[5].strip().replace("T;", "").split("|")

    return encouracado, porta_aviao, submarino, cruzador, tiros

J1_navios, J1_tiros = ler_navios_e_tiros_jogador("batalha_naval\\jogador1.txt")
J2_navios, J2_tiros = ler_navios_e_tiros_jogador("batalha_naval\\jogador2.txt")

# Definição dos navios
navios = [
    ("1", ["E", "E", "E", "E"]),  # Encouraçado
    ("2", ["P", "P", "P", "P", "P"]),  # Porta-aviões
    ("3", ["S"]),  # Submarino
    ("4", ["C", "C"])  # Cruzador
]

def validar_navios(J1_navios, navios):
    for i, (tipo_navio, posicoes_navio) in enumerate(navios):
        # Verifica se o navio tem o número correto de posições
        if len(J1_navios[i]) != len(posicoes_navio):
            return False
        # Verifica se nenhuma posição é repetida
        if len(J1_navios[i]) != len(set(J1_navios[i])):
            return False
        # Verifica se todas as posições estão dentro do tabuleiro
        for posicao in J1_navios[i]:
            linha, coluna = posicao[0], int(posicao[1:])
            if linha < 'A' or linha > 'J' or coluna < 1 or coluna > 10:
                return False
    return True

validacao_navios_j1 = validar_navios(J1, navios)
validacao_navios_j2 = validar_navios(J2, navios)

if not validacao_navios_j1 or not validacao_navios_j2:
    print("ERROR_NR_PARTS_VALIDATION")
    exit(1)
else:
    print("Todos os navios são válidos.")


def posicionar_navios(tabuleiro, jogador, navios):
    for i, (tipo_navio, _) in enumerate(navios):
        for posicao in jogador[i]:
            linha, coluna = posicao
            if tabuleiro[linha][coluna] != "O":
                return "ERROR_OVERWRITE_PIECES_VALIDATION"
            tabuleiro[linha][coluna] = tipo_navio
    return None



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

# # Função para posicionar navio com base na entrada do usuário
# def posicionar_navio_da_entrada(tabuleiro, entrada):
#     partes = entrada.split(";")
#     navio = partes[0]
#     coluna = partes[1][0]
#     linha = int(partes[1][1])
#     direcao = partes[1][2]
    
#     posicionar_navio(tabuleiro, navio, (linha, coluna, direcao))

# Definição e exibição do tabuleiro
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

exibir_tabuleiro(tabuleiro)



