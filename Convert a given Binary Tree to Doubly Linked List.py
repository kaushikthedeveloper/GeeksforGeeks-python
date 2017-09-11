#http://www.geeksforgeeks.org/convert-a-given-binary-tree-to-doubly-linked-list-set-4/

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder_traverse(head,result):
    if head is not None:
        inorder_traverse(head.left,result)
        result.append(head.data)
        inorder_traverse(head.right,result)


#main
if __name__=="__main__":
    """
    Constructing below tree
               5
             /   \
            3     6
           / \     \
          1   4     8
         / \       / \
        0   2     7   9  
    """
    #Create the above Tree
    head=Node(5)

    head.left=Node(3)
    head.left.left=Node(1)
    head.left.right=Node(4)
    head.left.left.left=Node(0)
    head.left.left.right=Node(2)

    head.right=Node(6)
    head.right.right=Node(8)
    head.right.right.left=Node(7)
    head.right.right.right=Node(9)

    #result will store the output
    result=[]
    inorder_traverse(head,result)

    print("Extracted Double Linked list is :")
    print(result)

"""
Output :
Extracted Double Linked list is :
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

'''
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

TreeToList

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

Below three different solutions have been discussed for this problem.
Convert a given Binary Tree to Doubly Linked List | Set 1
Convert a given Binary Tree to Doubly Linked List | Set 2
Convert a given Binary Tree to Doubly Linked List | Set 3

In the following implementation, we traverse the tree in inorder fashion. We add nodes at the beginning of current linked list and update head of the list using pointer to head pointer. Since we insert at the beginning, we need to process leaves in reverse order. For reverse order, we first traverse the right subtree before the left subtree. i.e. do a reverse inorder traversal.

C++Java
// C++ program to convert a given Binary
// Tree to Doubly Linked List
#include <stdio.h>
#include <stdlib.h>
 
// Structure for tree and linked list
struct Node
{
    int data;
    Node *left, *right;
};
 
// A simple recursive function to convert a given
// Binary tree to Doubly Linked List
// root     --> Root of Binary Tree
// head_ref --> Pointer to head node of created
//              doubly linked list
void BToDLL(Node* root, Node** head_ref)
{
    // Base cases
    if (root == NULL)
        return;
 
    // Recursively convert right subtree
    BToDLL(root->right, head_ref);
 
    // insert root into DLL
    root->right = *head_ref;
 
    // Change left pointer of previous head
    if (*head_ref != NULL)
        (*head_ref)->left = root;
 
    // Change head of Doubly linked list
    *head_ref = root;
 
    // Recursively convert left subtree
    BToDLL(root->left, head_ref);
}
 
// Utility function for allocating node for Binary
// Tree.
Node* newNode(int data)
{
    Node* node = new Node;
    node->data = data;
    node->left = node->right = NULL;
    return node;
}
 
// Utility function for printing double linked list.
void printList(Node* head)
{
    printf("Extracted Double Linked list is:\n");
    while (head)
    {
        printf("%d ", head->data);
        head = head->right;
    }
}
 
// Driver program to test above function
int main()
{
    /* Constructing below tree
               5
             /   \
            3     6
           / \     \
          1   4     8
         / \       / \
        0   2     7   9  */
    Node* root = newNode(5);
    root->left = newNode(3);
    root->right = newNode(6);
    root->left->left = newNode(1);
    root->left->right = newNode(4);
    root->right->right = newNode(8);
    root->left->left->left = newNode(0);
    root->left->left->right = newNode(2);
    root->right->right->left = newNode(7);
    root->right->right->right = newNode(9);
 
    Node* head = NULL;
    BToDLL(root, &head);
 
    printList(head);
 
    return 0;
}
Run on IDE
Output :

Extracted Double Linked list is:
0 1 2 3 4 5 6 7 8 9
Time Complexity: O(n), as the solution does a single traversal of given Binary Tree.
'''