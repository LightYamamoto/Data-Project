#Stack by linked list
from Node import Node
class Stack:
	def __init__(self):
		self.root = None
	def isEmpty(self):
		if self.root is None:
			return True 
		return False
    #Thêm ở đầu- Push new Node into self.root
	def push (self,data):
		newNode = Node(data)
		newNode.next = self.root
		self.root = newNode
    #Xóa ở đầu -Pop in the self.root 
	def pop(self):
		if self.isEmpty():
			
			return 
		popped_node=self.root		
		self.root = self.root.next		
		
		return popped_node.data
		
	# Peek-Xuát ra data ở root
	def peek(self):
		if self.root is None:
			return 'Stack clear'
			
		return self.root.data
