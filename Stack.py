class Stack:
    def  __init__(self, symbol):
        self.nro_elements = 0
        self.stack = []
        self.symbol = symbol

    def Add(self, obj): 
        self.stack.append(obj)
        self.nro_elements += 1

    def Pop(self):
        if self.nro_elements == 0:
            print("Stack empty...")
            ret = None
        elif self.nro_elements < 0:
            print("Error, Negative numbers")
            ret = None
        else:
            item_removed = self.stack[-1]
            self.stack = self.stack[:-1]
            self.nro_elements -= 1
            ret = item_removed

        return ret

    def Get_top(self):
        return self.stack[self.nro_elements-1]

    # Function to remove N elements
    def Remove_elements(self, nro_obj_to_remove): 
        lista = []
        if not isinstance(nro_obj_to_remove, int):
            print("Insert integer value.")
            return False, _

        if nro_obj_to_remove < 0:
            print("Insert non-negative value.")
            return False, _

        # Minimum value
        nro_obj_to_remove = min(nro_obj_to_remove, self.nro_elements)        

        # Remove N values
        for i in range(nro_obj_to_remove):
            elem = self.Pop()
            lista.append(elem)

        return lista
        
    def Get_number_elements(self):
        return self.nro_elements
        
    def Show_stack(self):
        print("Nro elements: ", self.nro_elements)
        for i in range(self.nro_elements):
            print(self.stack[i].Get_value_card())
            #print(self.stack[i])
        print("------------")
