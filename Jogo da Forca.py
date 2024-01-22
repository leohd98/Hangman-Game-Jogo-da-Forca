# JOGO DA FORCA POR LEONARDO HOFFMANN DIAS.
# 10/01/2024

# The program asks for the secret word.
palavra = str(input('Escolha a palavra: ')).upper()
resposta = list(palavra) # Create a list called 'resposta' with each individual letter.
teste = []
erro = 0
#-------------------------

# It creates a list called 'teste' with a blank space for each letter based on the length of the secret word 'palavra'.
for letra in palavra:
        if letra == ' ': # Space bar
             teste += ' '
        else:
             teste += '_'
#-------------------------
        
# Draws the start of the game, giving the player a tip about how many letters the secret word has.
# Also break the loop 'While' if the player lose (missing the letter 6x). 
while True:
    for jogo in range(99): # Creates 99 invisible lines so the player cant see what the secret word is while playing.
         print()
    print('=======')
    print('|     |')
    if erro >= 1:
         print(('|     O'))
    else:
         print('|')
    if erro == 2:
         print(('|     |'))
    elif erro == 3:
         print(('|    /|'))
    elif erro >= 4:
         print(('|    /|\\'))
    else:
         print('|')
    if erro == 5:
         print(('|    /'))
    elif erro == 6:
         print(('|    / \\'))
    else:
         print('|')
    for forca in range(3):
         print('|')
    print()
    print(*teste, sep = ' ')

    if erro == 6: # With 6 misses on gessing the word, the player loses.
         print()
         print('HAHA, VOCÊ PERDEU!')
         break
    
    print(f'\nA palavra secreta possui {len(palavra)} letras!') # Number of letters of the secret word.
    print(f'Número de erros: {erro}')
#-------------------------

# It adds the right letters to a list called 'teste' and also add the number of errors if the person chooses wrong.
    tentativa = str(input('\nTente adivinhar a palavra [digite 1 letra por vez ou contará como erro]: ')).upper()
    if tentativa not in palavra or len(tentativa) != 1:
         erro += 1
    elif tentativa in palavra:              
         x = palavra.find(tentativa)
         teste[x] = tentativa

         # If the letter typed by the player appears more than once on the secret word, it falls into this part here.
         # Lists cant add the same value more than once in some occasions, so this part fixes it.
         # I use the index to check positions.
         if palavra.count(tentativa) > 1:
          y = 0 # index position
          while y < len(palavra):
               for elemento in teste:
                    if tentativa == resposta[y] and teste[y] == '_':
                         teste[y] = tentativa
                         y += 1
                    else:
                         y += 1
          y = 0
#-------------------------
         
# It checks if the player won the game or not.        
    if teste == resposta:
        print()
        print('PARABÉNS, VOCÊ VENCEU O JOGO')
        break
#-------------------------  
