from colorama import Fore, Back

class Card:
    def __init__(self, value, symbol, is_hidden=True, fg=Fore.WHITE, bg=Back.BLACK):
        self.value = value
        self.symbol = symbol
        self.is_hidden = is_hidden
        self.fg = fg
        self.bg = bg

    def Flip(self):
        self.is_hidden = False if self.is_hidden else True
    
    def Get_value_card(self):
        return self.value
    
    def Get_symbol_card(self):
        return self.symbol
    
    def Get_is_hidden(self):
        return self.is_hidden
