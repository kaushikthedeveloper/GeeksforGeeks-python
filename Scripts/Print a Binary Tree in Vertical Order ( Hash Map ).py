# http://www.geeksforgeeks.org/print-binary-tree-vertical-order/
# Hash Map based

from collections import defaultdict

# Basic Tree structure
class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


# Derived Class
# Distance from class -> Left child(--) and Right child(++)
class ModifiedNode(Node):
    def __init__(self, data: int):
        Node.__init__(self, data)
        # store Node's Vertical Distance from root
        self.dist_from_root = None


# Used to store the [Node data] against its {dist_from_root value}
dist_data = defaultdict(list)


def vertical_traverse(head: Node):
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


def assign_dist(head: Node, distance: int):
    global dist_data
    if head is None:
        return

    # Store the distance in dist_from_data
    head.dist_from_root = distance
    # Add (append) the dist in a dictionary
    dist_data[head.dist_from_root].append(head.data)

    # Traverse the child nodes
    assign_dist(head.left, distance - 1)
    assign_dist(head.right, distance + 1)


# main
if __name__ == "__main__":
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

    print("Vertical Traversal")
    [print(x) for x in vertical_nodes]

"""
Input Explanation :
 - Tree is hard-coded as
            1
          /    \
         2      3
        / \    /  \
       4   5  6    7
               \   \
                8   9  

Output :
Vertical Traversal
4
2
1 5 6
3 8
7
9

"""

'''
Given a binary tree, print it vertically. The following example illustrates vertical order traversal.

           1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9 


The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9 
print-binary-tree-in-vertical-order

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

The idea is to traverse the tree once and get the minimum and maximum horizontal distance with respect to root. For the 
tree shown above, minimum distance is -2 (for node with value 4) and maximum distance is 3 (For node with value 9).
Once we have maximum and minimum distances from root, we iterate for each vertical line at distance minimum to maximum 
from root, and for each vertical line traverse the tree and print the nodes which lie on that vertical line.

Algorithm:

// min --> Minimum horizontal distance from root
// max --> Maximum horizontal distance from root
// hd  --> Horizontal distance of current node from root 
findMinMax(tree, min, max, hd)
     if tree is NULL then return;

     if hd is less than min then
           min = hd;
     else if hd is greater than max then
          *max = hd;

     findMinMax(tree->left, min, max, hd-1);
     findMinMax(tree->right, min, max, hd+1);


printVerticalLine(tree, line_no, hd)
     if tree is NULL then return;

     if hd is equal to line_no, then
           print(tree->data);
     printVerticalLine(tree->left, line_no, hd-1);
     printVerticalLine(tree->right, line_no, hd+1); 
Implementation:
Following is the implementation of above algorithm.

C++JavaPython
#include <iostream>
using namespace std;

// A node of binary tree
struct Node
{
    int data;
    struct Node *left, *right;
};

// A utility function to create a new Binary Tree node
Node* newNode(int data)
{
    Node *temp = new Node;
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

// A utility function to find min and max distances with respect
// to root.
void findMinMax(Node *node, int *min, int *max, int hd)
{
    // Base case
    if (node == NULL) return;

    // Update min and max
    if (hd < *min)  *min = hd;
    else if (hd > *max) *max = hd;

    // Recur for left and right subtrees
    findMinMax(node->left, min, max, hd-1);
    findMinMax(node->right, min, max, hd+1);
}

// A utility function to print all nodes on a given line_no.
// hd is horizontal distance of current node with respect to root.
void printVerticalLine(Node *node, int line_no, int hd)
{
    // Base case
    if (node == NULL) return;

    // If this node is on the given line number
    if (hd == line_no)
        cout << node->data << " ";

    // Recur for left and right subtrees
    printVerticalLine(node->left, line_no, hd-1);
    printVerticalLine(node->right, line_no, hd+1);
}

// The main function that prints a given binary tree in
// vertical order
void verticalOrder(Node *root)
{
    // Find min and max distances with resepect to root
    int min = 0, max = 0;
    findMinMax(root, &min, &max, 0);

    // Iterate through all possible vertical lines starting
    // from the leftmost line and print nodes line by line
    for (int line_no = min; line_no <= max; line_no++)
    {
        printVerticalLine(root, line_no, 0);
        cout << endl;
    }
}

// Driver program to test above functions
int main()
{
    // Create binary tree shown in above figure
    Node *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    root->right->left->right = newNode(8);
    root->right->right->right = newNode(9);

    cout << "Vertical order traversal is \n";
    verticalOrder(root);

    return 0;
}
Run on IDE

Output:
Vertical order traversal is
4
2
1 5 6
3 8
7
9
Time Complexity: Time complexity of above algorithm is O(w*n) where w is width of Binary Tree and n is number of nodes 
in Binary Tree. In worst case, the value of w can be O(n) (consider a complete tree for example) and time complexity 
can become O(n2).
'''
