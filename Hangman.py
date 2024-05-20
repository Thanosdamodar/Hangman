import random
from hangman_list import word_list
from hangman_stages import stages
live=6

##Choosing a random word from the word_list.
chosen_word=random.choice(word_list)

##Displays the numbers Underscore according to the word.
display=[]
for i in chosen_word:
  display.append("_")


end_of_game = False

##Game
while not end_of_game :
  
  ##Asking user to input their guess for the randomly chosen word.
  guess=input("Guess a letter:- ").lower()
  clear()
  if guess in display:
    print(f"You've already guessed {guess}")
  
  ##Checks if the guessed letter exists in the randomly chosen word.
  for i in range(len(chosen_word)):
    if chosen_word[i]==guess:
      display[i]=guess
  
  ##If the guessed word is not in the randomly selected word, the
  ##following code will deduct a live.
  if guess not in chosen_word:
    print(f"You've guessed \'{guess}\', that's not in the word. You lose a life.")
    live-=1

    ##If you don't have any more lives, the following code will end the     ##program.
    if live==0:
      end_of_game=True
      print(f'''The word was \"{chosen_word}\".
You Lose......''')
      
  ##Following code will join each letter in Display list so that we can
  ##show player the letters they are missing.
  word="".join(display)
  print(f'''{word}
{stages[live]}
Live:- {live}''')

  ##The following code will end the program if you guessed the word.
  if "_" not in display:
    end_of_game = True
    print("You Win......")
