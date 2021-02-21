# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # print(head)
        # 전체 linked-list인 head에 접근이 불가능 합니다.

        # print(node)
        
        """
        given node 를 건너 뛰기 위해 
        given node 의 val 를 다음 노드의 val 로 할당하고
        given node 의 next 노드를 다음 노드의 next 노드로 할당
        """
        node.val = node.next.val
        node.next = node.next.next