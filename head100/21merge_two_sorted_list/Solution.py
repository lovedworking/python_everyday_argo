from head100.all_utils import ListNode
class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        if not list1:
            return list2
        if not list2:
            return list1
        preNode = ListNode
        head = preNode
        while list1 and list2:
            if list1.val <= list2.val:
                preNode.next = list1
                list1 = list1.next
            else:
                preNode.next = list2
                list2 = list2.next
            preNode = preNode.next
        preNode.next = list1 if list1 is not None else list2

        return head.next


sol = Solution()
sol.mergeTwoLists([1,3,5], [2,4])