from Node import *

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        s = ''
        if self.head:
            n = self.head
            while n.next:
               s += f'{n.data}, '
               n = n.next
            s += f'{n.data}'
            return s
        return 'List is empty'


    def append(self, d):
        last = Node(d)
        n = self.head

        if n:
            while n.next:
                n = n.next
            n.next = last
        else:
            self.head = last


    def delete(self, data):
        if (self.head.data == data):
            self.head = self.head.next
            return self.head

        n = self.head

        while n.next:
            if n.next.data == data:
                n.next = n.next.next
                return self
            n = n.next

        return self

    def remove_dups1(self):
        past = None
        present = self.head
        seen = set()

        while present:
            if present.data in seen:
                past.next = present.next
            else:
                seen.add(present.data)
                past = present
            present = present.next

    def remove_dups2(self):
        slow = self.head
        fast = None

        while slow:
            print(f'slow={slow}\n')
            fast = slow.next
            while fast:
                print(f'\tfast={fast}\n')
                if fast.data == slow.data:
                    print(f'\t\tmatched; next is {fast.next}')
                    slow.next = fast.next
                fast = fast.next
            slow = slow.next
