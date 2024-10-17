class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        current = head
        carry = 0

        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            current.next = ListNode(val)
            current = current.next

        return head.next

def create_linked_list(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

num_l1 = [int(num) for num in input().split()]
num_l2 = [int(num) for num in input().split()]

l1 = create_linked_list(num_l1)
l2 = create_linked_list(num_l2)

result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.val, end=' ')
    result = result.next
