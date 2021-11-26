import random
import sys
import os


bem_vindo = 'BEM-VINDO(A) AO JOGO 21!'
separacao_b = ('-')*len(bem_vindo)
regras = 'REGRAS: O JOGO TERMINA AO COMPLETAR 21, CHEGAR PRóXIMO AO 21 E SE PASSAR DO 21'
separacao_r = ('-')*len(regras)
validacao = total = bar = nai = 0

def limpar_terminal(numlines=100):
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print('\n' * numlines)

def para_ou_continua():
    global validacao
    validacao = str(input("\nVocê quer mais uma carta [S] ou [N]? \n>> ").lower())
    if validacao != 's':
        verifica_total()

def verifica_total():
    if total > 21:
        print(f'\n{nome_jogador} Você PERDEU!\nAs soma das cartas escolhidas foi {total} e PASSOU de 21!')

    elif 15 < total < 21:
        print(f'\nParabéns! {nome_jogador} Você chegou próximo ao 21.\nA soma das cartas escolhidas foi {total} e Não PASSOU de 21!')

    elif total == 21:
        print(f'\nParabéns! {nome_jogador} Você Ganhou!\nA soma das cartas escolhidas foi {total} e Não PASSOU de 21!')

    else:
        print(f'Total das cartas {total}\n')
    print('\nGostaria de jogar novamente?')
    verifica_opcao()

def sorteio():
    limpar_terminal()

    global total
    baralho = ["AS",2,3,4,5,6,7,8,9,10,"VALETE","DAMA","REI"]
    naipes = ["♣", "♦", "♥", "♠"]

    bar = random.choice(baralho)
    nai = random.choice(naipes)

    if bar == "AS" :
        total = total + 1
    elif bar == "VALETE" or bar == "DAMA" or bar =="REI":
        total = total + 10
    else:
        total = total + bar

    print(f"\nA sua carta é: {bar} {nai}")
    print(f"O valor de sua(s) carta(s): {total}")
    para_ou_continua()

def verifica_opcao():
    opcao = input("\nDIGITE: \n[J] PARA JOGAR\n[S] PARA SAIR\n>> ").lower()

    if opcao == "j":
        global total
        print("\nCOMEÇANDO...")
        total = 0

    elif opcao =="s":
        print(f'\nSAINDO...\naté a Proxíma {nome_jogador}!')
        sys.exit()

    else:
        limpar_terminal()
        print("Digite somente as letras informadas.")
        verifica_opcao()

print(f'{separacao_b}\n{bem_vindo}\n{separacao_b}')
print(f'{separacao_r}\n{regras}\n{separacao_r}')
nome_jogador = str(input("\nDigite o nome do Jogador: ").upper())

verifica_opcao()


while True:

    sorteio()