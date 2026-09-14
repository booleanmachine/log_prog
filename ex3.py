import random
opcoes = ['pedra', 'papel', 'tesoura']

entrada = input('Digite sua entrada: ').lower()



bot = random.choice(opcoes)

if entrada not in opcoes:
    print(' Entrada invalida, repita a jogada ')
    quit()


if entrada == bot: 
    print('o jogo empatou')

if(
        (entrada == "pedra" and bot == "tesoura")
        or (entrada == "papel" and bot == "pedra")
        or (entrada == "tesoura" and bot == "papel")
    ):
    print (f'Você ganhou, você escolheu {entrada} e o bot {bot}')
else:
    print(f'O bot ganhou, {bot} vence {entrada}')