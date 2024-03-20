from random import randint

# Abrindo arquivo de texto Jogador 1
with open('jogador1.txt') as j1_file:
    linhas_j1 = j1_file.readlines()

encouracado_j1 = linhas_j1[0]
porta_aviao_j1 = linhas_j1[1]
submarino_j1 = linhas_j1[2]
cruzador_j1 = linhas_j1[3]
tiros_j1 = linhas_j1[5]


# Abrindo arquivo de texto Jogador 1
with open('jogador2.txt') as j2_file:
    linhas_j2 = j2_file.readlines()

encouracado_j2 = linhas_j2[0]
porta_aviao_j2 = linhas_j2[1]
submarino_j2 = linhas_j2[2]
cruzador_j2 = linhas_j2[3]
tiros_j2 = linhas_j2[5]



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

# Função para posicionar o navio com base na entrada
def posicionar_navio_da_entrada(tabuleiro, entrada):
    partes = entrada.split(";")
    navio = partes[0]
    coluna = partes[1][0]
    linha = int(partes[1][1])
    direcao = partes[1][2]
    
    posicionar_navio(tabuleiro, navio, (linha, coluna, direcao))


# Definindo Navios.
navios = {
    "1": ["E", "E", "E", "E"],  # Encouraçado
    "2": ["P", "P", "P", "P", "P"],  # Porta-aviões
    "3": ["S"],  # Submarino
    "4": ["C", "C"]  # Cruzador
    }


# Definindo tabuleiro
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


