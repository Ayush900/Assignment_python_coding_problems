class newnode:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root=None
    def insert(self , data):
        if self.root is None:
            self.root = newnode(data)
        else:
            self.insert1(data,self.root)
    def insert1(self,data,curr_node):
        if data<curr_node.data:
            if curr_node.left is None:
                curr_node.left = newnode(data)
            else:
                self.insert1(data,curr_node.left)

        else:
            if curr_node.right is None:
                curr_node.right = newnode(data)
            else:
                self.insert1(data,curr_node.right)


def noofelementsinleftview(root):
    if (not root):
        return
    q = []
    q.append(root)
    cnt=0
    while (len(q)):
        n = len(q)
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
            if (i == 1):
                cnt+=1
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
    return cnt


t = int(input())
for i in range(t):
    n=int(input())
    nodes = input()
    nodes = nodes.split()
    bst = BST()
    for j in range(len(nodes)):
        nodes[j]=int(nodes[j])
        bst.insert(nodes[j])
    print(noofelementsinleftview(bst.root))
