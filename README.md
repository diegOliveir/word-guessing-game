# Jogo de Adivinhação de Palavras

Este é um jogo de adivinhação de palavras desenvolvido em Python. O objetivo do jogador é descobrir uma palavra secreta, letra por letra, dentro de um limite de 12 tentativas.

## Como funciona

1. O sistema escolhe uma palavra aleatoriamente de uma lista predefinida.
2. O jogador é informado sobre o número de letras na palavra escolhida.
3. O jogador tem 12 tentativas para adivinhar a palavra, inserindo uma letra por vez.
4. A cada tentativa:
  - Se a letra estiver correta, ela é revelada na(s) posição(ões) correspondente(s).
  - Se a letra estiver errada, o número de tentativas restantes é reduzido, e uma mensagem de erro é exibida.
5. O jogo termina quando:
  - O jogador adivinha todas as letras da palavra (vitória).
  - As tentativas se esgotam (derrota)

## Requisitos

- **Python 3.x** deve estar instalado no seu sistema.
- Não é necessário instalar bibliotecas externas, apenas as bibliotecas padrão do Python (`random` e `math`).

## Como jogar

1. Execute o script Python.
2. Insira seu nome para começar o jogo.
3. Tente adivinhar a palavra escolhendo letras, uma por vez.
4. O sistema fornece feedback sobre quais letras já foram acertadas e quantas tentativas ainda restam.
5. O jogo termina quando você acertar a palavra ou esgotar todas as tentativas

### Exemplo de execução

```bash
Qual o seu nome? Diego  
Bem vindo, Diego!  
Esse é um jogo de adivinhação de palavras. Você tem 12 tentativas para acertar a palavra letra por letra!  
A palavra escolhida tem 7 letras!  
_ _ _ _ _ _ _  
Escolha uma letra: p  
Você errou! Lhe restam 11 tentativas.  
Escolha uma letra: r  
_ r _ _ _ _ _  
Escolha uma letra: o  
_ r o _ _ _ _  
Escolha uma letra: g  
_ r o g _ _ _  
Escolha uma letra: r  
Você venceu! A palavra era "program".  
!
```
## Regras

- A palavra escolhida é sempre uma das opções da lista predefinida no código.
- Você pode inserir uma ou mais letras por vez.
- Letras repetidas podem ser tentadas, mas não alteram o estado do jogo.
- O jogador vence ao descobrir todas as letras da palavra.

## Tratamento de Erros

- Caso o jogador insira algo que não seja uma letra (números, caracteres especiais, etc.), o comportamento do jogo dependerá da validação padrão do Python.

## Fonte de inspiração

Este projeto foi inspirado por um artigo do [GeeksforGeeks](https://www.geeksforgeeks.org/) sobre o jogo de adivinhação de números. Você pode conferir o artigo completo [aqui.](https://www.geeksforgeeks.org/python-program-for-word-guessing-game/)

## Contribuições

Sinta-se à vontade para fazer um fork deste projeto e sugerir melhorias!
