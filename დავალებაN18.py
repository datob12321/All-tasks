# Double Linked list - ეს არის Linked list-ის ერთ-ერთი სახეობა, რომლის კვანძებს(node) გააჩნიათ სამი
# თვისება-მნიშვნელობა, წინა ელემენტი და მომდევნო ელემენტი. ამგვარად, ორმაგი კავშირის რგოლის
#  დახმარებით სრულდება სიისთვის დამახასიათებელი მეთოდები. (append, remove, insert, pop და სხვა).

# პირველ რიგში შევქმნით კლასს, რომელიც დაგვიბრუნებს კვანძს, ანუ ობიექტს ზემოთ ნახსენები
# სამი თვისებით. წინა და მომდევნო წევრები(კვანძები) ნაგულისხმევად None-ია, რადგან მათ მნიშვნელობები
# სიის კლასიდან მიენიჭება.

class Node:
    def __init__(self, value):
        self.value = value
        self.preview = None
        self.next = None

    def __repr__(self):
        return str(self.value)


# ახლა ვქმნით კლასს, რომელიც მოგვცემს(დაგვიბრუნებს) ორმაგად დაკავშირებულ სიას. მას აქვს სამი თვისება:
# head-სიის პირველი ელემენტი, tail-სიის ბოლო ელემენტი, length-სიის სიგრძე, რომელიც თავდაპირველად 0-ის
# ტოლია(სწორედ ამიტომაა head და tail None-ის ტოლი).
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # პირველი ფუნქცია გვაქვს append, ახალი წევრის ბოლოში ჩამატება. ეს ნიშნავს იმას, რომ tail-მა ახალი წევრის
    #  მნიშვნელობა უნდა მიიღოს.

    def append(self, value):
        # კვანძის შექმნა
        new_node = Node(value)
        # როცა სია ცარიელია, ახალი კვანძის დამატებისას პირველი და ბოლო მნიშვნელობები ერთიდაიგივე იქნება.
        if self.length == 0:
            self.head = self.tail = new_node
            self.length += 1
        else:
            # მიმდინარე tail-ის შემდეგი წევრი None-დან ახალი წევრი უნდა გახდეს.
            self.tail.next = new_node
            # ახალი წევრის წინა წევრი მიმდინარე tail-ია.
            new_node.preview = self.tail
            # tail-ს ენიჭება ახალი წევრის მნიშვნელობა, საბოლოოდ კი სიის სიგრძე იზრდება.
            self.tail = new_node
            self.length += 1

    # გვაქვს, ასევე, მსგავსი ფუნქცია left_append იმ განსხვავებით, რომ იგი კვანძს თავში ამატებს, ანუ head-ად
    # ხდის. ახალი ელემენტი აქაც ანალოგიურად იქნება. უცვლელია სიის სიგრძის ცვლილების ასახვაც
    def left_append(self, value):
        new_node = Node(value)
        if self.length == 0:
            # ზუსტად წინა მეთოდის მსგავსი მდგომარეობა
            self.head = self.tail = new_node
            self.length += 1
        else:
            self.head.preview = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self, value, index):
        if index == 0:
            self.left_append(value)
        elif index == self.length:
            self.left_append(value)
        elif 0 < index < self.length:
            new_node = Node(value)
            current_node = self.head
            current_index = 0
            while current_index != index-1:
                current_node = current_node.next
                current_index += 1
            new_node.next = current_node.next
            current_node.next = new_node
            new_node.preview = current_node
            new_node.next.preview = new_node
            self.length += 1
        else:
            print("Index out of range")

    def pop(self):
        pop_node = self.tail
        if self.length == 0:
            print("List is already empty")
        elif self.length == 1:
            self.head.next = self.tail.next = None
            self.length -= 1
        else:
            self.tail.preview.next = None
            self.tail = self.tail.preview
            self.length -= 1
        return pop_node

    def left_pop(self):
        pop_node = self.head
        if self.length == 0:
            print("List is already empty")
        elif self.length == 1:
            self.head.next = self.tail.next = None
            self.length -= 1
        else:
            self.head = self.head.next
            self.head.preview = None
            self.length -= 1
        return pop_node

    def remove_by_value(self, value):
        if self.length == 0:
            return
        elif self.length == 1:
            if self.head.value == value:
                self.pop()
        else:
            if self.head.value == value:
                self.left_pop()
            elif self.tail.value == value:
                self.pop()
            else:
                current_node = self.head
                while current_node.next.value != value:
                    current_node = current_node.next
                current_node.next = current_node.next.next
                current_node.next.preview = current_node
                self.length -= 1

    def remove_by_index(self, index):
        if index == 0:
            self.left_pop()
        elif index == self.length - 1:
            self.pop()
        elif 0 < index < self.length - 1:
            current_node = self.head
            current_index = 0
            while current_index != index-1:
                current_node = current_node.next
                current_index += 1
            deleted_node = current_node.next
            current_node.next = deleted_node.next
            current_node.next.preview = current_node
        else:
            print("Index out of range")

    def clear(self):
        self.head.next = self.tail.preview = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def display(self):
        current_node = self.head
        if self.length == 0:
            print([])
        else:
            print(self.head, end='')
            while current_node.next is not None:
                print(f'<==>{current_node.next}', end='')
                current_node = current_node.next
            print()


my_list = DoubleLinkedList()
