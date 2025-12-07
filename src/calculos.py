## @file calculos.py
#  @brief Módulo com todas as funções lógicas e matemáticas.
#  @details Contém as funções  para validar números,cálculos de matrizes,
#           operações com vetores e o menu principal.
#  @author Gabriel Salazar, Daniel Colavito, Leandro Apolo, Jorge Altamirano
#  @version 1.2

import math
from random import choice, randint
import numpy as np
import sys

# --- CONFIGURAÇÃO CENTRAL ---
VECTOR_SIZE = 16 

# --- Funções ANSI ---
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
RESET = '\033[0m'

# --- Funções Auxiliares e Matemáticas ---

## @brief Pergunta ao utilizador se deseja continuar.
## @return True se a resposta for 'S', False caso contrário.
def perguntar_continuar():
    while True:
        resp = input(f"\n{CYAN}Deseja continuar? (S/N): {RESET}").strip().upper()
        if resp in ("S", "N"):
            return resp == "S"
        print(f"{RED}Resposta inválida! Digite apenas S ou N.{RESET}")

## @brief Solicita e valida uma entrada numérica do usuário.
## @param prompt Mensagem para o usuário.
## @param numero_min Valor mínimo permitido.
## @param numero_max Valor máximo permitido.
## @return Número inteiro válido dentro do intervalo.
def numero_valido(prompt, numero_min, numero_max):
    while True:
        try:
            num = int(input(prompt))
            if numero_min <= num <= numero_max:
                return num
            else:
                print(f"{RED}O seu número está fora do intervalo. Por favor, introduza um número entre {numero_min} e {numero_max}.{RESET}")
        except ValueError:
            print(f"{RED}Entrada inválida. Por favor, introduza um número inteiro.{RESET}")

## @brief Retorna um elemento aleatório do vetor.
## @param vector Vetor de entrada.
## @return Elemento aleatório do vetor.
def valor_aleatorio(vector):
    return choice(vector)

## @brief Calcula o seno de cada elemento do vetor.
## @param vector Vetor de entrada.
## @return Lista dos senos dos elementos do vetor.
def calcular_seno(vector):
    return [math.sin(element) for element in vector]

## @brief Constrói uma matriz 2xN.
## @param vector Vetor de entrada.
## @return Matriz 2xN (lista de listas).
def matriz_2x16(vector):
    matriz = []
    matriz.append(vector)
    segunda_linha = [randint(-10, 27) for _ in range(VECTOR_SIZE)]
    matriz.append(segunda_linha)
    return matriz

## @brief Encontra valores no vetor divisíveis por três.
## @param vector Vetor de entrada.
## @return Lista de valores divisíveis por três.
def divisivel_3(vector):
    return [x for x in vector if x % 3 == 0]

## @brief Multiplica cada elemento do vetor pelo último elemento.
## @param vector Vetor de entrada.
## @return Lista resultante da multiplicação.
def multiplicar_por_el_ultimo(vector):
    ultimo_elemento = vector[-1]
    return [element * ultimo_elemento for element in vector]

## @brief Ordena o vetor em ordem decrescente.
## @param vector Vetor de entrada.
## @return Vetor ordenado em ordem decrescente.
def orden_descreciente(vector):
    return sorted(vector, reverse=True)

## @brief Exibe uma simulação da mensagem de ajuda do argparse.
def mostrar_ajuda():
    import argparse
    print(f"\n{YELLOW}Esta é uma simulação de como o argparse geraria a mensagem de ajuda...{RESET}\n")
    parser = argparse.ArgumentParser(description='Este é o programa interativo para manipular vetores.', add_help=False)
    parser.add_argument('--opcao', type=int, help='Executa uma das opções do menu diretamente (1 a 11).')
    parser.add_argument('--vetor_inicial', nargs=VECTOR_SIZE, type=int, help=f'Define o vetor inicial com {VECTOR_SIZE} números inteiros.')
    parser.add_argument('--help', action='help', default=argparse.SUPPRESS, help='Mostra esta mensagem de ajuda e sai.')
    print(f"{YELLOW}--- Início da Ajuda do Argparse Simulada ---{RESET}")
    parser.print_help()
    print(f"{YELLOW}--- Fim da Ajuda do Argparse Simulada ---{RESET}")

