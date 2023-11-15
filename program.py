from random import choice
from words_english import all_words as english_words
from words_russia import all_words as russian_words
import frases as fr
from termcolor import colored
#import test_docstring

def color_string_letter(letter, color, string: list):
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
       
class GameMenu():
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

class ThisGame():
    '''This class contains some game constants and also the correct and answer word for each game'''

    def __init__(self, right_word, attempt=0, win=0, flag_quit=0, correct=0):
        self.num_letter = 5
        self.attempt = attempt
        self.win = win
        #flag for users win
        self.flag_quit = flag_quit
        #if user want to quit the game
        self.answer = []
        self.correct = correct
        #correct letters in word, that user enter
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
        

def main():
  while True:
    print(fr.language_frase)
      
    lang = input().lower()
    #language, that user choose
    match lang:
     
      case "eng":
        menu = GameMenu(english_words, fr.instraction_eng, fr.welcome_frase_eng, fr.detail_eng, fr.alphabet_eng, fr.to_play_eng, fr.word_eng, fr.lose_eng, fr.win_eng, fr.error_eng)
        
      case "rus":
        menu = GameMenu(russian_words, fr.instraction_rus, fr.welcome_frase_rus, fr.detail_rus, fr.alphabet_rus, fr.to_play_rus, fr.word_rus, fr.lose_rus, fr.win_rus, fr.error_rus)

      case _:
        print(fr.wrong_lang)
        continue
        
    #now all menu on english or on russia

    print(menu.welcome_frase)
    print(menu.detail)
    print(menu.play)

    #offer user instraction, exit or play again

    user_choice = input()
      
    match user_choice:
      case "p": 
      #play the game
            
        right_word = choice(menu.my_list).lower()
        game = ThisGame(right_word)
            
        print(menu.detail)
            
        while game.attempt < 6 and game.win==0:
              
          enter_word = input(menu.word).lower()

          match enter_word:
            case 'q':
              game.flag_quit = 1
              break
            case 'r':
              right_word = choice(menu.my_list).lower()
              game.reboot(right_word)
              continue
            case 'i':
              print(menu.instraction)
              continue
            case word if word.upper() not in menu.my_list:
              print(menu.error)
              continue

          game.attempt += 1
          game.correct = 0
              
          ans_string = ""

          for i in range(game.num_letter):
            if game.right_word[i] == enter_word[i]:
              game.correct += 1
              ans_string += colored(str(enter_word[i]), "green")
              menu.alphabet = color_string_letter(enter_word[i], "green", menu.alphabet)

              continue
            
            elif enter_word[i] in game.right_word:
              ans_string += colored(str(enter_word[i]), "yellow")
              menu.alphabet = color_string_letter(enter_word[i], "yellow", menu.alphabet)
              continue
                            
            else:
              ans_string += colored(str(enter_word[i]), "red")
              menu.alphabet = color_string_letter(enter_word[i], "red", menu.alphabet)
                                    
          game.answer.append(ans_string)
          game.print_ans(menu.alphabet)
          
          if game.correct == game.num_letter:
            game.win = 1
            break
          else:
            game.win = 0
                
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
              
      case 'r':
        continue
      case 'q':
        break
      case 'i':
        print(menu.instraction)
      case _:
        print("Eror 404")

main()
