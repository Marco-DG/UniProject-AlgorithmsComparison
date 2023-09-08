# Marco De Groskovskaja 08/02/23 - 15/02/23

class _LinkedList:

    class Node:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next
            
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, key, value):
        self.head = self.Node(key, value, self.head)
        self.size += 1

    def push_back(self, key, value):
        if self.head == None:
            self.head = self.Node(key, value)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = self.Node(key, value)
        self.size += 1

    def remove(self, key):
        curr = self.head
        prev = None
        found = False

        # If the list is empty
        if not curr:
            return False

        while not found:
            if curr.key == key:
                found = True
                self.size -= 1
            else:
                prev = curr
                curr = curr.next
            
        # If the key is the head
        if self.head.key == key:
            self.head = self.head.next
        # Else if curr in middle: update link
        else:
            prev.next = curr.next

        return found

    def search(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.key, curr.value)
            curr = curr.next
