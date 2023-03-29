#!/usr/nin/python3

"""Build a Singly linked list from a Node class"""


class Node:
    """A Node of a linked list
    args:
         data (int) the data to store in the node
         next_node istance of a Node or None
    """
    def __init__(self, data, next_node=None):
        """Initialize a new Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Set/Get data attriabute of a node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Set/Get next_node of a Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Initialize a Singly linked list from a Node"""

    def __init__(self):
        """Initialize a new singlyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to a Node list
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
             value (int) data for a Node
        """

        new = Node(value, self.__head)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                temp = temp.next_node

            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Prints the data of a SinglyLinkedList"""
        values = []
        temp = self.__head
        while (temp is not None):
            values.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(values))
