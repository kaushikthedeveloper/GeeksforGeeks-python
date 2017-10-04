# http://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def reverse(head: Node, k: int):
    # Code here
    node = head

    while node is not None:
        skip = k
        node_data_to_be_reversed = []
        temp_node = node

        # Record the data of Nodes to be reversed
        while (skip > 0) and temp_node is not None:
            node_data_to_be_reversed.append(temp_node.data)
            temp_node = temp_node.next
            skip -= 1

        # Traverse the list of data in reverse
        node_data_to_be_reversed.reverse()
        for data in node_data_to_be_reversed:
            # Replace the node data with reversed data
            node.data = data
            node = node.next

    return head


# main
if __name__ == "__main__":
    '''IMP Note : Work with LinkedList data structure'''

    data = list(map(int, input().split()))
    k = int(input())
    head = Node(data[0])
    orig_node = head

    # Build your LinkedList
    # 0 - n-1 (Create next Node for upto Last ele)
    for i in range(0, len(data) - 1):
        orig_node.next = Node(data[i + 1])
        orig_node = orig_node.next

    print("New Nodes : ")
    head = reverse(head, k)

    # Print the data of the Linked List
    temp_head = head
    while temp_head is not None:
        print(temp_head.data, end=' ')
        temp_head = temp_head.next

"""
Input Explanation :
 - List of numbers
 - 'k' nodes which are to be reversed

Input :
1 2 3 4 5 6
3

Output :
3 2 1 6 5 4

"""

'''
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).If a linked list 
is given as 1->2->3->4->5->6->7->8->NULL and k = 3 then output will be 3->2->1->6->5->4->8->7->NULL.

Input:
In this problem, method takes two argument: the head of the linked list and int k. You should not read any input from 
stdin/console.
The struct Node has a data part which stores the data and a next pointer which points to the next element of the 
linked list. 
There are multiple test cases. For each test case, this method will be called individually.

Output:
Reverse the linked list in the group of given size and return the reference of starting node(head) of the reversed 
Linked list .

Note: If you use "Test" or "Expected Output Button" use below example format
Example:
Input:
1
8
1 2 2 4 5 6 7 8
4

Output:
4 2 2 1 8 7 6 5
'''
