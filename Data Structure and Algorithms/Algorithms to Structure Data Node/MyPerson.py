from Node import Node
from MyBSTree import MyBSTree
from MyQueue import MyQueue


class Operation:
    def __init__(self):
        self.MyBSTree=MyBSTree(None)
        self.MyQueue = MyQueue()
    def load(self):
        while True:
            try:
                f=open(input('Please enter file path: '),'r')
                print(' The file is loaded successfully')
                break
            except:
                print('File path is not correct')

        # Split data into ID,Name,DayofBirth,Birthplace        
        f.readline()
        for line in f:
            arr = list(line.strip().split(','))
            new_employee = Node(arr[0],arr[1],arr[2],arr[3])
            self.MyBSTree.insert(new_employee)
        f.close()

    # 2 Insert new_employee
    def insert(self):
        IDExist = True
        while IDExist is True:            
            ID= input('Please insert the New ID:')
            check_id = self.MyBSTree.search(ID)                         
            if check_id is None:
                print('The Employee ID can be used')
                IDExist = False
            else:
                print('This ID has been chosen, please choose another ID!')
        
        Name = input("Please insert the Name:")
        DayofBirth = input("Please insert the Day of Birth:")
        Birthplace = input("Please insert the Birth Place:")
        new_employee = Node(ID, Name, DayofBirth, Birthplace)
        # Add to Tree
        self.MyBSTree.insert(new_employee)
        print("New ID:", new_employee.ID)
        print("Name:", new_employee.Name)
        print("Date of birth:", new_employee.DayofBirth)
        print("Birthplace:", new_employee.Birthplace)
        
        input('Please type anything to come back to the main menu!')

    # Function 3: Inorder Traversal
    def InorderTraversal(self):
        print('ID | Name | Day of Birth | Birthplace')
        res = self.MyBSTree.InorderTraversal()
        for Node in res:
            Node.printNode()
        
        input('Please type anything to come back to the main menu!')
        return 

    # 4. Breath First Search
    def BFS(self):
        print("ID | Name | Day of Birth | Birthplace")
        if self.MyBSTree is None:
            return 
        self.MyQueue.add(self.MyBSTree)
        
        # Loop Queue and PrintNode following BFS order
        while self.MyQueue.peek() is not None:
            cur_node= self.MyQueue.remove()
            cur_node.root.printNode()
            if (cur_node.left is not None):
                self.MyQueue.add(cur_node.left)
            if (cur_node.right is not None):
                self.MyQueue.add(cur_node.right)
        input("Please type anything to come back to the main memu")

    # 5. Search by ID
    def SearchByID(self):
        
        Search_ID=input('Please insert the ID for Searching:')
        print(f'Search for ID = {Search_ID}')
        search_node =  self.MyBSTree.search(Search_ID)
    
        if search_node is None:
            print( 'The searched ID is not valid.')
            return
        
        print("ID | Name | Day of Birth | Birthplace")
        search_node.printNode()
        input("Please type anything to come back to the main memu")
        return

    # 6. Delete by ID
    def DeleteByID(self):
        Search_ID=input('Please insert the ID for Deleting:')
        print(f'Delete the person with ID = {Search_ID}')
        search_node = self.MyBSTree.search(Search_ID)
        if search_node is not None:
            print( 'ID | Name | Day of Birth | Birthplace')
            self.MyBSTree.remove(Search_ID)
            search_node.printNode()
        else:
            print('The searched ID is not valid.')
        
        input('Please type anything to come back to the main menu!')



#Operation=Operation()
#Operation.load()
#Operation.insert()
#Operation.InorderTraversal()
#Operation.BFS()
#Operation.DeleteByID()
#Operation.InorderTraversal()