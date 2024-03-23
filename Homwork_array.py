import numpy as np
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        contents = []
        current = self.head
        while current:
            contents.append(current.data)
            current = current.next
        return contents

linked_list = LinkedList()
start_time_linked_list = time.time()
for i in range(1000):
    linked_list.append(i)
time_linked_list = time.time() - start_time_linked_list

numpy_array = np.array([])
start_time_numpy = time.time()
for i in range(1000):
    numpy_array = np.append(numpy_array, i)
time_numpy = time.time() - start_time_numpy

print("Tiempo de adición a la lista ligada: {:.6f} segundos".format(time_linked_list))
print("Tiempo de adición al array de Numpy: {:.6f} segundos".format(time_numpy))

print("Primeros y últimos 5 elementos de la lista ligada:", linked_list.display()[:5] + linked_list.display()[-5:])
print("Primeros y últimos 5 elementos del array de Numpy:", list(numpy_array[:5]) + list(numpy_array[-5:]))
