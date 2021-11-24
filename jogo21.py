import random
import sys

baralho = ["AS",2,3,4,5,6,7,8,9,10,"VALETE","DAMA","REI"]
naipes = ["♣", "♦", "♥", "♠"]
separacao = ('--')*20

print(f"{separacao}\n        BEM-VINDO(A) AO JOGO 21!\n{separacao}")

nome_jogador = input("\nDigite seu nome:")

opcao = input("\nDIGITE: \n[J] PARA JOGAR\n[S] PARA SAIR\n>> ")

opcao2 = total = bar = nai = 0

if opcao == "j" or opcao =="j":
    print("\nCOMEÇANDO...")
elif opcao == "S" or opcao =="s":
    print(f'\nSAINDO...\n{nome_jogador} até a Proxíma!')
    sys.exit()


while opcao2 != "N":
    bar = random.choice(baralho)
    nai = random.choice(naipes)


    if bar == "AS" :
        total = total + 1
    elif bar == "VALETE" or bar == "DAMA" or bar =="REI":
        total = total + 10
    else:
        total = total + bar

    print("\nA sua carta é:", bar, nai)
    print("O valor de sua(s) carta(s):", total)


    if total > 21:
          print(f'\n{nome_jogador} Você PERDEU!\nAs soma das cartas escolhidas foi {total} e PASSOU de 21!')
          break
    elif total > 15  and total < 21:
          print(f'\nParabéns! {nome_jogador} Você chegou próximo ao 21.\nA soma das cartas escolhidas foi {total} e Não PASSOU de 21!')
          break
    elif total == 21:
          print(f'\nParabéns! {nome_jogador} Você Ganhou!\nA soma das cartas escolhidas foi {total} e Não PASSOU de 21!')
          break

    opcao2 = str(input("\nVocê quer mais uma carta [S] ou [N]? \n>> ").upper())
