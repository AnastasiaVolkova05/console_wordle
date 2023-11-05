from random import choice
from words_for_wordle import all_words as english_words
from words_russia import all_words as russian_words
import frases as fr
from termcolor import colored
#import test_docstring

def Color_string_letter(letter, color, string: list):
    '''This function color the element in the list.
       Keys:
       letter - the element in list, that you need to color;
       color - green, red or yellow;
       string - list, that include our elemnt'''
    tmp = []
    for k in range(len(string)):
        if string[k] == letter:
            tmp.append(colored(string[k], color))
        elif (color == "green" and colored(letter, "yellow") == string[k]):
            tmp.append(colored(letter, color))
        else:
            tmp.append(string[k])
    return tmp.copy()
       
class Game_menu():
    '''This class contains some frases, that you need to display during the game.
    
       This class hasn't got any methods'''
    def __init__(self, wordlist, instraction, welcome_frase, detail, alphabet, play, word, lose, win, error):
        self.instraction = instraction
        self.welcome_frase = welcome_frase
        self.detail = detail
        self.alphabet = alphabet
        self.my_list = wordlist[:]
        self.play = play
        self.word = word
        self.lose = lose
        self.win = win
        self.error = error  
    
    
class This_game(Game_menu):
    '''This class contains some game constants and also the correct and answer word for each game'''
    def __init__(self, right_word, attempt=0, win=0, flag_quit=0, answer=[],correct=0):
        self.attempt = attempt
        self.win = win #flag for users win
        self.flag_quit = flag_quit #if user want to quit the game
        self.answer = answer
        self.correct = correct #correct letters in word, that user enter
        self.right_word = right_word
    def reboot(self, right_word):
        '''This method reboot the game.
        
          Rewrites the correct word, deletes the previous answer, 
          resets the number of attempts'''
        self.attempt = 0
        self.right_word = right_word
        self.answer = []
    def print_ans(self, alphabet):
        '''This method print the answer'''
        for i in range(len(self.answer)):
          print(self.answer[i])
        print(''.join(alphabet))
    def set_default(self):
        self.attempt = 0
        self.win = 0
        self.flag_quit = 0
        self.answer = []
        self.correct = 0 
        


while True:
  print(fr.language_frase)
  
  lang = input()  #language, that user choose

  if lang.lower() == "eng":
    menu = Game_menu(english_words, fr.instraction_eng, fr.welcome_frase_eng, fr.detail_eng, fr.alphabet_eng, fr.to_play_eng, fr.word_eng, fr.lose_eng, fr.win_eng, fr.error_eng)
    
  elif lang.lower() == "rus":
    menu = Game_menu(russian_words, fr.instraction_rus, fr.welcome_frase_rus, fr.detail_rus, fr.alphabet_rus, fr.to_play_rus, fr.word_rus, fr.lose_rus, fr.win_rus, fr.error_rus)

  else:
    print(fr.wrong_lang)
    continue
    
#now all menu on english or on russia

  print(menu.welcome_frase)
  print(menu.detail)
  print(menu.play)

#offer user instraction, exit or play again

  user_choice = input()
  
  if user_choice == "p": #play the game
    
    right_word = choice(menu.my_list).lower()
    game = This_game(right_word)
    
    print(menu.detail)
    
    while game.attempt<6 and game.win==0:
      
      enter_word = input(menu.word).lower()

      if enter_word == 'q':
        game.flag_quit = 1
        break 
        
      if enter_word == 'r':
        right_word = choice(menu.my_list).lower()
        game.reboot(right_word)
        continue
        
      if enter_word == 'i':
        print(menu.instraction)
        continue

      if enter_word.upper() not in menu.my_list:
        print(menu.error)
        continue

      game.attempt += 1
      
      ans_string = ""

      for i in range(5):
        if game.right_word[i] == enter_word[i]:
            game.correct += 1
            ans_string += colored(str(enter_word[i]), "green")
            menu.alphabet = Color_string_letter(enter_word[i], "green", menu.alphabet)

            continue

        if enter_word[i] in game.right_word:
            ans_string += colored(str(enter_word[i]), "yellow")
            menu.alphabet = Color_string_letter(enter_word[i], "yellow", menu.alphabet)
            continue
                
        ans_string += colored(str(enter_word[i]), "red")
        menu.alphabet = Color_string_letter(enter_word[i], "red", menu.alphabet)
                        
      game.answer.append(ans_string)

      if game.correct == 5:
        game.win = 1
        game.print_ans(menu.alphabet)
        break
      else:
        game.win = 0
        game.print_ans(menu.alphabet)
    
    if game.flag_quit:
      game.set_default()
      break
    else:
      if game.win == 1:
        game.set_default()
        print(menu.win)
      else:
        game.set_default()
        print(menu.lose)
  elif user_choice == 'r':
    continue
  elif user_choice == 'q':
    break
  elif user_choice == 'i':
    print(menu.instraction)
  else:
    print("Eror 404")
