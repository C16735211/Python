# stack implementation in python
#
# C16735211 - Darren Byrne
#
#

class Stack:

	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def sizeStack(self):
		return len(self.stack)


stack = Stack()

stack.push(50)
stack.push(10)
stack.push(60)
stack.push(90)
stack.push(80)

print("Stack size ", stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print("Stack size ", stack.sizeStack())
print("Peek: ", stack.peek())
print("Popped: ", stack.pop())
print("Peek: ", stack.peek())
print("Stack size ", stack.sizeStack())

