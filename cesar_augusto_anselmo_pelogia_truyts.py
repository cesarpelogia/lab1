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
    print("   " + " ".join(str(i+1).rjust(2, ' ') for i in range(len(tabuleiro[0]))))
    print("  +--------------------------------------------")
    for i in range(len(tabuleiro)):
        letra_linha = chr(ord('A') + i)
        print(f"{letra_linha} | {'  '.join(tabuleiro[i])}")
    print("\n")


def posicionar_navios(tabuleiro, jogador, navios):
    # Cria uma cópia do tabuleiro original para trabalhar
    novo_tabuleiro = [linha[:] for linha in tabuleiro]

    for i, (tipo_navio, _) in enumerate(navios):
        letra_navio = tipo_navio
        for posicao in jogador[i]:
            if len(posicao) == 3:
                letra_linha, coluna, orientacao = posicao

                linha = ord(letra_linha.upper()) - ord('A')
                coluna = int(coluna) - 1

                tamanho_navio = len(navios[int(tipo_navio) - 1][1])

                if orientacao == 'V':
                    for j in range(tamanho_navio):
                        # Verifica se a posição está dentro do tabuleiro e se está vazia
                        if linha + j >= len(novo_tabuleiro) or novo_tabuleiro[linha + j][coluna] != "O":
                            return "ERROR_INVALID_OR_OCCUPIED_POSITION"
                        novo_tabuleiro[linha + j][coluna] = letra_navio
                elif orientacao == 'H':
                    for j in range(tamanho_navio):
                        # Verifica se a posição está dentro do tabuleiro e se está vazia
                        if coluna + j >= len(novo_tabuleiro[0]) or novo_tabuleiro[linha][coluna + j] != "O":
                            return "ERROR_INVALID_OR_OCCUPIED_POSITION"
                        novo_tabuleiro[linha][coluna + j] = letra_navio
            elif len(posicao) == 2:
                letra_linha, coluna = posicao

                linha = ord(letra_linha.upper()) - ord('A')
                coluna = int(coluna) - 1

                # Verifica se a posição está vazia antes de posicionar o navio
                if novo_tabuleiro[linha][coluna] != "O":
                    return "ERROR_OVERWRITE_PIECES_VALIDATION"
                novo_tabuleiro[linha][coluna] = letra_navio

    return novo_tabuleiro

def buscarPosicao(naviosPosicionados, letra, numero, tabuleiro):
    for coodernada in tabuleiro:
        print(coodernada)
        print()



def dispararToperdos(tabuleiro, tiros):
    for tiro in tiros:
        try:
            tabuleiro = dispararTorpedo(tabuleiro, tiro[0], tiro[1])
        except ValueError as e:
            print(e)


def dispararTorpedo(tabuleiro, letra, numero):
    if letra > "P" or (numero > 15 and numero < 1):
        raise ValueError("ERROR_POSITION_NONEXISTENT_VALIDATION")
    # tabuleiro = buscarPosicao()
        




J1_navios_posicionados = posicionar_navios(tabuleiro, J1_navios, navios)
J2_navios_posicionados = posicionar_navios(tabuleiro, J2_navios, navios)


exibir_tabuleiro(J1_navios_posicionados)
exibir_tabuleiro(J2_navios_posicionados)

buscarPosicao(J1_navios, 1, 2, J1_navios_posicionados)




# def dividir(a, b):
#     if b == 0:
#         raise ValueError("Não é possível dividir por zero")
#     return a / b

# try:
#     resultado = dividir(10, 0)
#     print(f"Resultado: {resultado}")
# except ValueError as e:
#     print(f"Ocorreu um erro: {e}")







