from Node import Node
class Queue:
	def __init__ (self):
		self.front = self.rear = None
	def isEmpty(self):
		return self.front == None
	def enQueue(self, data):
		newNode = Node(data)
		if self.rear == None:
			self.front = self.rear = newNode
			return
		self.rear.next = newNode
		self.rear = newNode
		
	# Delete Node at self.front position
	def deQueue(self):
		if self.isEmpty():
			return
		cur_Node = self.front
		
		self.front = cur_Node.next
		# Đk quyết định còn Queue hay không
		if self.front == None:
			self.rear = None
		return cur_Node.data