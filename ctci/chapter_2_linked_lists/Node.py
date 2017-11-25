

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return f'Node({self.data})'


    def __str__(self):
        return f'(data={self.data}; next={self.next})'


    def append(self, x):
        last = Node(x)
        n = self

        while n.next:
            n = n.next
        n.next = last
        print(f'Added {last} to {n}')


    def delete_node(self, delete_data):
        if (self.data == delete_data):
            return self.next

        n = self

        while n.next:
            if n.next.data == delete_data:
                n.next = n.next.next
                return self
            n = n.next


