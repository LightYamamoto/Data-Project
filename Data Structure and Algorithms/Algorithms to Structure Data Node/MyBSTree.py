from Node import Node
class MyBSTree:
    def __init__(self,root):
        self.root= root
        
        self.left= None
        self.right= None
    def insert(self,new_node):
        if self.root is not None:
            if new_node.ID < self.root.ID:
                if self.left is not None:
                    self.left.insert(new_node)
                else:
                    self.left=MyBSTree(new_node)

            elif new_node.ID > self.root.ID:
                if self.right is not None:
                    self.right.insert(new_node)
                else:
                    self.right= MyBSTree(new_node)

            elif new_node.ID ==  self.root.ID:
                return
        else:
            self.root = new_node



    
    # Search by ID function
    def search(self, ID):
        # 1.Check if the BSTree's root is available
        if self.root is not None:
            if ID < self.root.ID:
                if self.left is None:
                    return None
                return self.left.search(ID)
                                
            elif ID > self.root.ID:
                if self.right is None:
                    return None
                return self.right.search(ID)
               
            else:
                return self.root
                
    # 3 Function:
    def InorderTraversal(self):
        res=[] 
        if self.left is not None:
            res += self.left.InorderTraversal()
        res.append(self.root)
        if self.right is not None:
            res += self.right.InorderTraversal()

        return res

    #4 Remove Node Function:
    def remove(self, ID):
        # check if tree is empty
        if self.root is None:
            print('BST is empty')
            return
        # find the node
        if ID < self.root.ID:
            if self.left is not None:
                self.left = self.left.remove(ID)
            else:
                print('{} is not present in BST'.format(ID))
        elif ID > self.root.ID:
            if self.right is not None:
                self.right = self.right.remove(ID)
            else:
                print('{} is not present in BST'.format(ID))
        # remove that node (three cases - 0, 1, or 2 childs)
        else:
            # if left is None, return right, and vice-versa
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            # find the mind_value in right side of delection node
            node = self.right
            while node.right is not None:
                node = node.right
            self.root = node.root
            self.right = self.right.remove(node.root.ID)
        return self

    




