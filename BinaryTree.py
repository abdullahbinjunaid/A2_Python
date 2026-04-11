Tree = ["A","B","C","D","E",None,"F"]
#Preorder Traversal
def Preorder(Tree,index = 0): #initializing the value zero of index at the start of the function 
    if (index >= len(Tree)) or (Tree[index] is None):
        return
    print(Tree[index], end = " ") #Root
    Preorder(Tree, 2 * index + 1) #Left
    Preorder(Tree, 2 * index + 2) #Right.
    
print(Preorder(Tree)) 

#Inorder Traversal
def Inorder(Tree,index = 0):
    if (index >= len(Tree)) or (Tree[index] is None):
        return
    Inorder(Tree, 2 * index + 1) #Left
    print(Tree[index], end = " ") #Root
    Inorder(Tree, 2 * index + 2) #Right.

print(Inorder(Tree))
    
    
    
#Inorder Traversal
def Postorder(Tree,index = 0):
    if (index >= len(Tree)) or (Tree[index] is None):
        return
    Postorder(Tree, 2 * index + 1) #Left
    Postorder(Tree, 2 * index + 2) #Right.
    print(Tree[index], end = " ") #Root
    
    
(Postorder(Tree))