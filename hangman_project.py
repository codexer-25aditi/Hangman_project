

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
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

display=[]
l=len(chosen_word)
for i in range(0,l):
  display.append('_')
  
lives=6



end_of_game="False"
while end_of_game=="False":
  guess = input("Guess a letter: ").lower()
  count=-1
  for letter in chosen_word:
    count=count+1
    if letter == guess:
      
        display[count]=letter
      
  if guess not in chosen_word:
    lives-=1
    if lives==0:
       print("You loose,better luck next time")
       end_of_game="True"
  print(stages[lives])       
   
  print(display)    
  if '_' in display:
    continue
  elif '_' not in display:
    end_of_game="True"
    print("Yay you have won!!")
  else:
    end_of_game="True"
  
