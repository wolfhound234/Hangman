import random

word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
start = input('Type "play" to play the game, "exit" to quit: ')
if start == 'play':
    random_word = random.choice(word_list)
    word_seal = "-" * (len(random_word))
    reveal = list(word_seal)
    whitelist = "abcdefghijklmnopqrstuvwxyz"

    i = 0
    tried_letter = []
    while i < 8:
        if word_seal == random_word:
            print('You guessed the word!')
            print('You survived!')
            break
        else:
            print()
            print(word_seal)
            guess = input('Input a letter: ')
            n = 0
            if guess in tried_letter:
                print('You already typed this letter')
            while n < len(random_word):
                if guess[-1] == random_word[n]:
                    reveal[n] = guess[-1]
                    word_seal = "".join(reveal)
                    n += 1
                    tried_letter.append(guess)
                else:
                    n += 1
            if len(guess) > 1:
                print('You should input a single letter')
            elif guess not in whitelist:
                print('It is not an ASCII lowercase letter')
            elif guess not in word_seal and guess not in tried_letter:
                tried_letter.append(guess)
                print('No such letter in the word')
                i += 1
    else:
        print('You are hanged!')
        start = input('Type "play" to play the game, "exit" to quit: ')
