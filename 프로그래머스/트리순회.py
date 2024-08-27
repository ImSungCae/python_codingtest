# 전위 순회 탐색 코드
def preorder(a):
    if a <= N:
        print(tree[a], end=' ')
        preorder(a*2)
        preorder(a*2 + 1)

# N = 9
# tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
# print(tree)
# preorder(1)

#출력 A B D H I E C F G

# 중위 순회 탐색 코드
def inorder(a):
    if a <= N:
        inorder(a*2)
        print(tree[a], end=' ')
        inorder(a*2 + 1)

# N = 9
# tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
# print(tree)
# inorder(1)

#출력 H D I B E A F C G

# 후위 순회 탐색 코드
def postorder(a):
    if a <= N:
        postorder(a*2)
        postorder(a*2 + 1)
        print(tree[a], end=' ')

N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
print(tree)
postorder(1)

#출력 H I D E B F G C A
