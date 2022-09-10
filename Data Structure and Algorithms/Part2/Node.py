class Node:
    def __init__(self,data=None):
        self.next=None
        if data is not None:
            self.data=data
            self.id,self.tittle,self.quantity,self.price=data.split()
        else:
            
            self.id=input("Please input new Product's id")
            self.tittle=input("Please input new Product'tille")
            self.quantity=input("Please input new Product's quantity")
            self.price=input("Please input new Product's Price")
            
            self.data=' '.join([self.id,self.tittle,self.quantity,self.price])
        
    def __str__(self):
        return self.data
    # Update data mới khi con trỏ trỏ tới Node mới
    def update(self):
        self.id,self.tittle,self.quantity,self.price=self.data.strip().split()
        

