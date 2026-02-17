import random
word_bank=["hello","bonjour","anneyong","Hi","namaste"]
word=random.choice(word_bank).lower()

guessword= ["_"]*len(word)

attempt=10

while attempt>0:
    print("\ncurrent word: "+" ".join(guessword))

    guess=input("guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessword[i]=guess
        print("dayum!right!")
        
    else:
        attempt -=1
        print('Wrong guess! Attempts left:'+ str(attempt))
    
    if '_' not in guessword:
        print('\nCongratulations!! You guessed the word:' ,word)
        break

if attempt==0 and "_" in guessword:
    print('\nYou\'ve run out of attempts! The word was:' ,word)
        
        