#!/usr/bin/env python3
"""
Jogo da Velha (3x3) - Terminal
- Dois jogadores locais (X e O)
- Mostra coordenadas do tabuleiro (linhas e colunas 1..3)
- Placar entre partidas
- Opção de jogar novamente
- Alterna quem começa a cada partida
Comentários e mensagens em português.
"""

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tab):
    # Mostra cabeçalho de colunas
    print("\n    1   2   3")
    print("  +---+---+---+")
    for i, linha in enumerate(tab, start=1):
        print(f"{i} | " + " | ".join(linha) + " |")
        print("  +---+---+---+")
    print()

def checar_vencedor(tab):
    # Linhas e colunas
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] != " ":
            return tab[i][0]
        if tab[0][i] == tab[1][i] == tab[2][i] != " ":
            return tab[0][i]
    # Diagonais
    if tab[0][0] == tab[1][1] == tab[2][2] != " ":
        return tab[0][0]
    if tab[0][2] == tab[1][1] == tab[2][0] != " ":
        return tab[0][2]
    return None

def cheio(tab):
    return all(cell != " " for row in tab for cell in row)

def solicitar_jogada(jogador, tab):
    while True:
        entrada = input(f"Jogador {jogador} - digite linha e coluna (1-3), separadas por espaço (ex: '2 3'): ").strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        # Permitir formatos "r c" ou "r,c" ou "r,c\n"
        entrada = entrada.replace(",", " ")
        partes = entrada.split()
        if len(partes) != 2:
            print("Formato inválido. Informe dois números: linha e coluna.")
            continue
        try:
            r = int(partes[0])
            c = int(partes[1])
        except ValueError:
            print("Digite números inteiros entre 1 e 3.")
            continue
        if not (1 <= r <= 3 and 1 <= c <= 3):
            print("Valores fora do intervalo. Use 1, 2 ou 3.")
            continue
        # Ajustar para índice 0-based
        if tab[r-1][c-1] != " ":
            print("Posição ocupada. Escolha outra.")
            continue
        return r-1, c-1

def jogar_uma_partida(iniciar_com_X):
    tab = criar_tabuleiro()
    jogador_atual = "X" if iniciar_com_X else "O"
    mostrar_tabuleiro(tab)
    while True:
        linha, col = solicitar_jogada(jogador_atual, tab)
        tab[linha][col] = jogador_atual
        mostrar_tabuleiro(tab)
        vencedor = checar_vencedor(tab)
        if vencedor:
            print(f"Parabéns! Jogador {vencedor} venceu a partida!")
            return vencedor
        if cheio(tab):
            print("Empate! Nenhum vencedor nesta partida.")
            return None
        # alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

def confirmar_sim_nao(pergunta, padrao=True):
    pad = "s" if padrao else "n"
    while True:
        resp = input(f"{pergunta} (s/n) [{pad}]: ").strip().lower()
        if resp == "":
            return padrao
        if resp in ("s", "n"):
            return resp == "s"
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

def main():
    print("=== JOGO DA VELHA (Terminal) ===")
    print("Dois jogadores: X e O. Para jogar, informe linha e coluna (1 a 3).")
    print("Exemplo de entrada: 2 3  (linha 2, coluna 3)")
    print()

    placar = {"X": 0, "O": 0, "empates": 0}
    iniciar_com_X = True  # alterna quem começa a cada partida

    while True:
        print(f"Placar atual: X {placar['X']}  -  O {placar['O']}  -  Empates {placar['empates']}")
        print(f"Quem começa nesta partida: {'X' if iniciar_com_X else 'O'}")
        vencedor = jogar_uma_partida(iniciar_com_X)
        if vencedor == "X":
            placar["X"] += 1
        elif vencedor == "O":
            placar["O"] += 1
        else:
            placar["empates"] += 1

        print(f"\nPlacar atualizado: X {placar['X']}  -  O {placar['O']}  -  Empates {placar['empates']}")
        jogar_novamente = confirmar_sim_nao("Deseja jogar outra partida?", padrao=True)
        if not jogar_novamente:
            print("Obrigado por jogar! Placar final:")
            print(f"X {placar['X']}  -  O {placar['O']}  -  Empates {placar['empates']}")
            break
        # alterna quem começa
        iniciar_com_X = not iniciar_com_X
        print("\nIniciando nova partida...\n")

if __name__ == "__main__":
    main()