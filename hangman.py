import random
from timeit import default_timer as timer  

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']  

logo = ''' 

  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
    '''
word_list = {
    'toy':'an object for a child to play with',
    'pizza': 'dish of Italian origin, consisting of a flat round bread',
    'badminton':'a game with rackets in which a shuttlecock',
    'flock': 'a collective noun for birds',
    'stopwatch':'a special watch with buttons that start, stop, and then zero the hands, used to time races.'
}

chosen_word, clue = random.choice(list(word_list.items()))
word_length = len(chosen_word)
print("...........................................................................................................\n")
print(f"Here's a HINT for you...{clue}")
print("\n...........................................................................................................")
try:
    with open(file="highscoretime.txt", mode="r") as file:
        current_high_score = float(file.readline())  
except:
    with open(file="highscoretime.txt", mode="w") as file:
        current_high_score = float("inf") 

print(f"The fastest time yet is {current_high_score} seconds.")
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo)
display = []
for _ in range(word_length):
    display += "_"
    
print(f"{' '.join(display)}")

start = timer()   #0.0
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()


    if guess in display:
        print(f"You've already guessed {guess}")

    
    for position in range(word_length): 
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

   
    if guess not in chosen_word:
        
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("The word was", chosen_word)
            print("GAME OVER ,YOU LOST, BETTER LUCK NEXT TIME ")

   
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")
        end = timer()
        time_elapsed = end - start
        print(f"The time you took is :{time_elapsed} seconds")
        if current_high_score > time_elapsed:
            print("CONGRATULATIONS THAT'S A NEW HIGHSCORE ")
            with open(file="highscoretime.txt", mode="w") as file:
                file.write(f"{time_elapsed}")
        else:
            print(f"That was a good attempt but our highscore is {current_high_score} seconds")
            print("BEAT IT THE NEXT TIME YOU TRY!! KEEP GOING. YOU ARE DOING AMAZING!!!")

    print(stages[lives])