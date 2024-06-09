# Abrindo e lendo arquivo de texto Jogador 1
with open('jogador1.txt') as j1_file:
    linhas_j1 = j1_file.readlines()
    print("Linhas Jogador 1:", linhas_j1)  # Adicionado para debug

# Processando as linhas para o jogador 1
encouracado_j1 = linhas_j1[0].strip()
porta_aviao_j1 = linhas_j1[1].strip()
submarino_j1 = linhas_j1[2].strip()
cruzador_j1 = linhas_j1[3].strip()
tiros_j1 = linhas_j1[5].strip()

# Abrindo e lendo arquivo de texto Jogador 2
with open('jogador2.txt') as j2_file:
    linhas_j2 = j2_file.readlines()
    print("Linhas Jogador 2:", linhas_j2)  # Adicionado para debug

# Processando as linhas para o jogador 2
encouracado_j2 = linhas_j2[0].strip()
porta_aviao_j2 = linhas_j2[1].strip()
submarino_j2 = linhas_j2[2].strip()
cruzador_j2 = linhas_j2[3].strip()
tiros_j2 = linhas_j2[5].strip()

# Função para posicionar navio no tabuleiro
# Estava dando erro de posicionamento. Então criei esse debug para saber onde estão os navios que não podem ser posicionados. 
def posicionar_navio(tabuleiro, navio, coordenadas):
    linha, coluna, direcao = coordenadas
    linha -= 1
    coluna = ord(coluna.upper()) - ord('A')
    tamanho = len(navio)
    
    if direcao == "V":
        for i in range(tamanho):
            if 0 <= linha + i < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
                tabuleiro[linha + i][coluna] = navio[0]
            else:
                print(f"Erro: Tentativa de posicionar navio fora dos limites na posição ({linha + i}, {coluna})")
                return
    elif direcao == "H":
        for i in range(tamanho):
            if 0 <= linha < len(tabuleiro) and 0 <= coluna + i < len(tabuleiro[0]):
                tabuleiro[linha][coluna + i] = navio[0]
            else:
                print(f"Erro: Tentativa de posicionar navio fora dos limites na posição ({linha}, {coluna + i})")
                return

# Função para posicionar o navio com base na entrada
def posicionar_navio_da_entrada(tabuleiro, entrada):
    partes = entrada.split(";")
    navio_codigo = partes[0]
    navio = navios[navio_codigo]
    posicoes = partes[1].split("|")
    
    for posicao in posicoes:
        coluna = posicao[0]
        linha = posicao[1:-1]
        direcao = posicao[-1]
        
        # Debug: Verificar a extração da linha
        print(f"Debug - Coluna: {coluna}, Linha: {linha}, Direção: {direcao}")
        
        # if linha.isdigit():
        #     linha = int(linha)
        #     if direcao in ["H", "V"]:
        #         posicionar_navio(tabuleiro, navio, (linha, coluna, direcao))
        #     else:
        #         # Assumir que é um submarino sem direção especificada
        #         posicionar_navio(tabuleiro, navio, (linha, coluna, "H"))  # ou "V"
        # else:
        #     print(f"Erro: Linha inválida '{linha}' na posição '{posicao}'")

        if linha.isdigit():
            linha = int(linha)
            if len(navio) == 1:
                # Para submarinos (tamanho 1), ignoramos a direção
                posicionar_navio(tabuleiro, navio, (linha, coluna, "H")) # Apenas para ocupar esse espaço.
            elif direcao in ["H", "V"]:
                posicionar_navio(tabuleiro, navio, (linha, coluna, direcao))
            else:
                print(f"Erro: Direção inválida '{direcao}' na posição '{posicao}'")
        else:
            print(f"Erro: Linha inválida '{linha}' na posição '{posicao}'")

# Definindo Navios
navios = {
    "1": ["E", "E", "E", "E"],  # Encouraçado
    "2": ["P", "P", "P", "P", "P"],  # Porta-aviões
    "3": ["S"],  # Submarino
    "4": ["C", "C"]  # Cruzador
}

# Função para criar o tabuleiro
def criar_tabuleiro():
    tabuleiro = []
    for _ in range(15):
        linha = ["O"] * 15
        tabuleiro.append(linha)
    return tabuleiro

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("     A B C D E F G H I J K L M N O")
    print("   | " + "-"*29)
    for i in range(15):
        linha_numero = str(i + 1).rjust(2, '0')
        print(f"{linha_numero} | {' '.join(tabuleiro[i])}")


# Criar tabuleiros
tabuleiro_jogador1 = criar_tabuleiro()
tabuleiro_jogador2 = criar_tabuleiro()

# Posicionar navios do jogador 1
posicionar_navio_da_entrada(tabuleiro_jogador1, encouracado_j1)
posicionar_navio_da_entrada(tabuleiro_jogador1, porta_aviao_j1)
posicionar_navio_da_entrada(tabuleiro_jogador1, submarino_j1)
posicionar_navio_da_entrada(tabuleiro_jogador1, cruzador_j1)

# Posicionar navios do jogador 2
posicionar_navio_da_entrada(tabuleiro_jogador2, encouracado_j2)
posicionar_navio_da_entrada(tabuleiro_jogador2, porta_aviao_j2)
posicionar_navio_da_entrada(tabuleiro_jogador2, submarino_j2)
posicionar_navio_da_entrada(tabuleiro_jogador2, cruzador_j2)

# Exibir tabuleiros
print("Tabuleiro Jogador 1:")
exibir_tabuleiro(tabuleiro_jogador1)
print("\nTabuleiro Jogador 2:")
exibir_tabuleiro(tabuleiro_jogador2)
