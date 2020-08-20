# Thanks: 
# Colorama project : https://pypi.org/project/colorama/
from colorama import Fore, Back, Style, init

class Table:
    def __init__(self):
        self.table = [
                ['out', 'out', 'out', 'out', 'out', 'out', 'out'],
                ['Deck', 'out', 'out', 'Hand ♦', 'Hand ♠', 'Hand ♥', 'Hand ♣'],
                [None, 'out', 'out', None, None, None, None],
                ['out', 'out', 'out', 'out', 'out', 'out', 'out'],
                ['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7'],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None]]

        self.width = 7
        self.height = 20

    def Draw(self):
        for i in range(self.height):
            string = ""
            for j in range(self.width):
                aux = self.table[i][j]
                if aux == 'out':
                    string += "{:^12}".format("")
                elif aux == 'Hand ♦' or aux == 'Hand ♥':
                    string += (Back.RED + "|{:^10}|".format(aux) + Style.RESET_ALL)
                elif aux == 'Hand ♠' or aux == 'Hand ♣':
                    string += (Back.BLACK + "|{:^10}|".format(aux) + Style.RESET_ALL)
                elif aux is not None:
                    string += "|{:^10}|".format(aux) 
                else:
                    string += "|{:^10}|".format("")
                
            print(string)



