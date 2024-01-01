from node import Node

class Stack:
    def __init__(self,value):
        new_node = Node(value=value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            print('|')
            print('v')
            temp = temp.next
        print()
    
    def push(self,value):
        new_node = Node(value=value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp
    
