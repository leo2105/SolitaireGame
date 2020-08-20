class Deck:
    def __init__(self):
        self.list = []
        self.id_actual = None
        self.nro_elements = 0
    
    def Add(self, obj):
        if self.nro_elements == 0:
            self.id_actual = 0
        self.list.append(obj)
        self.nro_elements += 1

    def Next_card(self):
        if self.nro_elements == 0:
            print("No cards in the deck")
        else:
            self.list[self.id_actual].Flip()
            self.id_actual = (self.id_actual + 1) % self.nro_elements
            self.list[self.id_actual].Flip()
        
            
    def Pick_card(self):
        if self.nro_elements == 0:
            print("Error: No cards in the deck")
            return None
        elif self.nro_elements == 1:
            print("No cards in the deck")
            card_aux = self.list.pop(self.id_actual)
            self.nro_elements -= 1
            self.id_actual = None          
            return card_aux
        else:
            card_aux = self.list.pop(self.id_actual)
            self.nro_elements -= 1
            self.id_actual = self.id_actual % self.nro_elements
            self.list[self.id_actual].Flip()
            return card_aux
    
    def Get_number_elements(self):
        return self.nro_elements