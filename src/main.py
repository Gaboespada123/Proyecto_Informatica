## @file main.py
#  @brief Programa principal otimizado para manipulação de vetores.
#  @details Ponto de entrada que gere argumentos, inicializa o vetor e inicia o programa.
#  @author Gabriel Salazar, Daniel Colavito, Leandro Apolo, Jorge Altamirano
#  @version 1.2

import argparse
import sys
from calculos import *

# --- Variáveis Globais ---

## @var Vetor
#  @brief Vetor principal que armazena os dados do usuário.
Vetor = []

## @var matriz_resultante_final
#  @brief Armazena a matriz NxN gerada pela opção 10.
#  @details É inicializada como lista vazia e atualizada globalmente.
matriz_resultante_final = []

# --- Bloco de Execução Principal ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Este é o programa interativo para manipular vetores.',
        epilog='Para ajuda detalhada sobre opções de linha de comando, use "python seu_script.py --help".'
    )
    parser.add_argument('--opcao', type=int, choices=range(1, 12),
                        help='Executa uma das opções do menu diretamente (1 a 11) e sai.')
    parser.add_argument('--vetor_inicial', nargs=VECTOR_SIZE, type=int,
                        help=f'Define o vetor inicial com {VECTOR_SIZE} números inteiros entre -10 e 27.')

    args = parser.parse_args()

    # 1. Inicialização do Vetor
    if args.vetor_inicial:
        if all(-10 <= x <= 27 for x in args.vetor_inicial):
            Vetor.extend(args.vetor_inicial)
            print(f"{GREEN}Vetor inicial definido pela linha de comando: {Vetor}{RESET}")
        else:
            print(f"{RED}Erro: Os valores do vetor inicial devem estar entre -10 e 27.{RESET}")
            sys.exit(1)
    else:
        print(f"{CYAN}A iniciar a entrada interativa para o vetor...{RESET}")
        for i in range(VECTOR_SIZE):
            n = numero_valido(f"Introduza um número entre -10 e 27 ({i+1}/{VECTOR_SIZE}): ", -10, 27)
            Vetor.append(n)
        print(f"\nO seu vetor é: {GREEN}{Vetor}{RESET}")

    # 2. Execução
    if args.opcao:
        print(f"{CYAN}Executando a opção {args.opcao} via linha de comando...{RESET}")
        # Chamamos a mesma função centralizada de calculos.py
        processar_escolha(args.opcao, Vetor, matriz_resultante_final)
        sys.exit(0)
    else:
        mostrar_menu(Vetor, matriz_resultante_final)