from Node import Node
import Mylist
import Mystack
import MyQueue
class OperationToProduct:
    def __init__(self):
        self.llist=Mylist.LinkedList()
    # 1. load file Data.txt
    def load(self):
        while True:
            try:
                f=open(input('Please enter the find path: '))
                print('The file is load successfully!')
                break
            except:
                print('File-path is not correct')
        # 1.2 Load data to LinkedList
        for line in f:
            product=Node(line)
            self.llist.append_node(product)
        f.close()
        
    # 2. Append product in the end of LinkedList
    def append(self):
        new_product=Node()
        self.llist.append_node(new_product)

    # 3. Display product information in the LinkedList(self.llist)     
    def display(self):
        self.llist.printList()
    
    # 4. Save Product's LinkedList to into given file
    def saveProductListToFile(self):
        f=open(input('Please enter the output path: '),'w')
        cur_node=self.llist.head
        while cur_node:
            f.write(f'{cur_node.data}')
            cur_node=cur_node.next
        print('The file is saved successfully!')
        f.close()

    #5 search by ID
    def searchByID(self):
        id = input('Please enter the ID: ')
        cur_node = self.llist.head
        while cur_node:
            if cur_node.id == id:
                print("ID |  Title   | Quantity | Price")
                print(cur_node.id," | ", cur_node.tittle, " | ", cur_node.quantity , " | ",cur_node.price)
                
                return cur_node.data        
            cur_node =cur_node.next
        
        print("ID is not in the dataset!")
       
        
    
    #6 Delete By ID
    def deletebyID(self):
        data=self.searchByID()
        
        if data==None:
            
            return
        print('The product is removed from the dataset successfully!')
        self.llist.delete_data(data)
         

    #7 Sort by ID:
    def sortByID(self):
        # Save nodes.data of llist in list table for sorting
        table = []
        cur_node = self.llist.head       
        while cur_node:
            table.append(cur_node.data)
            cur_node = cur_node.next
        table.sort() #Sorting data in the list table
        
        #Khai lại các node theo thứ tự đã đc sắp xếp
        f_node = self.llist.head
        index = 0
        while f_node:
            f_node.data = table[index]
            index +=1
            f_node.update()
            f_node = f_node.next
        return self.llist.printList()

    #8 Convert giá trị Quantity sang Binary
    def convertToBinary(self):
        
        data=self.searchByID()
        if data is None:
            return

        quantity=int(data.strip().split()[2])

        binary=[]
        while quantity>= 1:    
            binary.append(quantity%2)
            quantity //= 2
        #print("ID |  Title   | Quantity | Price")
        #product=data.strip().split()
        #print(product[0]," | ", product[1], " | ", product[2] , " | ",product[3])
        print('Convert quantity to binary: ',''.join(str(a) for a in binary))
        
    #9: Load to stack and display
    def loadToStackAndDisplay(self):
        self.stack_list=Mystack.Stack()
        while True:
            try:
                f=open(input('Please enter the file path:'))
                print('The file is load successfully!')
                break
            except:
                print('File path is not correct')
        for line in f:
            self.stack_list.push(line.strip())
        f.close()
        print("ID |  Title   | Quantity | Price")
        while self.stack_list is not None:
            product=[]
            try:
                product=self.stack_list.pop().split()
            except:
                return
            print(product[0]," | ", product[1], " | ", product[2] , " | ",product[3])
            
    #10: Load to queue and display
    def loadToQueueAndDisplay(self):
        self.Queue_list=MyQueue.Queue()
        while True:
            try:
                f=open(input('Please enter the file path:'))
                print('The file is load successfully!')
                break
            
            except:
                print("The file path is incorrect")
        for line in f:
            self.Queue_list.enQueue(line.strip())
        f.close()
        print("ID |  Title   | Quantity | Price")
        while self.Queue_list is not None:
            product=[]
            try:
                product=self.Queue_list.deQueue().split()                            
                print(product[0]," | ", product[1], " | ", product[2] , " | ",product[3])
            except: return










#Test Execution
#Ruler=OperationToProduct()
#Ruler.load()
#Ruler.display()
#Ruler.searchByID()
#Ruler.deletebyID()   
#Ruler.sortByID()
#Ruler.convertToBinary()
#Ruler.loadToStackAndDisplay()
#Ruler.loadToQueueAndDisplay()