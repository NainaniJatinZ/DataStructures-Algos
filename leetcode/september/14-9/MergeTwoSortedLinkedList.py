# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head

        while temp:
            print(temp.val, end = "->")
            temp = temp.next
    
    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node   


    
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # trying same as merge sort part, having a dummy node to return the head
        dum = ListNode(0)
        tail = dum

        while True:
            # after they are empty, simply assign the remaining
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next 
        return dum.next    

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    final = LinkedList()
    l1.append(-1)
    l1.append(2)
    l1.append(4)
    l2.append(1)
    l2.append(3)
    l2.append(4)
    final.head = Solution().mergeTwoLists(l1.head, l2.head)
    final.printlist()


# Recursively
# def mergeTwoLists2(self, l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     if l1.val < l2.val:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = self.mergeTwoLists(l1, l2.next)
#         return l2

# Try inplace after
