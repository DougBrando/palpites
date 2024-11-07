from random import randint

def jogar():
    computador = randint(0, 10)  # Gera um número aleatório entre 0 e 10
    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 0 e 10.")

    acertou = False
    palpite = 0

    while not acertou:
        try:
            jogador = int(input(f'{palpite + 1}º palpite: '))  # Solicita o palpite do jogador
            palpite += 1  # Incrementa o contador de palpites

            if jogador == computador:
                acertou = True  # O jogador acertou
            else:
                if jogador < computador:
                    print('Mais, tente outra vez.')  # O número é maior
                else:
                    print('Menos, tente outra vez.')  # O número é menor
        except ValueError:
            print("Por favor, insira um número válido.")  # Tratamento de exceção para entradas inválidas

    print(f'Parabéns! Você acertou no {palpite}º palpite.')

def main():
    while True:
        jogar()  # Inicia o jogo
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    main()
