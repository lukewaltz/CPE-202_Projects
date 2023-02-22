class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item, next=None, prev=None):  # initialize as none
        self.item = item
        self.next = next
        self.prev = prev


def search_helper(self, temp, value):
    if temp.item == value:  # item found
        return True
    elif temp == self.dummy.prev:  # traversed whole lst
        return False
    elif temp.item > value:  # passed values spot in the list and it wasn't there
        return False
    return search_helper(self, temp.next, value)  # recursive call


def reverse_helper(self, temp):
    if temp.item == self.dummy:
        return []
    return [temp.item] + reverse_helper(self, temp.prev)


def size_helper(self, temp):
    # adds one until the end of the list and returns count
    if temp == self.dummy:
        return 0
    return size_helper(self, temp.next) + 1


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.dummy.next == self.dummy:
            return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  Assume that all items added to your 
           list can be compared using the < operator and can be compared for equality/inequality.
           Make no other assumptions about the items in your list'''

        if self.is_empty():
            place = Node(item)
            place.prev = self.dummy
            place.next = self.dummy
            self.dummy.next = place
            self.dummy.prev = place
            return True
        if self.search(item):
            # item already in the list
            return False
        else:
            temp = self.dummy.next
            place = Node(item)
            while temp is not self.dummy and item > temp.item:
                # traverse list until item is greater value or end of list is reached
                temp = temp.next
            if temp.item != item:
                # adds new node right before the current temp Node
                place.prev = temp.prev
                place.next = temp
                temp.prev.next = place
                temp.prev = place
                return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        temp = self.dummy
        if self.is_empty():
            return False
        else:
            while temp.next != self.dummy:
                if temp.next.item == item:
                    # fills the hole left by the removed item
                    temp.next = temp.next.next
                    temp.next.prev = temp
                    return True
                else:
                    # keep moving through the list
                    temp = temp.next
            return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return None
        temp = self.dummy.next
        # starts first non-dummy node as index 0
        index = 0
        while temp.item != item:
            # move through list until item found
            temp = temp.next
            index += 1
        return index

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        node1 = self.dummy.next
        # starts traversal at first non-dummy node
        num_items = 0
        # value compared to desired index
        if self.is_empty():
            # empty list
            raise IndexError
        if index < 0:
            # negative index
            raise IndexError
        while node1 != self.dummy:
            if num_items == index:
                temp = node1.item
                node1.prev.next = node1.next
                node1.next.prev = node1.prev
                return temp
            else:
                node1 = node1.next
                num_items += 1
        else:
            raise IndexError

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        temp = self.dummy.next  # starts by looking at first non-dummy node
        return search_helper(self, temp, item)  # call to helper func

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        return_lst = []
        temp = self.dummy.next  # starts by looking at first non-dummy node
        while temp is not self.dummy:
            # add to list
            return_lst.append(temp.item)
            # focus on next node
            temp = temp.next
        return return_lst

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        temp = self.dummy.prev  # starts by looking at first non-dummy node
        return reverse_helper(self, temp)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        temp = self.dummy  # starts at dummy node as the 0th term and counts from there.
        return size_helper(self, temp.next)
