# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [3,9,20,null,null,15,7]
# []

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        print(root, "\n")
        
        # 트리구조는 재귀함수를 많이 사용합니다.
        
        # Q. deque(iterable, maxlength) 형태로 사용하다고 하는데, 이진트리 자료구조가 iterable 자료형이라고 봐도 되는건가 ?
        
        print(deque([root]), "\n")
        
        if root is None:
            answer = 0
        else:
            Q = deque([root])   # 원소 한개짜리 리스트 만들기
            depth = 0
            
            # 원소를 넣었다 뺐다 하며 원소 사라질 때 까지 반복
            while Q:
                depth += 1      # 해당 노드(부모노드)위치에 대해 카운트
            
                for _ in range(len(Q)):
                    cur_node = Q.popleft()      # 부모노드 빼서,
                    if cur_node.left:           # 왼쪽 자식노드 있으면 담기
                        Q.append(cur_node.left)
                    if cur_node.right:          # 오른쪽 자식노드 있으면 담기
                        Q.append(cur_node.right)
                        
            answer = depth
        
        return answer