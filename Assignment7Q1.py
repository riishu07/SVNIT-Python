class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        current = self.head
        prev = None
        
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return
        
        while current is not None and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            print("Key not found in the list")
            return
        
        prev.next = current.next
        current = None


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtEnd(10)
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.display()
    ll.insertAtBeginning(5)
    ll.display()
    ll.deleteNode(20)
    ll.display()

