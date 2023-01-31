from queue import Empty
from random import randrange

class LinkedQueue:
    class _Node:
        __slots__ ='_element','_next'
        def __init__(self, element ,next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        t = False

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty(' Queue is empty ')
        return self._head._element

    def search(self, c):
        p = self._head
        t = True
        while p :
            if p._element == c:
                return t
            p = p._next

        return False

    def dequeue(self):
        if self.is_empty():
            raise Empty(' Queue is empty ')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)

        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        return 0

class HashTable:

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table LinkedQueue."""
        self.capacity = cap  # maximum size of the array of buckets
        self.length = 0  # length of inserted items
        self.buckets = [LinkedQueue() for i in range(0, self.capacity)]

    def hash (self, k):
        return hash(k)%self.capacity

    def __len__(self):
        return self.length

    def __setitem__(self, k, v):
        index = self.hash(k)
        add = self.buckets[index].enqueue(v)
        if add == 0:  # increase the length if new item is added
            self.length += 1

    def __delitem__(self,k):
        index = self.hash(k)
        value = self.buckets[index].dequeue()
        if value:
            self.length -= 1
        return value

    def __search__(self,k, c):  # resize bucket array to capacity c
        index = self.hash(k)
        return self.buckets[index].search(c)

ht = HashTable() #create a hash table
print("Length:", ht.__len__())
ht.__setitem__(99,"ashton") #add a new item
ht.__setitem__(87,"agar") #add a new item
ht.__setitem__(90,"emily") #add a new item
ht.__setitem__(89,"agar") #update
key = 90
value="emily"
print("Length:", ht.__len__())
print(f"The score of {value} exists {ht.__search__(key,value)}") #searching score
print(f"The score of deleted item with key/name {key} is {ht.__delitem__(99)}") #deleting item
print("Length:", ht.__len__())
print("Get all items")