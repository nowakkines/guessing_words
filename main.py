# rich
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

# random
from random import choice

# time
from time import sleep

# variables
console = Console()
heart = '♡ '
tries = 5
word_list = ['time', 'human', 'president']


def get_word(word_list):
    return choice(word_list).upper()


def display_hangman(tries):  #принимает один аргумент tries – количество попыток угадывания слова и возвращает текущее состояние игры в графическом виде
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
                # голова, торс, обе руки
                 '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
               # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',                  # начальное состояние
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tries]


def hello():
    console.print(Panel(
      '''
      Правила довольно просты : вы должны ввести либо букву, либо слово.
      [red]У вас имеется только 5 попыток[/red], но помните, что при вводе неправильного слово вы автоматически проигрываете.
      Все буквы заглавные!
      ''', title='Hangman'), justify='center')
    console.print('↓↓  Ваше текущее положение ↓↓ ', justify='center')
    print(display_hangman(tries))
    play(tries)

# def question():
#      match input('Не хотели бы вы продолжить игру? '):
#         case '+':
#             play(tries)
#         case '-':
#             break

# play
def play(tries):
    result = get_word(word_list)
    word_completion = '_' * len(result)
    word_as_lst = list(word_completion)
    guessed_letters = []
    guessed_word = []
    word_count = word_completion.count('_')
    for _ in track(range(50), description='[green]Processing...'):
        sleep(0.03)
    print(f'[red]Слово было сгенерировано[/red]: {word_completion} ОСТАЛОСЬ {word_count} БУКВ {result}')

    while word_completion != result and tries != 0:
        letter = input('Введите букву или слово >> ')
        indices = [x for x in range(len(result)) if result[x] == letter]
   # If there is no letter and it's correct
        if is_valid(letter, result):
            if len(letter) == 1 and letter in guessed_letters:
                print('[red]Вы ввели букву, которая была использована.')
            elif letter == result: # if len(letter) == len(word) and letter == word:
                print('Вы отгадали слово, вы умница.')
                break
            elif len(letter) == 1 and letter not in result:
                print('Вы ввели неправильную букву. Т.к вы ввелите неправильно, ваша попытка исчерпана.')
                tries -= 1
                console.print('↓↓  Ваше текущее положение ↓↓ ', justify='center')
                print(display_hangman(tries))
            elif len(letter) == 1 and letter in result and letter not in guessed_letters:
                guessed_letters.append(letter)
                for index in indices:
                    word_as_lst[index] = letter
                    word_completion = ''.join(word_as_lst)
                print(word_completion)
                # print(f'У вас осталось: [{heart * tries}]')
            # word
            elif letter != result:
                print('Вы ввелите неправильно слово, поэтому вы автоматически проиграли')
                break
                # question()


#TODO: Добавить функцию для отображения попыток.
#TODO: Добавить функцию для повтора.
#FIXME: Не отображается информация, если в конечном вводить все правильные слова.






def is_valid(value, result):
    return value.isalpha() and (len(value) == 1 or len(value) == len(result))
if __name__ == '__main__':

    hello()
