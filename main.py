from typing import List


# Definition for a binary tree node.
class Node:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def fillLevels(self, node: Node, level=0):
    if node == None or node.val == None:
      return

    if len(self.levels) <= level:
      self.levels.append([node.val])
    else:
      self.levels[level].append(node.val)

    if node.left != None:
      self.fillLevels(node.left, level + 1)
    if node.right != None:
      self.fillLevels(node.right, level + 1)

  def levelOrder(self, root: Node) -> List[List[int]]:
    self.levels = []

    self.fillLevels(root)

    return self.levels


my = Solution()
n = Node(3, Node(9), Node(20, Node(15), Node(7)))
ans = my.levelOrder(n)
goal_ans = [[3], [9, 20], [15, 7]]
print("ans: correct? - %s" % str(ans == goal_ans), ans)

# Runtime: 32 ms, faster than 76.22% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.4 MB, less than 6.45% of Python3 online submissions for Binary Tree Level Order Traversal.

# Runtime: 24 ms, faster than 98.26% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.6 MB, less than 6.45% of Python3 online submissions for Binary Tree Level Order Traversal.