# http://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
# CAREFUL : only works for an array of size 'n' having values [0,n-1]

def number_of_swaps(array: list):
    count = 0
    n = len(array)

    # create dict with {key:element , value:index}
    arr_dict = {}
    for index, ele in enumerate(array):
        arr_dict[ele] = index

    # To keep track of visited elements (initalise False)
    visited = [False] * n

    # Sort the dictionary with the key(ele) value
    for ele, index in sorted(arr_dict.items(), key=lambda x: x[0]):

        # if ele already visited or if its already at correct place, ignore
        if visited[ele] or ele == index:
            continue

        # otherwise count the elements in present cycle
        cycle_count = 0
        i = ele
        while not visited[i]:
            # element visited now
            visited[i] = True

            # visit the ele at its index
            i = arr_dict[i]
            cycle_count += 1

        # add the cycle_count to count (cycle-1 always for the loop)
        count += cycle_count - 1

    return count


# main
if __name__ == "__main__":
    # the elements have value based on start Index 0
    array = list(map(int, input().split()))

    min_swaps = number_of_swaps(array)

    print("Minimum number of swaps required to sort the array")
    print(min_swaps)

"""
Input Explanation :
 - List of int ( Array of size(n) should only contain elements from range 0 to n-1 )

Input :
1 3 4 0 2

Output :
Minimum number of swaps required to sort the array
3

"""

'''
This can be easily done by visualizing the problem as a graph. We will have n nodes and an edge directed from node i to 
node j if the element at i’th index must be present at j’th index in the sorted array.

a
Graph for {4, 3, 2, 1}
The graph will now contain many non-intersecting cycles. Now a cycle with 2 nodes will only require 1 swap to reach the 
correct ordering, similarly a cycle with 3 nodes will only require 2 swap to do so.

b
Graph for {4, 5, 2, 1, 5}
Hence,

ans = Σi = 1k(cycle_size – 1)
where k is the number of cycles

Below is the C++ implementation of the idea.
C++Java
// C++ program to find  minimum number of swaps
// required to sort an array
#include<bits/stdc++.h>
using namespace std;
 
// Function returns the minimum number of swaps
// required to sort the array
int minSwaps(int arr[], int n)
{
    // Create an array of pairs where first
    // element is array element and second element
    // is position of first element
    pair<int, int> arrPos[n];
    for (int i = 0; i < n; i++)
    {
        arrPos[i].first = arr[i];
        arrPos[i].second = i;
    }
 
    // Sort the array by array element values to
    // get right position of every element as second
    // element of pair.
    sort(arrPos, arrPos + n);
 
    // To keep track of visited elements. Initialize
    // all elements as not visited or false.
    vector<bool> vis(n, false);
 
    // Initialize result
    int ans = 0;
 
    // Traverse array elements
    for (int i = 0; i < n; i++)
    {
        // already swapped and corrected or
        // already present at correct pos
        if (vis[i] || arrPos[i].second == i)
            continue;
 
        // find out the number of  node in
        // this cycle and add in ans
        int cycle_size = 0;
        int j = i;
        while (!vis[j])
        {
            vis[j] = 1;
 
            // move to next node
            j = arrPos[j].second;
            cycle_size++;
        }
 
        // Update answer by adding current cycle.
        ans += (cycle_size - 1);
    }
 
    // Return result
    return ans;
}
 
// Driver program to test the above function
int main()
{
    int arr[] = {1, 5, 4, 3, 2};
    int n = (sizeof(arr) / sizeof(int));
    cout << minSwaps(arr, n);
    return 0;
}
Run on IDE

Output:
2
Time Complexity: O(n*log(n))
Auxiliary Space: O(n)
'''
