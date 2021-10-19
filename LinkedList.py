
# Creating a node class that is the building block of the linkedlist
class node:
    def __init__(self, data, next): # two attribute are data and the pointer to the next node
        self.data = data
        self.next = next

# Creating a linked list class
class Linkedlist:
    def __init__(self, head = None): # One attribute you need is head that is the pointer to the start of the list
        self.head = head
# Method to return the size of the linked list
    def size(self):
        count = 0
        current = self.head # Using current as a pointer to run through the list starting at the head
        while(current): # Using a while loop to loop through the elements
            count += 1
            current = current.next
        return count
# Method to insert an element at the start of the linked list
    def insert(self, data):
        self.head = node(data, self.head) # Just changing the head to the new element with the next of
        # the new node pointing to the current head.
# Method to insert an element at a particular index (zero indexed)
    def insertat(self, index, data):
        current = self.head # Using current to keep track of the pointers
        count = 0
        if(index >= self.size()): # If the index is greater that the size of the list return an error
            print('Index out of bounds')
        elif(index == 0): # If index is 0 then its same as adding at the start of the list
            self.head = node(data, self.head)
        else:
            while(count < index): # Traverse the list till we reach the index
                previous = current # Use previous to track the current pointer as we are incrementing it
                current = current.next
                count += 1
            previous.next = node(data,current) # Once you reach the index using previous, point the next
            # element after the index is reached to the new node and add the current pointer to the next
# Method to empty the linked list
    def empty(self):
        self.head = None # Point the head to null automatically empties the list

# Method to insert at the end of the list
    def insertend(self,data):
        # If list is empty, assign head to the new node
        if self.head == None:
            self.head = node(data, self.head)
        else:
            while (current): # Traverse through the whole list
                current = current.next
            current.next = node(data, None) # Once you reach the end assign the next element of the last node to the
            # new node and next pointer is None. Can also be current.next.
# Method to remove element from start
    def remove(self):
        self.head = self.head.next # Just slide the head to point to the next element in the list
# Method to remove element from an index
    def removeat(self, index):
        count = 0
        current = self.head
        if(index >= self.size()): # Check if index is out of bounds. If it is raise error
            print("Index out of bounds")
        elif(index == 0): # If index is 0 it is same as removing from start of the list
            self.head = self.head.next
        else:
            while(count < index): # Traverse till the index element is reached
                previous = current # Using previous to track the current pointer as we are incrementing it
                count += 1
                current = current.next
            previous.next = current.next # all we are doing here is pointing the next pointer at the element before
            # the index element to the node after the index element. Thus effectively deleting the element at the index
# Method to print the data of the linked list
    def show(self):
        current = self.head # Using current to traverse the list
        while(current):
            print(current.data) # Printing the data of each element in the linked list
            current = current.next

