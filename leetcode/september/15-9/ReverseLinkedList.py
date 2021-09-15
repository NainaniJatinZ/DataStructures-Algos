# Given the head of a singly linked list, reverse the list, and return the reversed list.


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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dum = ListNode(0)
        # tail = dum
        p = None # None to break the first link 
        while head:
            tail = head
            head = head.next
            tail.next = p
            p = tail
        return p

    



if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    final = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l1.append(7)
    l2.append(3)
    l2.append(4)
    # print(l1.head.next.val)
    print(bool(l1.head))
    # final.head = Solution().reverseList(l1.head)
    # final.printlist()


 