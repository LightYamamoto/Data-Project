class Node:
    def __init__(self,ID,Name,DayofBirth,Birthplace):
        self.ID=ID
        self.Name=Name
        self.DayofBirth=DayofBirth
        self.Birthplace=Birthplace
        self.left=None
        self.right=None
    def printNode(self):
        print(self.ID, ' ', self.Name, ' ', self.DayofBirth, ' ', self.Birthplace)
        