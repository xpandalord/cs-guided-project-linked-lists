class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
​
    def __str__(self):
        return str(self.value)
​
​
def find_length(head):
    counter = 0
    current = head 
​
    while current is not None:
        counter += 1
        current = current.next
​
    return counter 
​
​
def find_middle(head):
    # fast-slow runners approach 
    slow = head 
    fast = head 
​
    # loop so long as fast is not None or fast's next is not None 
    while fast is not None and fast.next is not None:
        fast = fast.next.next 
        slow = slow.next 
​
    # at this point, fast has reached the end of the ll
    # return slow's value 
    return slow
​
    # # figure out the length of the linked list 
    # len = find_length(head)
    # # figure out the midpoint 
    # midpoint = len // 2
    # # traverse from the head to the middle
    # current = head 
​
    # # traverse through our ll until midpoint reaches 0 
    # while midpoint != 0:
    #     current = current.next 
    #     midpoint -= 1
​
    # return current
​
​
root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)
root.next.next.next.next = Node(7)
​
print(find_middle(root))