class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node
        self.head = sorted_head

    def _sorted_insert(self, sorted_head, new_node):
        if not sorted_head or new_node.data < sorted_head.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head


def merge_sorted_lists(list1: LinkedList, list2: LinkedList):
    merged_list = LinkedList()

    while list1.head or list2.head:
        if list1.head and list2.head:
            if list1.head and not list2.head or list1.head < list2.head:
                move_node(list1, merged_list)
            else:
                move_node(list2, merged_list)

        elif list1.head:
            move_node(list1, merged_list)
        else:
            move_node(list2, merged_list)

    return merged_list


def move_node(source: LinkedList, dest: LinkedList):
    if not source.head:
        return
    new_node = source.head
    source.head = source.head.next
    new_node.next = None
    if not dest.head:
        dest.head = new_node
    else:
        last = dest.head
        while last.next:
            last = last.next
        last.next = new_node


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

llist.reverse()

print("Зв'язний список (reversed):")
llist.print_list()

llist.insertion_sort()
print("Зв'язний список (sorted):")
llist.print_list()

llist2 = LinkedList()
llist2.insert_at_beginning(2)
llist2.insert_at_beginning(4)
llist2.insert_at_beginning(6)
llist2.insert_at_beginning(8)
llist2.insert_at_beginning(10)
llist2.insertion_sort()

llist3 = merge_sorted_lists(llist, llist2)
print("Зв'язний список (merged):")
llist3.print_list()
