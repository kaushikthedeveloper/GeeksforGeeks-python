#http://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

def triplet_sum(array: list, req_sum: int):
    triplets = []

    if len(array) < 3:
        return None

    array = sorted(array)

    #First loop takes the center value among the triplet
    for mid in range(1,len(array)):
        low = 0
        high = len(array) - 1

        while low<mid and high>mid :

            #if required sum triplet
            if array[low]+array[mid]+array[high] == req_sum:
                triplets.append([array[low], array[mid], array[high]])
                break

            #if present sum is greater than required sum, decrease high
            elif array[low]+array[mid]+array[high] > req_sum :
                high = high - 1
                continue


            # if present sum is lower than required sum, increase low
            else :
                low = low + 1
                continue

    #if atleast 1 triplet found
    if len(triplets) > 0 :
        return triplets
    else :
        return None

#main
if __name__=="__main__":
    array = list(map(int,input().split()))
    req_sum = int(input())

    triplets = triplet_sum(array, req_sum)

    if triplets is None :
        print("No Triplet exist for sum :", req_sum)
    else :
        print("Triplet for the sum", req_sum)
        for triple in triplets:
            print(' '.join(str(x) for x in triple))

"""
Input Explanation :
 - list of numbers
 - required sum

Input :
0 -1 1 2 3 4 -3 -2
3

Output :
Triplet for the sum 3
-1 0 4
-2 1 4
-3 2 4

"""

'''
Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. If there is such a triplet present in array, then print the triplet and return true. Else return false. For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24, then there is a triplet (12, 3 and 9) present in array whose sum is 24.

Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
Method 1 (Naive) 
A simple method is to generate all possible triplets and compare the sum of every triplet with the given value. The following code implements this simple method using three nested loops.
CJava
# include <stdio.h>
 
// returns true if there is triplet with sum equal
// to 'sum' present in A[]. Also, prints the triplet
bool find3Numbers(int A[], int arr_size, int sum)
{
    int l, r;
 
    // Fix the first element as A[i]
    for (int i = 0; i < arr_size-2; i++)
    {
       // Fix the second element as A[j]
       for (int j = i+1; j < arr_size-1; j++)
       {
           // Now look for the third number
           for (int k = j+1; k < arr_size; k++)
           {
               if (A[i] + A[j] + A[k] == sum)
               {
                 printf("Triplet is %d, %d, %d", A[i], A[j], A[k]);
                 return true;
               }
           }
       }
    }
 
    // If we reach here, then no triplet was found
    return false;
}
 
/* Driver program to test above function */
int main()
{
    int A[] = {1, 4, 45, 6, 10, 8};
    int sum = 22;
    int arr_size = sizeof(A)/sizeof(A[0]);
 
    find3Numbers(A, arr_size, sum);
 
    return 0;
}
Run on IDE

Output:
Triplet is 4, 10, 8
Time Complexity: O(n^3)



Method 2 (Use Sorting)
Time complexity of the method 1 is O(n^3). The complexity can be reduced to O(n^2) by sorting the array first, and then using method 1 of this post in a loop.
1) Sort the input array.
2) Fix the first element as A[i] where i is from 0 to array size – 2. After fixing the first element of triplet, find the other two elements using method 1 of this post.
C++Java
// C++ program to find a triplet
# include <bits/stdc++.h>
using namespace std;
 
// returns true if there is triplet with sum equal
// to 'sum' present in A[]. Also, prints the triplet
bool find3Numbers(int A[], int arr_size, int sum)
{
    int l, r;
 
    /* Sort the elements */
    sort(A, A+arr_size);
 
    /* Now fix the first element one by one and find the
       other two elements */
    for (int i=0; i<arr_size-2; i++)
    {
 
        // To find the other two elements, start two index
        // variables from two corners of the array and move
        // them toward each other
        l = i + 1; // index of the first element in the
                   // remaining elements
        r = arr_size-1; // index of the last element
        while (l < r)
        {
            if( A[i] + A[l] + A[r] == sum)
            {
                printf("Triplet is %d, %d, %d", A[i], 
                                         A[l], A[r]);
                return true;
            }
            else if (A[i] + A[l] + A[r] < sum)
                l++;
            else // A[i] + A[l] + A[r] > sum
                r--;
        }
    }
 
    // If we reach here, then no triplet was found
    return false;
}
 
/* Driver program to test above function */
int main()
{
    int A[] = {1, 4, 45, 6, 10, 8};
    int sum = 22;
    int arr_size = sizeof(A)/sizeof(A[0]);
 
    find3Numbers(A, arr_size, sum);
 
    return 0;
}
Run on IDE

Output:
Triplet is 4, 8, 10
Time Complexity: O(n^2)
'''