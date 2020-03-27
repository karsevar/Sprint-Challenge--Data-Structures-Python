from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the length of self.storage is less then self.capacity
            # add the item to the tail 
            # modify self.current to read the new tail.
        # else:
            # if self.current.next is None:
                # pop the self.storage.head from the doubly linked list 
                # add the new item to the storage through the method add_to_head
            # else:
                # since self.current is holding the most recent entry 
                # we know that the next node is the least recent 
                # modify the self.current.next.value with the passed in item 
        
        if self.capacity > len(self.storage):
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        else:
            if self.current.next is None:
                self.storage.remove_from_head() 
                self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # create a while loop that will traverse the linked list and 
        # return the values through appending them to the list provided 

        current_node = self.storage.head

        while current_node:
            list_buffer_contents.append(current_node.value) 
            current_node = current_node.next

        return list_buffer_contents

new_buffer = RingBuffer(5)
new_buffer.append('a')
new_buffer.append('b')
new_buffer.append('c') 
print(new_buffer.get())


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
