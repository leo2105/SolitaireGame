from Solitaire import Solitaire
from getkey import getkey, keys
from colorama import Fore, Back, Style, init

def Print_menu():
    print("\n[N] : Next Card in Deck")
    print("[M_#pile_#pile] : Move from Pile to another one")
    print("[H_#pile_#hand] : Move from Pile to Hand")
    print("[T_#hand] : Move from Deck to Hand")
    print("[D_#pile] : Deck to Pile")
    print("[Q] : Quit game")

def Update():
    print("\n\t\t\t\t", Style.BRIGHT + "JOGO PACIENCIA\n")
    solitaire_game.Update_table()
    solitaire_game.table.Draw()
    Print_menu()

def Win_condition():
    cond = True
    for hand in solitaire_game.arr_hands:
        cond = cond and (True if hand.nro_elements == 13 else False)
    return cond

solitaire_game = Solitaire()
solitaire_game.Setup()
Update()

while True:
    _input  = input("Choose an option: ")
    try:
        if _input[0] == "n" or _input[0] == "N":
            solitaire_game.deck.Next_card()

        elif _input[0] == 'm' or _input[0] == 'M':
            arr = _input.split('_')[1:]
            id_col_from, id_col_to = int(arr[0]), int(arr[1])
            solitaire_game.Move_pile_pile(id_col_from, id_col_to)

        elif _input[0] == 'h' or _input[0] == 'H':
            arr = _input.split('_')[1:]
            id_col_from, id_col_to = int(arr[0]), int(arr[1])
            solitaire_game.Move_pile_hand(id_col_from, id_col_to)

        elif _input[0] == 't' or _input[0] == 'T':
            hand_id = int(_input.split('_')[1])
            solitaire_game.Move_deck_hand(hand_id)

        elif _input[0] == 'd' or _input[0] == 'D':
            pile_id = int(_input.split('_')[1])
            solitaire_game.Move_deck_pile(pile_id)

        elif Win_condition():
            print("\n\n\t\t\t" + Style.BRIGHT + "YOU WON\n\n")
            break

        elif _input[0] == 'q' or _input[0] == 'Q':
            print("\n\n\t\t\t" + Style.BRIGHT + "THANKS FOR PLAYING\n\n")
            break
    
        else:
            print("Invalid input")
    
    except:
        print("Invalid input")
        
    Update()
    
    