# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.headval = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # First attempt was using counter to see if loop exists, time problem obv
        # Tortoise and Hare algorithm
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False


if __name__ == "__main__": 
    list1 = LinkedList()
    list1.headval = ListNode(3)
    e = ListNode(2)
    f = ListNode(1)
    i = ListNode(0)
    g = ListNode(-4)
    list1.headval.next = e
    e.next = f
    f.next = i
    i.next = g
    # g.next = e
    print(Solution().hasCycle(list1.headval))
    