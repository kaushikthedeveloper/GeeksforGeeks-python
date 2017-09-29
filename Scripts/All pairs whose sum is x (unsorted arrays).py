#http://www.geeksforgeeks.org/given-two-unsorted-arrays-find-pairs-whose-sum-x/
#Hashing

def sum_pairs(array1: list, array2: list, req_sum: int):
    sum_lists = []

    #hash array1 for later searching
    hash1 = { x:x for x in array1 }

    for y in array2:
        try:
            #if hash1[req_sum-y] exists
            x = hash1[req_sum - y]
            sum_lists.append([x,y])
        except:
            #the other number for pairing with y not found
            continue

    return sum_lists

#main
if __name__=="__main__":
    array1 = list(map(int,input().split()))
    array2 = list(map(int,input().split()))
    req_sum=int(input())

    pairs = sum_pairs(array1,array2,req_sum)
    print("Sum pairs for", req_sum,"are")
    print([pair for pair in pairs])



"""
Input Explanation :
 - List 1
 - List 2
 - Required sum

Input :
-1 -2 4 -6 5 7
6 3 4 0
8

Output :
Sum pairs for 8 are
[[5, 3], [4, 4]]

"""

'''
Given two unsorted arrays of distinct elements, the task is to find all pairs from both arrays whose sum is equal to x.

Examples:

Input :  arr1[] = {-1, -2, 4, -6, 5, 7}
         arr2[] = {6, 3, 4, 0}  
         x = 8
Output : 4 4
         5 3

Input : arr1[] = {1, 2, 4, 5, 7} 
        arr2[] = {5, 6, 3, 4, 8}  
        x = 9
Output : 1 8
         4 5
         5 4
Asked in : Amazon

Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
A Naive approach is to simply run two loops and pick elements from both arrays. One by one check that both elements sum is equal to given value x or not.

// C++ program to find all pairs in both arrays
// whose sum is equal to given value x
#include<bits/stdc++.h>
using namespace std;
 
// Function to print all pairs in both arrays
// whose sum is equal to given value x
void findPairs(int arr1[], int arr2[], int n,
                               int m, int x)
{
    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            if (arr1[i] + arr2[j] == x)
                cout << arr1[i] << " "
                     << arr2[j] << endl;
}
 
// Driver code
int main()
{
    int arr1[] = {1, 2, 3, 7, 5, 4};
    int arr2[] = {0, 7, 4, 3, 2, 1};
    int n = sizeof(arr1)/sizeof(int);
    int m = sizeof(arr2)/sizeof(int);
    int x = 8;
    findPairs(arr1, arr2, n, m, x);
    return 0;
}
Run on IDE
Output:

1 7
7 1
5 3
4 4
Time Complexity : O(n^2)
Auxiliary Space : O(1)

An Efficient solution of this problem is to hashing. Hash table is implemented using unordered_set in C++. We store all first array elements in hash table. For elements of second array, we subtract every element from x and check the result in hash table. If result is present, we print the element and key in hash (which is an element of first array).
C++Java
// C++ program to find all pair in both arrays
// whose sum is equal to given value x
#include<bits/stdc++.h>
using namespace std;
 
// Function to find all pairs in both arrays
// whose sum is equal to given value x
void findPairs(int arr1[], int arr2[], int n,
                               int m, int x)
{
    // Insert all elements of first array in a hash
    unordered_set<int> s;
    for (int i=0; i<n; i++)
        s.insert(arr1[i]);
 
    // Subtract sum from second array elements one
    // by one and check it's present in array first
    // or not
    for (int j=0; j<m; j++)
        if (s.find(x - arr2[j]) != s.end())
            cout << x-arr2[j] << " "
                 << arr2[j] << endl;
}
 
// Driver code
int main()
{
    int arr1[] = {1, 0, -4, 7, 6, 4};
    int arr2[] = {0 ,2, 4, -3, 2, 1};
    int x = 8;
    int n = sizeof(arr1)/sizeof(int);
    int m = sizeof(arr2)/sizeof(int);
    findPairs(arr1, arr2, n, m, x);
    return 0;
}
Run on IDE

Output:
6 2
4 4
6 2
7 1
Time Complexity : O(n)
Auxiliary Space : O(n)
'''