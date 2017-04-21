# -*- coding:utf-8 -*-
__author__ = 'Raychang'

#二叉树
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right


t = Tree(Tree("a", "b"), Tree("c", "d"))
print t.right
print t.right.left

#非二叉树
class Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next
t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))

print t
print t.kids
print t.kids.next
print t.kids.next.next
print t.kids.next.next.val
