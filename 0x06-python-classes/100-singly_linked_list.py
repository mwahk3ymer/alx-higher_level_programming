#!/usr/bin/python3
"""
This module defines the Node and SinglyLinkedList classes.
"""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node (private).
        __next_node (Node): The next node in the list (private).
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance with data and optional next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the list (default is None).

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not None or a Node object.

        Returns:
            None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the list.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.

        Args:
            value (Node): The next node in the list.

        Raises:
            TypeError: If value is not None or a Node object.

        Returns:
            None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        __head: The head node of the linked list (private).
    """

    def __init__(self):
        """
        Initializes an empty SinglyLinkedList instance.

        Returns:
            None.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value of the new node to be inserted.

        Returns:
            None.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representing the linked list.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

