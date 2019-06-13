# sorted linked list in Python

# Darren Byrne C16735211


class SortedLL:

	def _init_(self):
		self.dummy = Node(None, None)
		self.dummy.next = self.dummy
		self.head = Node(self.dummy, 'Start')

	def print_nodes(self):
		current = self.head

		while current != self.dummy:
			print(current.data)
			current = current.next

	def insert(self, value):
		new_node = Node(None, value)
		current = self.head

		while(current.next != self.dummy and value > current.next.data):
			current = current.next

	new_node.next = current.next
	current.next = new_node

	def remove(self, value):
		print("List is empty!!")
		return

	

	while (current.next.data != value and current.next != self.dummy):

	while (current.data != value)

	def isEmpty():
		current = self.head

		if current.next == self.dummy:
			return True
		else:
			return False


class Node
	def _init_(self, node, data):
		self.data = data
		self.next = node

