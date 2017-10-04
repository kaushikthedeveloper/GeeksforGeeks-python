# http://www.geeksforgeeks.org/constant-time-range-add-operation-array/
# modified to work with any array and sum to be added

def range_add_op(array: list, ranges: list, addition: int):
    # work on the algorithm as we would for the array of 0s of len(array)
    arr_for_0 = [0 for i in range(len(array) + 1)]

    # work with the ranges (add at start and subtract at end+1)
    for start, end in ranges:
        arr_for_0[start] = arr_for_0[start] + addition
        arr_for_0[end + 1] = arr_for_0[end + 1] - addition

    previous_ele = 0

    # go through the list and calculate the sum that will come for each index
    for i, curr_ele in enumerate(arr_for_0[:len(array)]):
        previous_ele = previous_ele + curr_ele

        # add the sum we got from array_of_0s to the original array
        array[i] += previous_ele

    return array

# main
if __name__ == "__main__":
    array = list(map(int, input().split()))  # List of int
    addition = int(input())  # Sum to be added if the element comes within the range
    no_of_additions = int(input())  # number of ranges that will be provided
    ranges = []  # ranges provided

    # ranges given from index 0
    for i in range(no_of_additions):
        # get range from user
        ranges.append(list(map(int, input().split())))

    final_array = range_add_op(array, ranges, addition)

    print("Final list after additions")
    print(' '.join(str(x) for x in final_array))

"""
Input Explanation :
 - List of int
 - Sum to be added if the element comes within the range
 - Number of ranges that will be provided (no_of_additions) 
 - Ranges provided [start end] (no_of_additions lines)

Input :
10 20 10 0 10
10
3
1 4
2 3
0 2

Output :
Final list after additions
20 40 40 20 20

"""

'''
Given an array of size N which is initialized with all zeros. We are given many range add queries, which should be 
applied to this array. We need to print final updated array as our result.
Examples:

N = 6
Arr = [0, 0, 0, 0, 0, 0]
rangeUpdate1 [0, 2], add 100
Arr = [100, 100, 100, 0, 0, 0]
rangeUpdate1 [1, 5], add 100
Arr = [100, 200, 200, 100, 100, 100]
rangeUpdate1 [2, 3], add 100
Arr = [100, 200, 300, 200, 100, 100]
Which is the final updated array.
Recommended: Please try your approach on {IDE} first, before moving on to the solution.

This problem can be solved using segment tree with lazy updates in O(log N) time per query but we can do better here, 
as update operation is not given. We can process each query in constant time using this logic, when a query to add V is 
given in range [a, b] we will add V to arr[a] and –V to arr[b+1] now if we want to get the actual values of array we 
will convert the above array into prefix sum array. See below example to understand,

Arr = [0, 0, 0, 0, 0, 0]
rangeUpdate1 [0, 2], add 100
Arr = [100, 0, 0, -100, 0, 0]
rangeUpdate1 [1, 5], add 100
Arr = [100, 100, 0, -100, 0, 0, -100]
rangeUpdate1 [2, 3], add 100
Arr = [100, 100, 100, -100, -100, 0, -100]    
Now we will convert above operation array to prefix sum array as shown below,
Arr = [100, 200, 300, 200, 100, 100]
Which is the final updated array.
So in effect, when we add a value V to specific index of array, It represents adding V to all elements right to this 
index, that is why we add –V after range to remove its effect after its range of add query.
Please note in below code, if range spans till the last index, the addition of –V is omitted to be in memory limit of 
the array.

C++Java
//  C++ program to get updated array after many array range
// add operation
#include <bits/stdc++.h>
using namespace std;
 
//  Utility method to add value val, to range [lo, hi]
void add(int arr[], int N, int lo, int hi, int val)
{
    arr[lo] += val;
    if (hi != N - 1)
       arr[hi + 1] -= val;
}
 
//  Utility method to get actual array from operation array
void updateArray(int arr[], int N)
{
    //  convert array into prefix sum array
    for (int i = 1; i < N; i++)
        arr[i] += arr[i - 1];
}
 
//  method to print final updated array
void printArr(int arr[], int N)
{
    updateArray(arr, N);
    for (int i = 0; i < N; i++)
        cout << arr[i] << " ";
    cout << endl;
}
 
//  Driver code to test above methods
int main()
{
    int N = 6;
 
    int arr[N] = {0};
 
    //  Range add Queries
    add(arr, N, 0, 2, 100);
    add(arr, N, 1, 5, 100);
    add(arr, N, 2, 3, 100);
 
    printArr(arr, N);
    return 0;
}
Run on IDE

Output:
100 200 300 200 100 100
'''
