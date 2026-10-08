

class node:
    def _init_(self):
        self.value=None
        self.next=None

class Linked_list:
    def (self):
        self.head=None
    def is_empty(self):
        return self.head==None
    def insert_first(self,x):
        if self.is_empty():
            new_node=node()
            new_node.value=x
            new_node.next=None
            self.head=new_node
        else:
            new_node=node()
            new_node.value=x
            new_node.next=self.head
            self.head=new_node
    def display(self):
        if self.is_empty():
            print("the linked list is empty\n")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.value)
                temp=temp.next





