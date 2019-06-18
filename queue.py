# Queue implementation in python
# using the functions enqueue(), dequeue() and peek()
# 
# FIFO structure - First in First out 
#
# C16735211 - Darren Byrne

class Queue:

	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def sizeQueue(self):
		return len(self.queue)

queue = Queue()
queue.enqueue(20)
queue.enqueue(60)
queue.enqueue(120)
queue.enqueue(200)
queue.enqueue(2000)

print("Queue: ", queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print("Queue: ", queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Queue: ", queue.sizeQueue())
