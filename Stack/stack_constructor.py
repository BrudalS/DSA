#  Last in first out (LIFO)
class Node:
	def __inti__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self, value):
		new_node = Node(value)
		#  Only need to keep track of top as its LIFO 
		#  No need of bottom
		self.top = new_node
		self.length = 1
