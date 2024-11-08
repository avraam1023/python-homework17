# Node კლასის შექმნა, რომელიც წარმოადგენს ერთეულს, ანუ კვანძს დაკავშირებულ სიაში
class Node:
    def __init__(self, data=None):
        self.data = data  # კვანძის მონაცემთა ველი, რომელიც შეიცავს მნიშვნელობას
        self.next = None  # მიანიშნებს შემდეგ კვანძზე, თუ არ არსებობს - None


# დაკავშირებული სიის (LinkedList) კლასის შექმნა
class LinkedList:
    def __init__(self):
        self.head = None  # პირველი კვანძის მისამართის შესანახად, თავდაპირველად ცარიელია

    # მონაცემების დამატება დაკავშირებულ სიაში
    def append(self, data):
        new_node = Node(data)  # ახალი კვანძის შექმნა გადაცემული მონაცემებით
        if self.head is None:  # თუ სია ცარიელია
            self.head = new_node  # ახალი კვანძი ხდება სიის თავი (პირველი ელემენტი)
            return

        # სხვა შემთხვევაში, ვიპოვოთ სიის ბოლო კვანძი
        last_node = self.head
        while last_node.next:  # ვაგრძელებთ ბოლო კვანძამდე მისვლას
            last_node = last_node.next

        last_node.next = new_node  # ბოლო კვანძის შემდეგ ვამატებთ ახალ კვანძს

    # კვანძის წაშლა მითითებული ინდექსით
    def remove_at(self, index):
        if index < 0 and self.head is None:  # თუ ინდექსი ნაკლებია ნულზე ან სია ცარიელია, არ ვაგრძელებთ
            return

        if index == 0:  # თუ წასაშლელია პირველი კვანძი
            self.head = self.head.next  # სიის თავი გადავა შემდეგ კვანძზე
            return

        # სხვა შემთხვევაში, ვიპოვოთ წასაშლელი კვანძის წინა კვანძი
        current_node = self.head
        current_position = 0

        while current_node.next and current_position < index - 1:  # ვმოძრაობთ წინა კვანძამდე
            current_node = current_node.next
            current_position += 1

        if current_node.next:  # თუ წასაშლელი კვანძი არსებობს
            current_node.next = current_node.next.next  # წავშალოთ კვანძი, გაერთიანებით შემდეგ კვანძთან

    # სიის მონაცემების ეკრანზე გამოსახვა
    def display(self):
        current_node = self.head  # დავიწყოთ სიის თავიდან
        while current_node is not None:  # ვივლით ყველა კვანძზე, ვიდრე სია არ დამთავრდება
            print(current_node.data, end=' -> ')  # გამოვიტანოთ კვანძის მონაცემი
            current_node = current_node.next  # გადავიდეთ შემდეგ კვანძზე


# დაკავშირებული სიის ობიექტის შექმნა
linked_list = LinkedList()

# სიის კვანძების დამატება
linked_list.append(10)
linked_list.append(5)
linked_list.append(25)
linked_list.append(12)
linked_list.append(11)

# სიის გამოტანა ეკრანზე
linked_list.display()
print()

# სიის მეორე ინდექსის კვანძის წაშლა და ხელახლა გამოტანა
linked_list.remove_at(2)
linked_list.display()
print()

# კიდევ ერთ ინდექსზე წაშლა და ხელახლა გამოტანა
linked_list.remove_at(2)
linked_list.display()
