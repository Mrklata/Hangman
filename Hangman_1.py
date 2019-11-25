import random


class Game:
    def __init__(self):
        self.selected_word = self.word()
        self.word_constant = self.selected_word
        self.lives = 7
        self.used_letter = set()
        self.check_used_letter = set()
        self.temp = ''

    @staticmethod
    def word():
        with open("./lista.txt") as opened_file:
            read_file = opened_file.read()
            split_file = read_file.split(", ")
        x = random.randint(0, len(split_file) - 1)
        return split_file[x]

    def print_word(self, letter):
        temp = self.temp
        self.used_letter.add(letter)
        for i in self.word_constant:
            if i in self.used_letter:
                temp += i
            else:
                temp += '_ '
        print(temp)


def main():
    game = Game()
    print(len(game.selected_word) * '_ ')
    check(game)


def check(game):
    if set(game.selected_word) == set('0'):
        return print('Wygrana')
    elif game.lives == 0:
        return print(f'Przegrana\nTwoje słowo to {game.word_constant}')
    else:
        letter = input("Wprowadż litere").lower()
        game.print_word(letter)

        if len(letter) != 1 or letter in game.check_used_letter:
            check(game)
        if letter in game.selected_word:
            game.selected_word = game.selected_word.replace(letter, '0')
            print('Dobra robota!!!')
            game.check_used_letter.add(letter)
            check(game)

        else:
            game.lives -= 1
            print(f'Stracona szansa, zostało {game.lives} szans')
            game.check_used_letter.add(letter)
            check(game)


if __name__ == '__main__':
    main()
