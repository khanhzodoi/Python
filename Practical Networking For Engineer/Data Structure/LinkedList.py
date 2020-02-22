class Node:
    # Function to initialize Node(None by default for the 'data' parameter)
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    # Function to initialize linked list by creating a head to hold null
    def __init__(self):
        self.head = self.tail = None

    # Function to traverse the list and print all its data from head to tail.
    def printList(self):
        temp = self.head
        while temp:  # Check temp is whether None or not
            if temp.next:
                print(str(temp.data) + " -> ", end=" ")
            else:
                print(str(temp.data))

            temp = temp.next

    # Function to check the list is empty or not
    def isEmpty(self):
        return not self.head

    # Function to insert Node to the node head
    def insertNode2Head(self, data):
        # Initialize a node for a given data
        node = Node(data)

        if self.isEmpty():  # The list is empty
            self.head = self.tail = node  # head list -> node <- head tail
            return
        else:  # The list is not empty
            node.next = self.head  # the new node -> the current node head
            self.head = node  # head list -> new head node we create at first

    # Function to insert Node to the list tail
    def insertNode2Tail(self, data):
        # Initialize a node for a given data
        node = Node(data)

        if self.isEmpty():  # The list is empty
            self.head = self.tail = node  # thead list -> new node <- head tail
            return
        else:  # The list is not empty
            self.tail.next = node  # list tail -> new node
            self.tail = node  # Update the list tail

    # Function to insert Node after a given Node in the list
    def insertNode2After(self, givenNode: Node, data: int):

        if self.isEmpty():  # The list is empty
            self.insertNode2Tail(data)
        else:  # The list is not empty
            # Initialize a node for a given data
            newNode = Node(data)

            newNode.next = givenNode.next  # newNode -> next node of givenNode
            givenNode.next = newNode  # givenNode -> newNode

            if givenNode is self.tail:  # q is at the list tail
                self.tail = newNode  # Update the list tail

    # Fucntion to remove the node from the list head
    def removeNodeAtHead(self):
        tempNode = self.head  # Hold the node head
        if self.isEmpty():  # Check the list is empty
            return
        else:  # otherwise
            self.head = tempNode.next  # update the head node
            if self.head is None:  # check if list have only one node to remove
                self.tail = None  # detach connection to the node

            tempNode.next = None  # detach connection of the old node head
            del tempNode  # delete tempNode

if __name__ == '__main__':
    firstNode = Node(1)
    list = SLinkedList()
    list.insertNode2Tail(1)
    list.insertNode2Tail(2)
    list.insertNode2After(list.head, 6)
    list.printList()

    list.removeNodeAtHead()
    list.printList()
