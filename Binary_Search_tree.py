class Node: 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print(root.key), 
        inorder(root.right) 
def insert( node, key): 
    if node is None: 
        return Node(key)  
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
    return node 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val==node.val:
            return 0
        elif root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.val==node.val:
                return 0
            elif root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
def distanceFromRoot(root, x): 
    if root.key == x: 
        return 0
    elif root.key > x: 
        return 1 + distanceFromRoot(root.left, x) 
    return 1 + distanceFromRoot(root.right, x) 
def distanceBetween2(root, a, b): 
    if root == None: 
        return 0
    if root.key > a and root.key > b: 
        return distanceBetween2(root.left, a, b)  
    if root.key < a and root.key < b: # same path 
        return distanceBetween2(root.right, a, b) 
    if root.key >= a and root.key <= b: 
        return (distanceFromRoot(root, a) +
                distanceFromRoot(root, b)) 
def findDistWrapper(root, a, b): 
    if a > b: 
        a, b = b, a 
    return distanceBetween2(root, a, b) 
def minValueNode( node): 
    current = node 
    while(current.left is not None): 
        current = current.left 
    return current 
def deleteNode(root, key): 
    if root is None: 
        return root 
    if key < root.key: 
        root.left = deleteNode(root.left, key) 
    elif(key > root.key): 
        root.right = deleteNode(root.right, key) 
    else: 
        if root.left is None : 
            temp = root.right 
            root = None
            return temp 
        elif root.right is None : 
            temp = root.left 
            root = None
            return temp 
        temp = minValueNode(root.right) 
        root.key = temp.key 
        root.right = deleteNode(root.right , temp.key) 
    return root 
def maxDepth(node): 
    if node is None: 
        return 0 ; 
    else :  
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
if __name__=="__main__":
    root = None
    root = insert(root, 50) 
    root = insert(root, 30) 
    root = insert(root, 20) 
    root = insert(root, 40) 
    root = insert(root, 70) 
    root = insert(root, 60) 
    root = insert(root, 80) 
    inorder(root) 
    root = deleteNode(root, 20) 
    inorder(root) 
    root = deleteNode(root, 30) 
    inorder(root) 
    root = deleteNode(root, 50) 
    inorder(root) 
    print(maxDepth(root))
    res=findDistWrapper(root, 50, 60)
    print(res)
