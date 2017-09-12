#http://www.geeksforgeeks.org/level-order-tree-traversal/
#Hash Map based

from collections import defaultdict

#Basic Tree structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Derived Class
#Distance from class -> child(++)
class ModifiedNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        # store Node's Distance from root
        self.dist_from_root = None


# Used to store the [Node data] against its {dist_from_root value}
dist_data = defaultdict(list)

def vertical_traverse(head):
    # Sort the Dictionary based on its key (distance_from_root)
    # print the data
    vertical_nodes = []

    for key in sorted(dist_data):
        data_list = dist_data[key]
        # convert list of int to string
        data_list = ' '.join(str(x) for x in data_list)
        # print(data_list)
        vertical_nodes.append(data_list)

    return vertical_nodes


def assign_dist(head, distance):
    global dist_data
    if head is None:
        return

    # Store the distance in dist_from_data
    head.dist_from_root = distance
    # Add (append) the dist in a dictionary
    dist_data[head.dist_from_root].append(head.data)

    # Traverse the child nodes
    assign_dist(head.left, distance + 1)
    assign_dist(head.right, distance + 1)

#main
if __name__=="__main__":
    """
        Constructing below tree
                1
              /    \
             2      3
            / \    /  \
           4   5  6    7
                    \   \
                     8   9  
        """
    # Create the above Tree
    head = ModifiedNode(1)

    head.left = ModifiedNode(2)
    head.left.left = ModifiedNode(4)
    head.left.right = ModifiedNode(5)

    head.right = ModifiedNode(3)
    head.right.left = ModifiedNode(6)
    head.right.right = ModifiedNode(7)
    head.right.left.right = ModifiedNode(8)
    head.right.right.right = ModifiedNode(9)

    # distance from root to nodes -> dist_from_root
    assign_dist(head, 0)
    vertical_nodes = vertical_traverse(head)

    print("Level Order Traversal")
    [print(x) for x in vertical_nodes]


"""
Input Explanation :
Tree is hard-coded as
            1
          /    \
         2      3
        / \    /  \
       4   5  6    7
               \   \
                8   9  

Output :
Level Order Traversal
1
2 3
4 5 6 7
8 9

"""

'''
Level order traversal of a tree is breadth first traversal for the tree.

METHOD 1 (Use function to print a given level)

Algorithm:
There are basically two functions in this method. One is to print all nodes at a given level (printGivenLevel), and other is to print level order traversal of the tree (printLevelorder). printLevelorder makes use of printGivenLevel to print nodes at all levels one by one starting from root.

/*Function to print level order traversal of tree*/
printLevelorder(tree)
for d = 1 to height(tree)
   printGivenLevel(tree, d);

/*Function to print all nodes at a given level*/
printGivenLevel(tree, level)
if tree is NULL then return;
if level is 1, then
    print(tree->data);
else if level greater than 1, then
    printGivenLevel(tree->left, level-1);
    printGivenLevel(tree->right, level-1);
Implementation:
CJavaPython
// Recursive C program for level order traversal of Binary Tree
#include <stdio.h>
#include <stdlib.h>
 
/* A binary tree node has data, pointer to left child
   and a pointer to right child */
struct node
{
    int data;
    struct node* left, *right;
};
 
/* Function protoypes */
void printGivenLevel(struct node* root, int level);
int height(struct node* node);
struct node* newNode(int data);
 
/* Function to print level order traversal a tree*/
void printLevelOrder(struct node* root)
{
    int h = height(root);
    int i;
    for (i=1; i<=h; i++)
        printGivenLevel(root, i);
}
 
/* Print nodes at a given level */
void printGivenLevel(struct node* root, int level)
{
    if (root == NULL)
        return;
    if (level == 1)
        printf("%d ", root->data);
    else if (level > 1)
    {
        printGivenLevel(root->left, level-1);
        printGivenLevel(root->right, level-1);
    }
}
 
/* Compute the "height" of a tree -- the number of
    nodes along the longest path from the root node
    down to the farthest leaf node.*/
int height(struct node* node)
{
    if (node==NULL)
        return 0;
    else
    {
        /* compute the height of each subtree */
        int lheight = height(node->left);
        int rheight = height(node->right);
 
        /* use the larger one */
        if (lheight > rheight)
            return(lheight+1);
        else return(rheight+1);
    }
}
 
/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
struct node* newNode(int data)
{
    struct node* node = (struct node*)
                        malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
 
    return(node);
}
 
/* Driver program to test above functions*/
int main()
{
    struct node *root = newNode(1);
    root->left        = newNode(2);
    root->right       = newNode(3);
    root->left->left  = newNode(4);
    root->left->right = newNode(5);
 
    printf("Level Order traversal of binary tree is \n");
    printLevelOrder(root);
 
    return 0;
}
Run on IDE

Output:
Level order traversal of binary tree is - 
1 2 3 4 5 
Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel() takes O(n) time where n is the number of nodes in the skewed tree. So time complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).






METHOD 2 (Use Queue)

Algorithm:
For each node, first the node is visited and then it’s child nodes are put in a FIFO queue.

printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children (first left then right children) to q
    c) Dequeue a node from q and assign it’s value to temp_node
Implementation:
Here is a simple implementation of the above algorithm. Queue is implemented using an array with maximum size of 500. We can implement queue as linked list also.
CC++JavaPython
// Iterative Queue based C program to do level order traversal
// of Binary Tree
#include <stdio.h>
#include <stdlib.h>
#define MAX_Q_SIZE 500
 
/* A binary tree node has data, pointer to left child
   and a pointer to right child */
struct node
{
    int data;
    struct node* left;
    struct node* right;
};
 
/* frunction prototypes */
struct node** createQueue(int *, int *);
void enQueue(struct node **, int *, struct node *);
struct node *deQueue(struct node **, int *);
 
/* Given a binary tree, print its nodes in level order
   using array for implementing queue */
void printLevelOrder(struct node* root)
{
    int rear, front;
    struct node **queue = createQueue(&front, &rear);
    struct node *temp_node = root;
 
    while (temp_node)
    {
        printf("%d ", temp_node->data);
 
        /*Enqueue left child */
        if (temp_node->left)
            enQueue(queue, &rear, temp_node->left);
 
        /*Enqueue right child */
        if (temp_node->right)
            enQueue(queue, &rear, temp_node->right);
 
        /*Dequeue node and make it temp_node*/
        temp_node = deQueue(queue, &front);
    }
}
 
/*UTILITY FUNCTIONS*/
struct node** createQueue(int *front, int *rear)
{
    struct node **queue =
        (struct node **)malloc(sizeof(struct node*)*MAX_Q_SIZE);
 
    *front = *rear = 0;
    return queue;
}
 
void enQueue(struct node **queue, int *rear, struct node *new_node)
{
    queue[*rear] = new_node;
    (*rear)++;
}
 
struct node *deQueue(struct node **queue, int *front)
{
    (*front)++;
    return queue[*front - 1];
}
 
/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
struct node* newNode(int data)
{
    struct node* node = (struct node*)
                        malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
 
    return(node);
}
 
/* Driver program to test above functions*/
int main()
{
    struct node *root = newNode(1);
    root->left        = newNode(2);
    root->right       = newNode(3);
    root->left->left  = newNode(4);
    root->left->right = newNode(5);
 
    printf("Level Order traversal of binary tree is \n");
    printLevelOrder(root);
 
    return 0;
}
Run on IDE

Output:
Level order traversal of binary tree is - 
1 2 3 4 5 
Time Complexity: O(n) where n is number of nodes in the binary tree
'''