from random import randint

def ler_navios_jogador(arquivo):
    with open(arquivo) as arquivo_jogador:
        linhas = arquivo_jogador.readlines()

    encouracado = linhas[0].strip()
    encouracado = encouracado.replace("1;", "")
    encouracado = encouracado.split("|")

    porta_aviao = linhas[1].strip()
    porta_aviao = porta_aviao.replace("2;", "")
    porta_aviao = porta_aviao.split("|")

    submarino = linhas[2].strip()
    submarino = submarino.replace("3;", "")
    submarino = submarino.split("|")

    cruzador = linhas[3].strip()
    cruzador = cruzador.replace("4;", "")
    cruzador = cruzador.split("|")

    return encouracado, porta_aviao, submarino, cruzador

def ler_tiros_jogador(arquivo):
    with open(arquivo) as arquivo_jogador:
        linhas = arquivo_jogador.readlines()

    tiros = linhas[5].strip()
    tiros = tiros.replace("T;", "")
    tiros = tiros.split("|")
    return tiros

J1 = ler_navios_jogador("batalha_naval\\jogador1.txt")
J2 = ler_navios_jogador("batalha_naval\\jogador2.txt")
jogadas_j1 = ler_tiros_jogador("batalha_naval\\jogador1.txt")
jogadas_j2 = ler_tiros_jogador("batalha_naval\\jogador2.txt")

# Definição dos navios
navios = [
    ("1", ["E", "E", "E", "E"]),  # Encouraçado
    ("2", ["P", "P", "P", "P", "P"]),  # Porta-aviões
    ("3", ["S"]),  # Submarino
    ("4", ["C", "C"])  # Cruzador
]

def validar_navios(jogador, navios):
    for i, (tipo_navio, posicoes_navio) in enumerate(navios):
        # Verifica se o navio tem o número correto de posições
        if len(jogador[i]) != len(posicoes_navio):
            return False
        # Verifica se nenhuma posição é repetida
        if len(jogador[i]) != len(set(jogador[i])):
            return False
        # Verifica se todas as posições estão dentro do tabuleiro
        for posicao in jogador[i]:
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



# Função para posicionar navio no tabuleiro
def posicionar_navio(tabuleiro, navio, coordenadas):
    linha, coluna, direcao = coordenadas
    linha -= 1
    coluna = ord(coluna.upper()) - ord('A')
    tamanho = len(navio)
    
    if direcao == "V":
        for i in range(tamanho):
            tabuleiro[linha + i][coluna] = navio[i]
    elif direcao == "H":
        for i in range(tamanho):
            tabuleiro[linha][coluna + i] = navio[i]

# Função para posicionar navio com base na entrada do usuário
def posicionar_navio_da_entrada(tabuleiro, entrada):
    partes = entrada.split(";")
    navio = partes[0]
    coluna = partes[1][0]
    linha = int(partes[1][1])
    direcao = partes[1][2]
    
    posicionar_navio(tabuleiro, navio, (linha, coluna, direcao))

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



