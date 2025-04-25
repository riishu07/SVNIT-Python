class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print("Enqueued: " ,item)
    
    def dequeue(self):
        if not self.isEmpty():
            removedItem = self.queue.pop(0)
            print("Dequeued: " ,removedItem)
            return removedItem
        else:
            print("Queue is empty")
            return None
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue:", " -> ".join(map(str, self.queue)))


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()