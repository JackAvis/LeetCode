# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# the idea is to take the smallest value from all of the linked lists, put it in our mergedList, then increment that linked list and repeat
# when done mark it with -10**4 + 1
class Solution(object):
    def mergeKLists(self, lists):
        if lists == []:
            return None
        mergedList = None
        ptrs = []
        for i in lists:
            if i:
                ptrs.append([i.val, i])
        if len(ptrs) == 0:
            return None
        mergedList = ListNode(val = self.findSmallest(ptrs), next=None)
        headptr = mergedList
        complete = False
        while not complete:
            nextVal = self.findSmallest(ptrs)
            if nextVal == float('inf'):
                complete = True
                break
            mergedList.next = ListNode(val = nextVal, next=None)
            mergedList = mergedList.next
        return headptr
    def findSmallest(self, ptrs):
        minVal = float('inf')
        minIndex = -1
        for i in range(len(ptrs)):
            if ptrs[i][0] <= minVal and ptrs[i][0] != -10**4 + 1 and ptrs[i][1] != None:
                minVal = ptrs[i][0]
                minIndex = i
        if ptrs[minIndex][1].next:
            ptrs[minIndex][1] = ptrs[minIndex][1].next
            ptrs[minIndex][0] = ptrs[minIndex][1].val
        else:
            ptrs[minIndex][0] = -10**4 + 1
        return minVal
