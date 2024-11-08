class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def insert_at(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_position = 0

        while current_node and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')

linked_list = LinkedList()
linked_list.insert_at(0, 10)
linked_list.insert_at(1, 20)
linked_list.insert_at(2, 30)
linked_list.insert_at(1, 15)

linked_list.display()

linked_list.remove_by_value(15)
linked_list.display()

linked_list.remove_by_value(10)
linked_list.display()