## @brief Cria um novo vetor misturando metade do original com metade de um novo.
## @param vector_original Vetor original de entrada.
## @return Vetor misturado (Metade original + Metade novo).
def mitad_mitad(vector_original):
    Vetor_2 = []
    print(f"\n{CYAN}Introduza os {VECTOR_SIZE} números para o novo vetor (para misturar):{RESET}")
    for i in range(VECTOR_SIZE):
        num_input = numero_valido(f"Introduza um número entre -10 e 27 ({i+1}/{VECTOR_SIZE}): ", -10, 27)
        Vetor_2.append(num_input)
    
    half = VECTOR_SIZE // 2
    return vector_original[:half] + Vetor_2[:half]

## @brief Encontra os números primos no vetor.
## @param vector Vetor de entrada.
## @return Lista de números primos encontrados.
def numeros_primos(vector):
    primos = []
    for num in vector:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primos.append(num)
    return primos

## @brief Gera uma matriz NxN a partir do produto de dois vetores.
## @param vector_initial Vetor inicial de entrada.
## @return Matriz NxN resultante do produto.
def matriz_16x16(vector_initial):
    Vetor_novo = []
    print(f"\n{CYAN}Introduza os {VECTOR_SIZE} números para o novo vetor (1x{VECTOR_SIZE}):{RESET}")
    for i in range(VECTOR_SIZE):
        num_input = numero_valido(f"Introduza um número entre -10 e 27 ({i+1}/{VECTOR_SIZE}): ", -10, 27)
        Vetor_novo.append(num_input)
    
    matriz_resultante = []
    for i in range(VECTOR_SIZE):
        row = []
        for j in range(VECTOR_SIZE):
            row.append(vector_initial[i] * Vetor_novo[j])
        matriz_resultante.append(row)
    return matriz_resultante

## @brief Calcula o determinante da matriz NxN.
## @param matrix Matriz quadrada.
## @return Valor do determinante ou mensagem de erro.
def calcular_determinante(matrix):
    if matrix is not None and len(matrix) > 0:
        try:
            det = np.linalg.det(np.array(matrix))
            return det
        except Exception as e:
            return f"Erro ao calcular o determinante: {e}"
    else:
        return f"Por favor, execute a opção 10 primeiro para gerar a matriz {VECTOR_SIZE}x{VECTOR_SIZE}."

# --- LÓGICA CENTRALIZADA ---

