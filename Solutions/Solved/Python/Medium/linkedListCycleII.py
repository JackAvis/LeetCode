# whats true about the head of a linked list cycle 
# well its the first node which would show up twice when iterating
# 3->2->0->-4->(2)
class Solution(object):
    def detectCycle(self, head):
        nodes = set()
        def findCycle(head):
            while head:
                if head in nodes:
                    return head
                nodes.add(head)
                head = head.next
            return None
        return findCycle(head)