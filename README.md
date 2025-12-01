# Projeto de Manipulação de Vetores e Matrizes 

Este projeto foi desenvolvido no âmbito da disciplina de **Laboratórios de Informática** do curso de **Licenciatura em Inteligência Artificial e Ciência de Dados**.

O programa consiste numa aplicação em Python que permite a manipulação de vetores, realização de cálculos matemáticos (seno, determinantes, números primos) e geração de matrizes através de um menu interativo ou via linha de comando.

---

##  Autores 

* **Gabriel Salazar**
* **Daniel Colavito**
* **Leandro Apolo**
* **Jorge Altamirano**

---

##  Funcionalidades

O programa permite realizar as seguintes operações sobre um vetor de tamanho N (configurado para 16):

1. Obter um elemento aleatório.  
2. Calcular o seno dos elementos.  
3. Construir uma matriz 2xN.  
4. Filtrar números divisíveis por 3.  
5. Multiplicar pelo último elemento.  
6. Ordenar de forma decrescente.  
7. Misturar o vetor com novos valores (Metade/Metade).  
8. Encontrar números primos.  
9. Gerar Matriz NxN (Produto de vetores).  
10. Calcular determinante da matriz gerada.

---

##  Pré-requisitos

Para executar este projeto, necessita de ter instalado:

* **Python 3.x**
* Biblioteca **NumPy**

Para instalar as dependências, execute:

```bash
pip install numpy
```

---

##  Como Executar?

### 1. Modo Interativo (Menu)

Para iniciar o programa e usar o menu textual:

```bash
python src/main.py
```

### 2. Modo Linha de Comando (CLI)

Pode executar funções específicas diretamente sem passar pelo menu.

**Exemplo de ajuda:**

```bash
python src/main.py --help
```

**Exemplo de execução de uma opção (ex: calcular senos):**

```bash
python src/main.py --opcao 2
```

---

##  Documentação (Doxygen)

A documentação técnica do código foi gerada automaticamente utilizando **Doxygen**.

Para visualizar a documentação:

1. Navegue até à pasta `docs/html`.  
2. Abra o ficheiro `index.html` no seu navegador.

---

## Estrutura do Projeto

```
src/          → Código fonte (main.py e calculos.py)
docs/         → Documentação gerada (HTML)
Doxyfile      → Ficheiro de configuração do Doxygen
Relatorio.pdf → Relatório técnico do trabalho
```
