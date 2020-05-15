class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        self.size = 1 if node is not None else 0
        self.oldest_node = self.head

    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.head.next is not None:
            prev_head = self.head
            self.head = prev_head.next
            self.head.prev= prev_head.prev
            prev_head.next = None
        self.size -= 1
            
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.oldest_node = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

            
        

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.removal = None
        self.storage = DoublyLinkedList()
        # self.oldest_node = self.storage.head

    def append(self, item):
        if self.storage.size < self.capacity:
            self.storage.add_to_tail(item)
        else:
            self.storage.oldest_node.value = item
            if self.storage.oldest_node.next is not None:
                self.storage.oldest_node = self.storage.oldest_node.next
            else:
                self.storage.oldest_node = self.storage.head


    def get(self):
        dll = []
        if self.storage.head:
            node = self.storage.head
            while node:
                dll.append(node.value)
                node = node.next
            return dll



