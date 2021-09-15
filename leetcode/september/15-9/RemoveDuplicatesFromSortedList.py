# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
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
    def deleteDuplicates(self, head): # TIme limit exceeded for 1,1,1 cause handling two variables, and gives error if uncomment line 45
        # adding multiple if statements bad
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        temp =  head.next
        prev = head
        while prev and temp:
            if (temp.val == prev.val):
                prev.next = temp.next
                prev = prev.next
                temp = prev.next.next
            else:     
                prev = temp
                temp = temp.next
        return head

class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        while temp and temp.next:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    final = LinkedList()
    l1.append(1)
    l1.append(1)
    l1.append(1)
    # l1.append(2)
    # l1.append(3)
    # l1.printlist()
    final.head = Solution1().deleteDuplicates(l1.head)
    final.printlist()