## @brief Processa uma opção escolhida e imprime o resultado.
## @details Esta função centraliza a lógica de escolha para evitar duplicação
#           entre o menu interativo e a linha de comandos.
## @param opcao O número da opção (int ou str).
## @param Vetor O vetor de dados.
## @param matriz_resultante_final A matriz global (lista).
## @return True se deve sair do programa (opção 12), False caso contrário.
def processar_escolha(opcao, Vetor, matriz_resultante_final):
    # Convertemos para string para garantir comparação igual
    op = str(opcao)

    if op == "1":
        valor = valor_aleatorio(Vetor)
        print(f"O elemento aleatório do vetor {Vetor} é: {GREEN}{valor}{RESET}")
    elif op == "2":
        senos = calcular_seno(Vetor)
        print(f"Os senos dos elementos do vetor {Vetor} são:")
        for v, s in zip(Vetor, senos):
            print(f"  sen({v}): {GREEN}{s:.3f}{RESET}")
    elif op == "3":
        matriz = matriz_2x16(Vetor)
        print(f"A sua matriz 2x{VECTOR_SIZE} é:")
        for linha in matriz:
            print(f"{GREEN}{linha}{RESET}")
    elif op == "4":
        div3 = divisivel_3(Vetor)
        if div3:
            print(f"Os números divisíveis por três do vetor {Vetor} são:\n{GREEN}{div3}{RESET}")
        else:
            print(f"{RED}Não foram encontrados números divisíveis por três no vetor.{RESET}")
    elif op == "5":
        resultado = multiplicar_por_el_ultimo(Vetor)
        print(f"O vetor resultante da multiplicação de cada elemento pelo último elemento de {Vetor} é:\n {GREEN}{resultado}{RESET}")
    elif op == "6":
        ordenado = orden_descreciente(Vetor)
        print(f"O vetor {Vetor} ordenado por ordem decrescente é:\n {GREEN}{ordenado}{RESET}")
    elif op == "7":
        mostrar_ajuda()
    elif op == "8":
        # Opção que requer input, funciona em ambos os modos
        misturado = mitad_mitad(Vetor)
        print(f"\nO vetor misturado ({VECTOR_SIZE//2}+{VECTOR_SIZE//2}) é:{GREEN}{misturado}{RESET}")
    elif op == "9":
        primos = numeros_primos(Vetor)
        if primos:
            print(f"Os primos do seu vetor {Vetor} são:\n{GREEN}{primos}{RESET}")
        else:
            print(f"{RED}Não foram encontrados números primos no vetor.{RESET}")
    elif op == "10":
        # Opção que requer input
        matriz_resultante_final.clear()
        matriz = matriz_16x16(Vetor)
        matriz_resultante_final.extend(matriz)
        print(f"A matriz {VECTOR_SIZE}x{VECTOR_SIZE} resultante é:")
        for linha in matriz:
            print(f"  {GREEN}{linha}{RESET}")
    elif op == "11":
        det = calcular_determinante(matriz_resultante_final)
        if det is not None and not isinstance(det, str):
            print(f"O determinante da matriz é: {GREEN}{det:.2f}{RESET}")
        elif isinstance(det, str):
            print(f"{RED}{det}{RESET}")
        else:
             print(f"{RED}Por favor, execute a opção 10 primeiro para gerar a matriz {VECTOR_SIZE}x{VECTOR_SIZE}.{RESET}")
    elif op == "12":
        print(f"{CYAN}\nObrigado pela atenção{RESET}")
        return True # Indica que deve sair
    else:
        print(f"{RED}Escolha um número válido{RESET}")
    
    return False

# --- Menu Principal ---

## @brief Muestra el menú interactivo y gestiona la elección del usuario.
## @param Vetor El vector principal con el que se trabaja.
## @param matriz_resultante_final La variable global para almacenar la matriz.
## @return No retorna nada, pero ejecuta otras funciones según la elección.
def mostrar_menu(Vetor, matriz_resultante_final):
    while True:
        print(f"\n{YELLOW}{ITALIC}1 - Retorno de um elemento aleatório desse vetor")
        print(f"2- Cálculo do seno (sin)")
        print(f"3- Construção de uma matriz 2 por {VECTOR_SIZE}")
        print(f"4- Devolução dos valores do vetor que são divisíveis por três")
        print(f"5- Cálculo da multiplicação de cada elemento do vetor com o último elemento do vetor")
        print(f"6- Devolução do vetor ordenado por ordem decrescente")
        print(f"7- Ajuda")
        print(f"8- Novo Vetor, metade e metade")
        print(f"9- Números primos")
        print(f"10- Leitura de um novo vetor 1x{VECTOR_SIZE}, cálculo e devolução da matriz {VECTOR_SIZE}x{VECTOR_SIZE} resultante do produto do vetor inicial com o novo vetor gerado;")
        print(f"11- Cálculo do determinante da matriz gerada anteriormente;")
        print(f"12- Sair do programa" + RESET)

        user_choice = input(f"\n{CYAN}Escolha uma opção: {RESET}")

        # CHAMAMOS A FUNÇÃO CENTRALIZADA
        sair = processar_escolha(user_choice, Vetor, matriz_resultante_final)
        
        if sair: break
        
        if not perguntar_continuar():
            print(f"{CYAN}\nPrograma finalizado pelo usuário.{RESET}")
            break