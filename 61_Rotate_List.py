# 61_Rotate_List
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, rotate the list to the right by k places.


# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class object:
    def rotateRight(self, head, k):
        raise NotImplementedError("you have to overide")


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        n = len(head)
        for i in range(len(head)):
            head.append(head[i])

        k = k % n
        headnode = ListNode(head[n - k])
        cur = headnode
        count = 1
        while count <= n:
            if count + 1 <= n:
                cur.next = ListNode(head[count + n - k])
                cur = cur.next
            count += 1

        # ------------------check------------------------

        # cur = headnode
        # while cur:
        #     print(cur.val, end=" -> ")
        #     cur = cur.next
        # print("None")
        # return [4, 5, 1, 2, 3]
        return headnode


class headisList(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1

        fst = head
        k %= n
        if k == 0:
            return head
        for i in range(0, n - k - 1):
            fst = fst.next

        sec = fst.next
        fst.next = None
        cur = sec
        while cur.next:
            cur = cur.next
        cur.next = head
        return sec


head, k = [1, 2, 3, 4, 5], 2
headislist = ListNode(head[0])
current = headislist
for i in range(1, len(head)):
    current.next = ListNode(head[i])
    current = current.next
solution = [Solution(), headisList()]
sol = solution[2]
# print(sol.rotateRight(head, k))
headnode = sol.rotateRight(headislist, k)
while headnode:
    print(headnode.val, end=" -> ")
    headnode = headnode.next
print("None")
