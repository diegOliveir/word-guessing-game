import random

name = input('Qual o seu nome? ')
print(f'Bem vindo, {name}! \nEsse é um jogo de adivinhação de palavras. Você tem 12 tentativas para acertar a palavra letra por letra!')

words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print(f'A palavra escolhida tem {len(word)} letras!')

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for i in word:
        if i in guesses:
            print(i, end='')
        else:
            print('_', end='')
            failed += 1
    
    if failed == 0:
        print(f'Você venceu! A palavra era {word}.')
        break

    guess = input('\nEscolha uma letra: ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print(f'Você errou! Lhe restam {turns} tentativas.')

        if turns == 0:
            print('Você perdeu!')