import os

TAMANHO_TABULEIRO = 15

# Função para converter coordenadas do formato A1 para índices do tabuleiro
def converter_coordenadas(coord):
    linha = ord(coord[0].upper()) - ord('A')
    coluna = int(coord[1:]) - 1
    return linha, coluna

# Função para ler o arquivo de entrada
def ler_arquivo_entrada(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        conteudo = file.read().strip().split('# Jogada')
        posicoes = conteudo[0].strip().split('\n')
        tiros = conteudo[1].strip().split(';')[1].split('|')
    return posicoes, tiros

# Função para inicializar o tabuleiro vazio
def inicializar_tabuleiro():
    return [['~'] * TAMANHO_TABULEIRO for _ in range(TAMANHO_TABULEIRO)]

# Função para imprimir o tabuleiro (para depuração)
def imprimir_tabuleiro(tabuleiro):
    print("  " + " ".join(str(i + 1) for i in range(TAMANHO_TABULEIRO)))
    for i, linha in enumerate(tabuleiro):
        print(chr(i + ord('A')) + " " + " ".join(linha))

# Função para posicionar os navios no tabuleiro
def posicionar_navios(tabuleiro, posicoes):
    for pos in posicoes:
        codigo, dados = pos.split(';')
        codigo = int(codigo)
        posicionamentos = dados.split('|')
        for posicao in posicionamentos:
            coord, orientacao = posicao[:-1], posicao[-1]
            x, y = converter_coordenadas(coord)
            if not posicao_valida(tabuleiro, x, y, codigo, orientacao):
                return False, 'ERROR_OVERWRITE_PIECES_VALIDATION'
            posicionar_navio(tabuleiro, x, y, codigo, orientacao)
    return True, None

# Função para verificar se a posição é válida
def posicao_valida(tabuleiro, x, y, codigo, orientacao):
    comprimento = obter_comprimento_navio(codigo)
    for i in range(comprimento):
        if orientacao == 'H':
            if y + i >= TAMANHO_TABULEIRO or tabuleiro[x][y + i] != '~':
                return False
        elif orientacao == 'V':
            if x + i >= TAMANHO_TABULEIRO or tabuleiro[x + i][y] != '~':
                return False
    return True

# Função para obter o comprimento do navio com base no código
def obter_comprimento_navio(codigo):
    if codigo == 1:
        return 4
    elif codigo == 2:
        return 5
    elif codigo == 3:
        return 1
    elif codigo == 4:
        return 2

# Função para posicionar um navio no tabuleiro
def posicionar_navio(tabuleiro, x, y, codigo, orientacao):
    comprimento = obter_comprimento_navio(codigo)
    for i in range(comprimento):
        if orientacao == 'H':
            tabuleiro[x][y + i] = str(codigo)
        elif orientacao == 'V':
            tabuleiro[x + i][y] = str(codigo)

# Função para processar os tiros
def processar_tiros(tabuleiro, tiros):
    acertos = 0
    for tiro in tiros:
        x, y = converter_coordenadas(tiro)
        if x < 0 or x >= TAMANHO_TABULEIRO or y < 0 or y >= TAMANHO_TABULEIRO:
            return False, 'ERROR_POSITION_NONEXISTENT_VALIDATION', 0
        if tabuleiro[x][y] != '~' and tabuleiro[x][y] != 'X':
            acertos += 1
            tabuleiro[x][y] = 'X'
        else:
            tabuleiro[x][y] = 'O'
    return True, None, acertos

# Função principal para executar o jogo
def jogar_batalha_naval(arquivo_jogador1, arquivo_jogador2, arquivo_saida):
    # Ler arquivos de entrada
    posicoes1, tiros1 = ler_arquivo_entrada(arquivo_jogador1)
    posicoes2, tiros2 = ler_arquivo_entrada(arquivo_jogador2)

    # Inicializar tabuleiros
    tabuleiro1 = inicializar_tabuleiro()
    tabuleiro2 = inicializar_tabuleiro()

    # Posicionar navios
    valido1, erro1 = posicionar_navios(tabuleiro1, posicoes1)
    if not valido1:
        with open(arquivo_saida, 'w') as file:
            file.write(f"J1 {erro1}\n")
        return

    valido2, erro2 = posicionar_navios(tabuleiro2, posicoes2)
    if not valido2:
        with open(arquivo_saida, 'w') as file:
            file.write(f"J2 {erro2}\n")
        return

    # Processar tiros
    valido1, erro1, acertos1 = processar_tiros(tabuleiro2, tiros1)
    if not valido1:
        with open(arquivo_saida, 'w') as file:
            file.write(f"J1 {erro1}\n")
        return

    valido2, erro2, acertos2 = processar_tiros(tabuleiro1, tiros2)
    if not valido2:
        with open(arquivo_saida, 'w') as file:
            file.write(f"J2 {erro2}\n")
        return

    # Calcular pontuação
    pontuacao1 = acertos1 * 3 + (acertos1 // 5) * 5
    pontuacao2 = acertos2 * 3 + (acertos2 // 5) * 5

    # Determinar vencedor
    if pontuacao1 > pontuacao2:
        vencedor = "J1"
    elif pontuacao2 > pontuacao1:
        vencedor = "J2"
    else:
        vencedor = "EMPATE"

    # Escrever resultado no arquivo de saída
    with open(arquivo_saida, 'w') as file:
        if vencedor == "EMPATE":
            file.write(f"J1 {acertos1}A {25-acertos1}E {pontuacao1}PT\n")
            file.write(f"J2 {acertos2}A {25-acertos2}E {pontuacao2}PT\n")
        else:
            file.write(f"{vencedor} {acertos1 if vencedor == 'J1' else acertos2}A {25 - (acertos1 if vencedor == 'J1' else acertos2)}E {pontuacao1 if vencedor == 'J1' else pontuacao2}PT\n")

# Teste com os arquivos de exemplo
jogar_batalha_naval('jogador1.txt', 'jogador2.txt', 'resultado.txt')
