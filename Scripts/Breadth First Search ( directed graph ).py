# http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/

from collections import defaultdict

# Basic Tree structure
class Node:
    def __init__(self):
        # default dictionary to store graph
        # key : Node , values : NeighbouringNodes
        self.graph = defaultdict(list)

    # since graph is bidirectional, add as neighbour both ways (both sources)
    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, source: int):

        bfs_traverse = []

        # keep track of nodes traversed already
        is_visited = [False] * len(self.graph)
        # Queue used for keeping track of next node to be travelled - start with Source
        queue = [source]

        # mark source as visited (as its already added to queue_
        is_visited[source] = True

        while len(queue) > 0:

            # pop (first) element of the queue
            curr_node = queue.pop(0)
            bfs_traverse.append(curr_node)

            # add the neighbouring nodes that were still not visited
            for neighbour_node in self.graph[curr_node]:
                if not is_visited[neighbour_node]:
                    queue.append(neighbour_node)
                    # make visited True as they join queue
                    is_visited[neighbour_node] = True

        return bfs_traverse


def run_bfs(node: Node, source: int):
    return node.bfs(source)

# main
if __name__ == "__main__":
    """
        Constructing below graph
                   0
                 /   \
                1     2
               /  \  /
              3 --- 4
               \   /
                 5
    """

    node = Node()
    node.add_edge(0, 1)
    node.add_edge(0, 2)
    node.add_edge(1, 3)
    node.add_edge(1, 4)
    node.add_edge(2, 4)
    node.add_edge(3, 4)
    node.add_edge(3, 5)
    node.add_edge(4, 5)

    bfs_traverse = run_bfs(node, 0)

    print("Breadth First Search traversal")
    print(' '.join(str(ele) for ele in bfs_traverse))

"""
Input Explanation :
 - Graph is harcoded as :
               0
             /   \
            1     2
           /  \  /
          3 --- 4
           \   /
             5

Output :
Breadth First Search traversal
0 1 2 3 4 5

"""

'''
Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this 
post). The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid 
processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are 
reachable from the starting vertex.
For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for all 
adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don’t mark visited vertices, then 2 will be processed 
again and it will become a non-terminating process. A Breadth First Traversal of the following graph is 2, 0, 3, 1.

Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
Following are C++ and Java implementations of simple Breadth First Traversal from a given source.

The C++ implementation uses adjacency list representation of graphs. STL‘s list container is used to store lists of 
adjacent nodes and queue of nodes needed for BFS traversal.

C++JavaPython
// Program to print BFS traversal from a given source vertex. BFS(int s) 
// traverses vertices reachable from s.
#include<iostream>
#include <list>
 
using namespace std;
 
// This class represents a directed graph using adjacency list representation
class Graph
{
    int V;    // No. of vertices
    list<int> *adj;    // Pointer to an array containing adjacency lists
public:
    Graph(int V);  // Constructor
    void addEdge(int v, int w); // function to add an edge to graph
    void BFS(int s);  // prints BFS traversal from a given source s
};
 
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}
 
void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w); // Add w to v’s list.
}
 
void Graph::BFS(int s)
{
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    for(int i = 0; i < V; i++)
        visited[i] = false;
 
    // Create a queue for BFS
    list<int> queue;
 
    // Mark the current node as visited and enqueue it
    visited[s] = true;
    queue.push_back(s);
 
    // 'i' will be used to get all adjacent vertices of a vertex
    list<int>::iterator i;
 
    while(!queue.empty())
    {
        // Dequeue a vertex from queue and print it
        s = queue.front();
        cout << s << " ";
        queue.pop_front();
 
        // Get all adjacent vertices of the dequeued vertex s
        // If a adjacent has not been visited, then mark it visited
        // and enqueue it
        for(i = adj[s].begin(); i != adj[s].end(); ++i)
        {
            if(!visited[*i])
            {
                visited[*i] = true;
                queue.push_back(*i);
            }
        }
    }
}
 
// Driver program to test methods of graph class
int main()
{
    // Create a graph given in the above diagram
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
 
    cout << "Following is Breadth First Traversal "
         << "(starting from vertex 2) n";
    g.BFS(2);
 
    return 0;
}
# This code is contributed by Neelam Yadav
Run on IDE

Output:
Following is Breadth First Traversal (starting from vertex 2)
2 0 3 1
Note that the above code traverses only the vertices reachable from a given source vertex. All the vertices may not be 
reachable from a given vertex (example Disconnected graph). To print all the vertices, we can modify the BFS function to
 do traversal starting from all nodes one by one (Like the DFS modified version) .

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
'''
