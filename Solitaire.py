from Stack import Stack
from Card import Card
from Deck import Deck
from Table import Table
import random
from colorama import Fore, Back, Style, init

class Solitaire:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.letters = ['♦', '♠', '♥', '♣']
        self.num2letra = {1:'A', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'J', 12:'Q', 13:'K'}
        self.values_letters = [[x, y] for x in self.values for y in self.letters]
        random.shuffle(self.values_letters)
        self.arr_piles = [[], [], [], [], [], [], []]
        self.arr_hands = [Stack('♦'), Stack('♠'), Stack('♥'), Stack('♣')]
        self.deck = Deck()
        self.table = Table()

        init(autoreset=True)

    def Setup(self):
        arr_cards = []
        for i in range(28):
            symbol = self.values_letters[i][1]
            if symbol == '♦' or symbol == '♥':
                arr_cards.append(Card(self.values_letters[i][0], self.values_letters[i][1], True, fg=Fore.WHITE, bg=Back.RED))
            else:
                arr_cards.append(Card(self.values_letters[i][0], self.values_letters[i][1], True, fg=Fore.WHITE, bg=Back.BLACK))

        # Init piles
        idx = 0
        for idy in range(7):
            for i in range(idy+1):
                self.arr_piles[idy].append(arr_cards[idx])
                idx += 1
            self.arr_piles[idy][-1].Flip()

        # Init deck
        for i in range(28, len(self.values_letters)):
            symbol = self.values_letters[i][1]
            if symbol == '♦' or symbol == '♥':
                self.deck.Add(Card(self.values_letters[i][0], self.values_letters[i][1], True, fg=Fore.WHITE, bg=Back.RED))
            else:
                self.deck.Add(Card(self.values_letters[i][0], self.values_letters[i][1], True, fg=Fore.WHITE, bg=Back.BLACK))
        self.deck.list[self.deck.id_actual].Flip()

    def Move_pile_pile(self, id_from, id_to):
        if len(self.arr_piles[id_to-1]) == 0:
            for i in range(len(self.arr_piles[id_from-1])):
                if self.arr_piles[id_from-1][i].value == 13 and not self.arr_piles[id_from-1][i].Get_is_hidden():
                    arr_cards2move = self.arr_piles[id_from-1][i:]
                    self.arr_piles[id_from-1] = self.arr_piles[id_from-1][:i] 
                    self.arr_piles[id_to-1] = arr_cards2move
                    for k, j in enumerate(range(i, len(self.arr_piles[id_from-1])+len(arr_cards2move))):
                        self.table.table[j+5][id_from-1] = None   
                    if len(self.arr_piles[id_from-1]) > 0 and self.arr_piles[id_from-1][-1].Get_is_hidden():
                        self.arr_piles[id_from-1][-1].Flip()
                    break
        else:
            last_number = self.arr_piles[id_to-1][-1].value
            last_symbol = self.arr_piles[id_to-1][-1].symbol
            for i in range(len(self.arr_piles[id_from-1])):
                if not self.arr_piles[id_from-1][i].Get_is_hidden():
                    val_aux = self.arr_piles[id_from-1][i].value
                    sym_aux = self.arr_piles[id_from-1][i].symbol
                    if ((last_symbol == self.letters[0] or last_symbol == self.letters[2]) and (sym_aux == self.letters[1] or sym_aux == self.letters[3])) or \
                        ((last_symbol == self.letters[1] or last_symbol == self.letters[3]) and (sym_aux == self.letters[0] or sym_aux == self.letters[2])):
                            if val_aux + 1 == last_number: 
                                arr_cards2move = self.arr_piles[id_from-1][i:]
                                self.arr_piles[id_from-1] = self.arr_piles[id_from-1][:i] 
                                self.arr_piles[id_to-1] = self.arr_piles[id_to-1] + arr_cards2move
                                for k, j in enumerate(range(i, len(self.arr_piles[id_from-1])+len(arr_cards2move))):
                                    self.table.table[j+5][id_from-1] = None   
                                if len(self.arr_piles[id_from-1]) > 0 and self.arr_piles[id_from-1][-1].Get_is_hidden():
                                    self.arr_piles[id_from-1][-1].Flip()    
                                break 


    def Move_pile_hand(self, id_from, id_to):
        if self.arr_hands[id_to-1].Get_number_elements() == 0:
            aux_card = self.arr_piles[id_from-1][-1]
            if aux_card.value == 1 and aux_card.symbol == self.arr_hands[id_to-1].symbol:
                self.arr_hands[id_to-1].Add(aux_card)
                self.arr_piles[id_from-1] = self.arr_piles[id_from-1][:-1]
                self.table.table[len(self.arr_piles[id_from-1])+5][id_from-1] = None
                if len(self.arr_piles[id_from-1]) > 0 and self.arr_piles[id_from-1][-1].Get_is_hidden():
                    self.arr_piles[id_from-1][-1].Flip()
        else:
            aux_card_from = self.arr_piles[id_from-1][-1]
            aux_card_to = self.arr_hands[id_to-1].Get_top()
            if aux_card_from.value == aux_card_to.value + 1 and aux_card_from.symbol == aux_card_to.symbol:
                self.arr_hands[id_to-1].Add(aux_card_from)
                self.arr_piles[id_from-1] = self.arr_piles[id_from-1][:-1]
                self.table.table[len(self.arr_piles[id_from-1])+5][id_from-1] = None
                if len(self.arr_piles[id_from-1]) > 0 and self.arr_piles[id_from-1][-1].Get_is_hidden():
                    self.arr_piles[id_from-1][-1].Flip() 

    def Move_deck_pile(self, pile_id):
        if self.deck.nro_elements > 0:
            if len(self.arr_piles[pile_id-1]) == 0:
                card_deck = self.deck.list[self.deck.id_actual]
                if card_deck.value == 13:
                    card_picked = self.deck.Pick_card()
                    self.arr_piles[pile_id-1].append(card_picked)
            else:
                card_deck = self.deck.list[self.deck.id_actual]
                last_card_pile = self.arr_piles[pile_id-1][-1]
                last_symbol = last_card_pile.symbol
                sym_aux = card_deck.symbol
                if last_card_pile.value == card_deck.value + 1 and (
                    ((last_symbol == self.letters[0] or last_symbol == self.letters[2]) and (sym_aux == self.letters[1] or sym_aux == self.letters[3])) or \
                    ((last_symbol == self.letters[1] or last_symbol == self.letters[3]) and (sym_aux == self.letters[0] or sym_aux == self.letters[2]))):
                    card_picked = self.deck.Pick_card()
                    self.arr_piles[pile_id-1].append(card_picked)
            
    def Move_deck_hand(self, hand_id):
        if self.deck.nro_elements > 0:
            card_deck = self.deck.list[self.deck.id_actual]
            if self.arr_hands[hand_id-1].Get_number_elements() == 0:
                if card_deck.value == 1 and card_deck.symbol == self.letters[hand_id-1]:
                    card_picked = self.deck.Pick_card()
                    self.arr_hands[hand_id-1].Add(card_picked)
            else:
                aux_card_to = self.arr_hands[hand_id-1].Get_top()
                if card_deck.value == aux_card_to.value + 1 and card_deck.symbol == self.letters[hand_id-1]:
                    card_picked = self.deck.Pick_card()
                    self.arr_hands[hand_id-1].Add(card_picked)

    def Update_table(self):
        str_hd_val = 'X' if self.deck.Get_number_elements() == 0 else str(self.num2letra[self.deck.list[self.deck.id_actual].Get_value_card()])
        str_hd_sym = 'X' if self.deck.Get_number_elements() == 0 else self.deck.list[self.deck.id_actual].Get_symbol_card()
        self.table.table[2][0] = "{:^10}".format(str_hd_val+str_hd_sym)
        if self.deck.Get_number_elements() > 0:
            self.table.table[2][0] = self.deck.list[self.deck.id_actual].bg + self.table.table[2][0] + Style.RESET_ALL
        arr_str_hand_val, arr_str_hand_sym, arr_str_hand_bg  = [], [], []
        for i in range(4):
            arr_str_hand_val.append('X' if self.arr_hands[i].Get_number_elements() == 0 else str(self.num2letra[self.arr_hands[i].Get_top().Get_value_card()]))
            arr_str_hand_sym.append('X' if self.arr_hands[i].Get_number_elements() == 0 else self.arr_hands[i].Get_top().Get_symbol_card())
            arr_str_hand_bg.append( "" if self.arr_hands[i].Get_number_elements() == 0 else self.arr_hands[i].Get_top().bg)
            self.table.table[2][3+i] = arr_str_hand_bg[i]+"{:^10}".format(arr_str_hand_val[i]+arr_str_hand_sym[i])+Style.RESET_ALL
        for j, pile in enumerate(self.arr_piles):
            for i in range(len(pile)):
                self.table.table[i+5][j] = "{:^10}".format("--" if pile[i].Get_is_hidden() else str(self.num2letra[pile[i].Get_value_card()]) + str(pile[i].Get_symbol_card()))
                if not pile[i].Get_is_hidden():
                    self.table.table[i+5][j] = pile[i].bg + self.table.table[i+5][j] + Style.RESET_ALL
        